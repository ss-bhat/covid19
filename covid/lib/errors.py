

class CovidBaseException(Exception):
    pass


class ActionNotFoundError(CovidBaseException):
    pass


class CountryNotFound(CovidBaseException):
    pass


class ProvinceNotFound(CovidBaseException):
    pass


class ValidationError(CovidBaseException):
    pass
