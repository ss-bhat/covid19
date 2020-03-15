from covid.lib.covid_request import CovIdRequest
from covid.model import country


class CovId19Data(CovIdRequest):

    def __init__(self, *args, **kwargs):
        CovIdRequest.__init__(self, *args, **kwargs)

    def get_total_deaths(self):
        """
        Shows the total death till now
        Assign: Vipin
        :return: dict
        """

    def get_total_recovered(self):
        """
        Shows total recovered till now
        Assign: Vipin
        :return: dict
        """
        pass

    def get_total_confirmed(self):
        """
        Shows total confirmed cases till now
        Assign: Vipin
        :return: dict
        """
        pass

    def get_total_active(self):
        """
        Shows total active cases till now
        Assign: Vipin
        :return: dict
        """

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

    def get_all_records_by_country(self):
        """
        Get all the records for all the countries. This will return the latest values of
        confirmed, deaths and recovered.
        :return: dict
        """
        return country.get_all_records_by_country(self)

    def get_all_records_by_provinces(self):
        """
        Get all the records for all the provinces/state. This will return the latest values of
        confirmed, deaths and recovered.
        :return: dict
        """
        return country.get_all_records_by_provinces(self)

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
