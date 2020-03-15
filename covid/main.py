from covid.base import CovIdRequest


class CovId19Data(CovIdRequest):

    def __init__(self, *args, **kwargs):
        CovIdRequest.__init__(self, *args, **kwargs)

    def get_total_deaths(self):
        pass

    def get_total_recovered(self):
        pass

    def get_total_confirmed(self):
        pass

    def get_total_active(self):
        pass

    def get_new_confirmed(self, period=None):
        pass

    def get_new_recovered(self, period=None):
        pass
