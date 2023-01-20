import allure


@allure.step("Action: create key to avoid [specified] web element")
def list_exclude_xpath_creation(main_path_part, attr_name, list_values) -> str:
    """Add's to [initial part] + [not(@key = "value" or ...)]

    :param main_path_part: initial part to which need to add
    :param attr_name: "key" name
    :param list_values: value list
    :return: upgraded key
    """
    constructed = ""
    for el, value in enumerate(list_values):
        if el == 0:
            constructed += '@' + attr_name + ' = "' + str(value) + '"'
        else:
            constructed += ' or @' + attr_name + ' = "' + str(value) + '"'
    return str(main_path_part + '[not(' + constructed + ')]')


def tuple_update(position: int, tuple_object: tuple, value: str):
    """ Function to update data with `%s`
    :param position: position in the tuple to change
    :param tuple_object: tuple object
    :param value: value to insert
    """
    list_object = list(tuple_object)
    list_object[position] = list_object[position] % value
    return tuple(list_object)
