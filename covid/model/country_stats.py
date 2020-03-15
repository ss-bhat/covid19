from covid.model import country
from covid.lib import helper as h, errors
from dateutil.parser import parse
import json

def get_total_stats(instance):
    """
    This method  returns the total deaths across all countries and also returns total deaths per country.
    :param instance: instance of the class
    :return dict
    """

    current_records = country.get_all_records_by_country(instance)
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


def get_history_by_country(instance, country):
    all_history = list()
    f_deaths = getattr(instance, "deaths")
    f_confirmed = getattr(instance, "confirmed")
    f_recovered = getattr(instance, "recovered")
    _country_id = h.convert_label_to_id(country)
    result = dict()
    for _action in instance._actions_files:
        reader = getattr(instance, _action)
        for row in reader:
            _country = h.convert_label_to_id(row.get('Country/Region'))
            if _country_id == _country:
                if _country_id in result:
                    for key in row:
                        try:
                            _item = str(parse(key))
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
                        except Exception as e:
                            pass

                else:
                    result[_country_id] = dict()
                    result[_country_id]['label'] = row.get('Country/Region')
                    result[_country_id]['lat'] = row.get('Lat')
                    result[_country_id]['lat'] = row.get('Long')
                    result[_country_id]['history'] = dict()
                    for key in row:
                        try:
                            _item = str(parse(key))
                            _history = result[_country_id]['history'][_item] = dict()
                            _history[_item] = dict()
                            _history[_item][_action] = int(row.get(key))
                        except Exception as e:
                            pass
                break
    print(result)

    if not result:
        raise errors.CountryNotFound("Given country not found")
    """
    for row1, row2, row3 in zip(f_deaths, f_confirmed, f_recovered):
        print(row1)
        d = dict()
        for item in range(4, len(list(row1.keys()))):
            _key = list(row1.keys())[item]
            _country = h.convert_label_to_id(row1["Country/Region"])
            d["Country"] = _country
            d["Province"] = h.convert_label_to_id(row1["Province/State"]) if row1.get("Province/State") else ""

            d[_key] = {"deaths": int(row1.get(_key)),
                       "confirmed": int(row2.get(_key)),
                       "recovered": int(row3.get(_key))}
            break
        break
        d["lastUpdate"] = list(row1.keys())[-1]
        all_history.append(d)

    return all_history"""