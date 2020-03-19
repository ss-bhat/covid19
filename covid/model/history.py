from covid.lib import helper as h, errors
from dateutil.parser import parse
from functools import lru_cache


def _update_history(row, result, _country_id, _action, _previous_value):
    """
    Updates the history if the country id already exists in the result dictionary
    :param row: csv DictWriter OrderedDict
    :param result: dict
    :param _country_id: str
    :param _action: str
    :param _previous_value: str
    :return: dict
    """
    for key in row:
        try:
            _item = str(parse(key))
            _current_value = row.get(key)
            # If the history (date) already exists update the value and its action.
            if _item in result[_country_id]['history']:
                if _action in result[_country_id]['history'][_item]:
                    result[_country_id]['history'][_item][_action] += int(row.get(key))
                else:
                    result[_country_id]['history'][_item][_action] = int(row.get(key))
            else:
                # This should not occur
                # Only this occurs when the length/rows are of unequal sizes
                result[_country_id]['history'][_item] = dict()
                result[_country_id]['history'][_item][_action] = int(row.get(key))

            result[_country_id]['history'][_item]["change_{}".format(_action)] = h.calculate_change(
                _current_value, _previous_value
            )

            # Assign previous value to current to calculate the next change
            _previous_value = _current_value
        except Exception as e:
            pass

    return result


def _get_history_data(instance, country_province, column_label):
    """
    History of all the available cases for the given data.
    If no change can be calculated value = 'na' is assigned
    :param instance: instance of the class
    :param country_province: str
    :param column_label: str
    :return: dict
    """
    _country_province_id = h.convert_label_to_id(country_province)
    result = dict()

    for _action in instance._actions_files:
        reader = instance.get_reader(_action)
        for row in reader:
            _country = h.convert_label_to_id(row.get(column_label))
            # if given country
            if _country_province_id == _country:
                # If country exists in dict
                if _country_province_id in result:
                    _previous_value = ''
                    # Update the existing dict and calculate change in value
                    result = _update_history(row, result, _country_province_id, _action, _previous_value)
                else:
                    # Only executed for the action = confirmed (for the first time)
                    # new data
                    result[_country_province_id] = dict()
                    result[_country_province_id]['label'] = row.get(column_label)
                    result[_country_province_id]['lat'] = row.get('Lat')
                    result[_country_province_id]['long'] = row.get('Long')
                    result[_country_province_id]['history'] = dict()
                    _previous_value = ''

                    for key in row:
                        try:
                            _item = str(parse(key))
                            _current_value = row.get(key)
                            _history = result[_country_province_id]['history']
                            _history[_item] = dict()
                            _history[_item][_action] = int(_current_value)
                            # Calculate the change in value
                            _history[_item]["change_{}".format(_action)] = h.calculate_change(
                                _current_value, _previous_value)

                            # Assign previous value to current to calculate the next change
                            _previous_value = _current_value
                        except Exception as e:
                            pass
    if result:
        return result
    else:
        raise errors.CountryNotFound("Given {} not found".format(column_label))


@lru_cache(maxsize=30)
def get_history_by_country(instance, country):
    """
    Get all the history data for the given country
    :param instance: class instance
    :param country: str
    :return: dict
    """
    _label = 'Country/Region'
    res = _get_history_data(instance, country, _label)

    return res


@lru_cache(maxsize=10)
def get_history_by_province(instance, province):
    """
    Get all the history data for the given province
    :param instance: class instance
    :param province: str
    :return: dict
    """
    _label = 'Province/State'
    res = _get_history_data(instance, province, _label)
    return res
