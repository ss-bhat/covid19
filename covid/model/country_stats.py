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

    current_records = country_model.get_all_records_by_country(instance)
    stats = dict()
    deaths = confirmed = recovered = active = 0
    for key in current_records:
        current_stats = current_records.get(key)
        deaths += current_stats.get('deaths')
        confirmed += current_stats.get('confirmed')
        recovered += current_stats.get('recovered')

    active = confirmed - recovered - deaths
    stats["Deaths"] = deaths
    stats["Confirmed"] = confirmed
    stats["Recovered"] = recovered
    stats["Active"] = active

    return stats


"""
# Using zip is faster
 TODO: How to handle uneven length of the data?
 TODO: What if the number of columns is larger?
def get_history_by_country(instance, country):
    all_history = list()
    res = None
    _ct = h.convert_label_to_id(country)
    for row1, row2, row3 in zip(*[getattr(instance, x) for x in instance._actions_files]):
        _ct2 = h.convert_label_to_id(row1["Country/Region"])
        if _ct == _ct2:
            res = dict()
            res['hsitory'] = dict()
            res["label"] = row1["Country/Region"]
            res["Province"] = h.convert_label_to_id(row1["Province/State"]) if row1.get("Province/State") else ""
            for item in range(4, len(list(row1.keys()))):
                _key = list(row1.keys())[item]
                key = str(parse(_key))
                res['history'][key] = {
                    "deaths": int(row1.get(_key)),
                    "confirmed": int(row2.get(_key)),
                    "recovered": int(row3.get(_key))
                }

            res["lastUpdate"] = list(row1.keys())[-1]
            return res

    raise errors.CountryNotFound("Given country not found.")
"""


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
            _previous_value = _current_value
        except Exception as e:
            pass

    return result


@lru_cache(maxsize=10)
def get_history_by_country(instance, country):
    """
    History of all the available cases for the given data.
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
            if _country_id == _country:
                if _country_id in result:
                    _previous_value = ''
                    result = _update_history(row, result, _country_id, _action, _previous_value)
                else:
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
                            _history[_item]["change_{}".format(_action)] = h.calculate_change(
                                _current_value, _previous_value)
                            _previous_value = _current_value
                        except Exception as e:
                            print(e)
    if result:
        return result
    else:
        raise errors.CountryNotFound("Given country not found")
