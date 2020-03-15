import json
from covid.model import country


def get_total_stats(instance):
    """This method  returns the total deaths across all countries and also returns total deaths per country"""

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

    print(stats)

    return json.dumps(stats)
