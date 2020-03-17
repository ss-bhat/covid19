import os
import csv


class CovId19Data:

    _actions_files = {
        "confirmed": "time_series_19-covid-Confirmed.csv",
        "deaths": "time_series_19-covid-Deaths.csv",
        "recovered": "time_series_19-covid-Recovered.csv"
    }

    _geojson_file = "{}/{}".format(os.path.dirname(os.path.dirname(os.path.realpath(__file__))), "countries.geojson")

    _country_mapping = {
        "us": "united states of america",
        "korea, south": "south korea",
        "korea, north": "north korea"
    }

    def __init__(self, *args, **kwargs):
        self._data_dir_path = "{}/{}".format(os.path.dirname(os.path.dirname(os.path.realpath(__file__))), "data")
        self._actions_files = kwargs.get("_actions_files", CovId19Data._actions_files)

    def _assign_loader(self):
        for _action in self._actions_files:

            setattr(self, _action, csv.DictReader(open(
                "{}/{}".format(self._data_dir_path, self._actions_files[_action]), 'r')))



