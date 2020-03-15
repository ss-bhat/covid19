

def get_all_country_data(instance):

    _actions = (
        "confirmed",
        "deaths",
        "recovered"
    )

    for _item in _actions:
        reader = getattr(instance, _item)
        for row in reader:
            k, v = row
            print(k, v)
        break
