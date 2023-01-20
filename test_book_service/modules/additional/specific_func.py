import uuid
from faker import Faker


def json_param_value_changing(json_body: dict, json_param: str, json_value: str):
    """Function for json value update

    :param json_body: full json body
    :param json_param: json parameter that will be changed
    :param json_value: json value on which it will be changed
    :return: json
    """
    json_body[json_param] = json_value
    return json_body


def url_param_generation(param_name: str, param_value: str or int, parameters_dict: dict = None):
    """Request parameter generation function

    :param param_name: parameter name that will be applied
    :param param_value: param value which will be added to param_name
    :param parameters_dict: If you have some generated dict with parameters in format{"...":"...",...}
    :return: json
    """
    if parameters_dict is None:
        parameters_dict = {}
    parameters_dict[param_name] = param_value

    return parameters_dict


def uuid4() -> uuid:
    """UUID generator
    :return: uuid4
    """
    return uuid.uuid4()


def fake_data() -> str:
    """Reurned random generated data from today + 30 years"""
    faked_data = Faker().date_between(start_date='today', end_date='+30y')
    return str(faked_data)
