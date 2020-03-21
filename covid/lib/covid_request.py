from covid.lib import errors
from covid.lib.loader import CovId19Data
import requests
import os
import datetime
import glob
import logging
log = logging.getLogger(__name__)


class CovIdRequest(CovId19Data):
    """
    This module sends the get request for the covid-19 git repository and downloads all the csv files and saves
    in the data directory. Stored file is refreshed only when current date is greater than the stored date.
    You can forcefully refresh the data using the force_refresh flag attribute.

    :parameter

    force: boolean
    _url: str (Do not use this as long as default url works good)
    _headers: str (Do not use this as long as default url works good)
    _actions_files: if more actions to be added in future. Customize this

    Note:
        All the files must be availabe in the repo folder /csse_covid_19_data/csse_covid_19_time_series
    """

    _URL = "https://raw.githubusercontent.com/CSSEGISandData/" \
           "COVID-19/master/csse_covid_19_data/csse_covid_19_time_series/{}"
    _headers = {
        "content-type": "text; charset=utf-8",
        "User-Agent": "python-covid19"
    }

    def __init__(self, *args, **kwargs):
        self._url = kwargs.get("_url", CovIdRequest._URL)  # In case if the source url is changed.
        self._headers = kwargs.get("_headers", CovIdRequest._headers)
        self._current_date = datetime.datetime.strptime(str(datetime.datetime.now().date()), "%Y-%m-%d")
        self.force_refresh = kwargs.get("force", False)
        CovId19Data.__init__(self, *args, **kwargs)
        self.run()

    def __repr__(self):
        """
        Representation of this class
        :return:
        """
        return CovIdRequest.__doc__

    def __str__(self):
        """
        On print get the all the actions available and the file names
        :return:
        """
        return str({
            "actions": self._actions_files,
            "message": "All files will be downloaded while instantiating this object. "
                       "Data will be refreshed once a day. If you want the fresh data, "
                       "please use the force=True, but not recommended",
        })

    def __call__(self, action=None):
        """
        On given action get the raw content of the file
        :param action: str (confirmed, recovered or death)
        :return:
        """
        if not action:
            raise errors.ActionNotFoundError("No action given")
        return self.get_raw_content(action)

    def _clean_data(self):
        """
        Cleans the data directory and removes all the files.
        :return:
        """
        _files = glob.glob("{}*.txt".format(self._data_dir_path))
        for _f in _files:
            os.remove(_f)

    def _check_if_file_exists(self):
        """
        Check if the file exists and returns boolean.
        :return:
        """
        _files = glob.glob("{}/*.csv".format(self._data_dir_path))
        if _files and (len(_files) == len(self._actions_files)):
            _date = datetime.datetime.fromtimestamp(os.path.getctime(_files[0])).date()
            _date_time = datetime.datetime.strptime(str(_date), "%Y-%m-%d")
            if _date_time < self._current_date:
                return False
            else:
                logging.debug("File already exists")
                return True
        else:
            return False

    def _save_file(self, content, file_name):
        """
        save the data in a file with name same as defiled in parameter _action_files
        :param content: str request content
        :param file_name: str file_name
        :return: None
        """

        _f = "{}/{}".format(self._data_dir_path, file_name)
        with open(_f, 'w') as f:
            f.write(content)
            f.close()

    def _get_request(self):

        for _action in self._actions_files:
            file_name = self._actions_files.get(_action)
            try:
                req = requests.get(self._url.format(file_name), headers=self._headers)
                _data = req.text
                yield _data, file_name
            except requests.exceptions.RequestException as e:
                self._clean_data()
                raise ConnectionError(e)

    def _clean_and_save_all(self):

        self._clean_data()
        for content, file_name in self._get_request():
            self._save_file(content, file_name)

    def _process(self):
        """
        Get the raw data form the covid19 visualization site site.
        url: https://gisanddata.maps.arcgis.com/apps/opsdashboard/index.html#/bda7594740fd40299423467b48e9ecf6
        More Info: https://systems.jhu.edu/
        :return:None
        """
        if self._check_if_file_exists():
            if self.force_refresh:
                logging.debug("Force download new data")
                self._clean_and_save_all()
            else:
                pass
        else:
            logging.debug("Downloading new files")
            self._clean_and_save_all()

    def get_raw_content(self, action):
        """
        Get the raw content in from the saved file.
        :return: str
        """
        try:
            _file_name = self._actions_files.get(action)
            if not _file_name:
                raise KeyError
            _path = "{}/{}".format(self._data_dir_path, _file_name)
            with open(_path, 'r') as f:
                content = f.read()
                f.close()
                return content
        except KeyError as e:
            raise errors.ActionNotFoundError("Action Not found")

    def run(self):
        """
        Get the data and save the data.
        :return:
        """
        self._process()
        self._assign_loader()

