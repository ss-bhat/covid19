from covid.lib import helper as h
from dateutil.parser import parse


def get_all_records_by_country(instance, show_geometry=False):
    """
    Collect all confirmed, recovered and deaths for all the countries
    :param instance: class instance
    :param show_geometry: boolean (if true show a multi polygon coordinates)
    :return: dict
    """
    result = dict()

    for _action in instance._actions_files.keys():
        reader = getattr(instance, _action)
        # Dict reader of the respective action
        for row in reader:
            # Country id
            _country = h.convert_label_to_id(row.get('Country/Region'))
            # Latest value i.e. last column of the ordered dict
            _key = list(row.keys())[-1]
            _val = int(row.get(_key))

            # Aggregation
            if _country in result:
                _cnty_data = result.get(_country)
                if _action in _cnty_data:
                    _cnty_data[_action] += _val
                else:
                    _cnty_data[_action] = _val
            else:
                # Dict structure of the return data
                result[_country] = dict()
                result[_country][_action] = _val
                result[_country]['label'] = row.get('Country/Region')
                result[_country]['last_updated'] = str(parse(_key))
                result[_country]['lat'] = row.get('Lat')
                result[_country]['long'] = row.get('Long')
                if show_geometry:
                    result[_country]['geometry'] = instance.get_polygon_for_country(row.get('Country/Region'))
    return result


def get_all_records_by_provinces(instance):
    """
    Collect all the data if the province column is not null and get corresponding latitude and longitude data
    :param instance: class instance
    :return: dict
    """

    result = dict()

    for _action in instance._actions_files.keys():
        reader = getattr(instance, _action)
        for row in reader:
            _province_label = row.get('Province/State')
            if _province_label:
                _province = h.convert_label_to_id(_province_label)
                _key = list(row.keys())[-1]
                _val = int(row.get(_key))
                # Aggregation
                if _province in result:
                    _province_data = result.get(_province)
                    if _action in _province_data:
                        _province_data[_action] += _val
                    else:
                        _province_data[_action] = _val
                else:
                    # Dict structure of the return data
                    result[_province] = dict()
                    result[_province][_action] = _val
                    result[_province]['label'] = _province_label
                    result[_province]['country'] = row.get('Country/Region')
                    result[_province]['lat'] = row.get('Lat')
                    result[_province]['long'] = row.get('Long')
                    result[_province]['last_updated'] = str(parse(_key))

    return result


def show_available_countries(instance):
    """
    Show all the available countries
    :param instance: class instance
    :return: dict
    """
    _actions = (
        "confirmed",
        "deaths",
        "recovered"
    )

    res = dict()

    for _item in _actions:
        reader = getattr(instance, _item)
        res[_item] = []
        for row in reader:
            _ctry = dict(row).get("Country/Region")
            if _ctry not in res[_item]:
                res[_item].append(_ctry)
    return res


def show_available_province(instance):
    """
    Show all the available provinces/state
    :param instance: class instance
    :return: dict
    """
    res = dict()

    for _item in instance._actions_files.keys():
        reader = getattr(instance, _item)
        res[_item] = []
        for row in reader:
            province = dict(row).get("Province/State")
            if province and (province not in res[_item]):
                res[_item].append(province)
    return res
