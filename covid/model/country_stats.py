from covid.model import country as country_model
from covid.lib import helper as h, errors
from dateutil.parser import parse
from functools import lru_cache


@lru_cache(maxsize=30)
def get_total_stats(instance):
    """
    This method  returns the total deaths across all countries and also returns total deaths per country.
    :param instance: instance of the class
    :return dict
    """
    stats = dict()
    current_records = country_model.get_all_records_by_country(instance)
    for _country_id in current_records:
        for _action in instance._actions_files:
            stats[_action] = stats.get(_action, 0) + current_records[_country_id][_action]
            
    return stats


def _update_history(row, result, _country_id, _action, _previous_value):
    """
    Updates the history if the country id already exists in the result dictionary
    :param row: csv DictWriter OrderdDict
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


@lru_cache(maxsize=10)
def get_history_by_country(instance, country):
    """
    History of all the available cases for the given data.
    If no change can be calculated value = 'na' is assigned
    :param instance: instance of the class
    :param country: str
    :return: dict
    """
    _country_id = h.convert_label_to_id(country)
    result = dict()
    for _action in instance._actions_files:
        reader = getattr(instance, _action)
        for row in reader:
            _country = h.convert_label_to_id(row.get('Country/Region'))
            # if given country
            if _country_id == _country:
                # If country exists in dict
                if _country_id in result:
                    _previous_value = ''
                    # Update the existing dict and calculate change in value
                    result = _update_history(row, result, _country_id, _action, _previous_value)
                else:
                    # Only executed for the action = confirmed (for the first time)
                    # new data
                    result[_country_id] = dict()
                    result[_country_id]['label'] = row.get('Country/Region')
                    result[_country_id]['lat'] = row.get('Lat')
                    result[_country_id]['long'] = row.get('Long')
                    result[_country_id]['history'] = dict()
                    _previous_value = ''

                    for key in row:
                        try:
                            _item = str(parse(key))
                            _current_value = row.get(key)
                            _history = result[_country_id]['history']
                            _history[_item] = dict()
                            _history[_item][_action] = int(_current_value)
                            # Calculate the change in value
                            _history[_item]["change_{}".format(_action)] = h.calculate_change(
                                _current_value, _previous_value)

                            # Assign previous value to current to calculate the next change
                            _previous_value = _current_value
                        except Exception as e:
                            print(e)
    if result:
        return result
    else:
        raise errors.CountryNotFound("Given country not found")
