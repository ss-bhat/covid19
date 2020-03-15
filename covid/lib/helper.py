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
