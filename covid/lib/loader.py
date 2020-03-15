import os
import csv


class CovId19Data:

    _actions_files = {
        "confirmed": "time_series_19-covid-Confirmed.csv",
        "deaths": "time_series_19-covid-Deaths.csv",
        "recovered": "time_series_19-covid-Recovered.csv"
    }

    def __init__(self, *args, **kwargs):
        self._data_dir_path = "{}/{}".format(os.path.dirname(os.path.dirname(os.path.realpath(__file__))), "data")
        self._actions_files = kwargs.get("_actions_files", CovId19Data._actions_files)
        self._assign_loader()

    def _assign_loader(self):
        for _action in self._actions_files:
            with open("{}/{}".format(self._data_dir_path, self._actions_files[_action])) as f:
                setattr(self, _action, csv.DictReader(f))



