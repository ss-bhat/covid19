from covid.lib.covid_request import CovIdRequest
from covid.model import country, country_stats


class CovId19Data(CovIdRequest):

    def __init__(self, *args, **kwargs):
        CovIdRequest.__init__(self, *args, **kwargs)

    def get_total_stats(self):
        """
        Shows the total death till now
        Assign: Vipin
        :return: dict
        """
        return country_stats.get_total_stats(self)

    def get_new_confirmed(self, period=None):
        """
        Periods should be current month or one manth previous data. No old data should be shown
        :param period:
        :return:
        """
        pass

    def get_new_recovered(self, period=None):
        """
        Periods should be current month or one manth previous data. No old data should be shown
        :param period:
        :return:
        """
        pass

    def get_all_records_by_country(self, show_geometry=False):
        """
        Get all the records for all the countries. This will return the latest values of
        confirmed, deaths and recovered.
        :return: dict
        """
        return country.get_all_records_by_country(self, show_geometry)

    def get_all_records_by_provinces(self):
        """
        Get all the records for all the provinces/state. This will return the latest values of
        confirmed, deaths and recovered.
        :return: dict
        """
        return country.get_all_records_by_provinces(self)

    def filter_by_country(self, show_geometry=False):
        """
        Extract the record for a given country. If show_geometry=True. Coordinates of the country will be shown.
        If no match in the country. Empty records are show
        :param show_geometry: boolean
        :return: dict
        """
        pass

    def filter_by_province(self):
        """
        Extract the record for a given province. If no province matched. Empty data is extracted.
        :return: dict
        """
        pass

    def show_available_countries(self):
        """
        Show all the available countries
        :return: dict
        """
        return country.show_available_countries(self)

    def show_available_regions(self):
        """
        Show all the available provinces/state
        :return:
        """
        return country.show_available_province(self)
