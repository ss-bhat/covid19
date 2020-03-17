from covid.lib.covid_request import CovIdRequest
from covid.model import country as country_model, history


class CovId19Data(CovIdRequest):

    def __init__(self, *args, **kwargs):
        CovIdRequest.__init__(self, *args, **kwargs)

    def get_stats(self):
        """
        Shows the total death till now
        Assign: Vipin
        :return: dict
        """
        return country_model.get_total_stats(self)

    def get_all_records_by_country(self):
        """
        Get all the records for all the countries. This will return the latest values of
        confirmed, deaths and recovered.
        :return: dict
        """
        return country_model.get_all_records_by_country(self)

    def get_all_records_by_provinces(self):
        """
        Get all the records for all the provinces/state. This will return the latest values of
        confirmed, deaths and recovered.
        :return: dict
        """
        return country_model.get_all_records_by_provinces(self)

    def filter_by_country(self, country):
        """
        Extract the record for a given country.
        If no match in the country. Empty records are show
        :param country: str
        :return: dict
        """

        return country_model.filter_by_country(self, country)

    def filter_by_province(self, province):
        """
        Extract the record for a given province. If no province matched. Empty data is extracted.
        :return: dict
        """
        return country_model.filter_by_province(self, province)

    def show_available_countries(self):
        """
        Show all the available countries
        :return: dict
        """
        return country_model.show_available_countries(self)

    def show_available_regions(self):
        """
        Show all the available provinces/state
        :return:
        """
        return country_model.show_available_province(self)

    def get_history_by_country(self, country):
        """"
        The method returns the history statistics of all country
        """
        return history.get_history_by_country(self, country)

    def get_history_by_province(self, province):
        """"
        The method returns the history statistics of all country
        """
        return history.get_history_by_province(self, province)
