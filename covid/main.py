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

    def get_all_regional_data(self):
        pass

    def get_all_country_data(self):
        country.get_all_country_data(self)

    def get_all_records_for_country(self, country=None):
        pass

    def get_all_records_for_region(self, region=None):
        pass

    def show_available_countries(self):
        pass

    def show_available_regions(self):
        pass
