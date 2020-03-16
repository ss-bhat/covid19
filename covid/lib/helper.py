import logging


def convert_label_to_id(val):
    """
    Convert the given label to id. Change to lower case and remove space
    :param val: str
    :return: str
    """
    try:
        val = val.lower()
        val = "_".join(val.split(" "))

        return val
    except Exception as e:
        logging.debug(e)
        return None


def calculate_change(current_value, previous_value):
    """
    Calculate change in value given current value and previous value. Can be either +ve or -ve
    :param current_value: str
    :param previous_value: str
    :return: int or na
    """
    if not previous_value:
        pass
    else:
        diff = int(current_value) - int(previous_value)
        if int(previous_value):
            return diff / int(previous_value)

    return 'na'
