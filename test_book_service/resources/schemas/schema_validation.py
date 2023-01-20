from jsonschema import validate, ValidationError
from requests import Response


def schema_validation(json_body: dict, schema: dict):
    """Schema validation method
    :param json_body: actual json
    :param schema: expected json
    """
    try:
        validate(json_body, schema)
    except ValidationError as e:
        raise AssertionError(e)


def body_validation(actual_response_body: dict, expected_body: dict):
    """Body validation method
    :param actual_response_body: actual body
    :param expected_body: expected body
    """
    assert actual_response_body == expected_body, f'Response body is invalid:\n' \
                                                  f'Actual: {actual_response_body}\n' \
                                                  f'Expected: {expected_body}'


def check_response(response: Response, status_code: int, schema: dict = None, body: dict = None) -> None:
    """"Check response:
    1) Check status code
    2) Optional verification: scheme or body  - can be specified
        :param response: object, which contains a server's response to an HTTP request.
        :param status_code: Response status code
        :param schema: scheme for contract testing
        :param body: full body structure
        """
    act_status_code = response.status_code
    assert act_status_code == status_code, f'Invalid status code:\n' \
                                           f'Actual: {act_status_code}\n' \
                                           f'Expected: {status_code}'

    if schema:
        schema_validation(response.json(), schema)

    if body:
        body_validation(response.json(), body)


def check_body_values(expected_body: dict, actual_body: dict):
    """"Compare body:
        :param expected_body: Expected body
        :param actual_body: Actual response, which need to check

    """
    for el in expected_body:
        assert el in actual_body, f'Response body doesn\'t contain value :\n' \
                                  f'Actual: {actual_body}\n' \
                                  f'Expected: {el}'
        assert expected_body[el] == actual_body[el], f'Response body is value:\n' \
                                                     f'Actual: {actual_body[el]}\n' \
                                                     f'Expected: {expected_body[el]}'


def compare_values(actual_value: str, expected_value: str or int, param_key: str):
    """ Compare values

    :param actual_value: Actual value
    :param expected_value: Expected value
    :param param_key: Key which is being comparing
    """
    assert actual_value == expected_value, f"Response body value `{param_key}`doesn't match:\n" \
                                           f'Actual: {actual_value}\n' \
                                           f'Expected: {expected_value}'



def check_specific_values(param_to_check: str, body_before_upd: dict, body_after_upd: dict, value_conformity: bool = True):
    """"Compare specific values:

        :param param_to_check: parameter which need to find and check for correctness
        :param body_before_upd: Response body before update
        :param body_after_upd: Response body after update
        :param value_conformity: does the value match or not
    """
    if value_conformity:
        assert body_before_upd[param_to_check] == body_after_upd[param_to_check], f'Values does not match:\n' \
                                                                                  f'Actual: {body_after_upd[param_to_check]}\n' \
                                                                                  f'Expected: {body_before_upd[param_to_check]}'
    else:
        assert body_before_upd[param_to_check] != body_after_upd[param_to_check], f'Values does not match:\n' \
                                                                                  f'Actual: {body_after_upd[param_to_check]}\n' \
                                                                                  f'Expected: != {body_before_upd[param_to_check]}'


def check_list_specific_values(params_list: list, body_before_upd: dict, body_after_upd: dict, value_conformity: bool = True):
    """"Compare specific values:

        :param params_list: parameters which need to find and check for correctness
        :param body_before_upd: Response body before update
        :param body_after_upd: Response body after update
        :param value_conformity: does the value match or not
    """

    for el in params_list:
        check_specific_values(param_to_check=el,
                              body_before_upd=body_before_upd,
                              body_after_upd=body_after_upd,
                              value_conformity=value_conformity)
