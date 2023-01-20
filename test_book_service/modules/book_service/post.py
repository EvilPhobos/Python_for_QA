from test_book_service.resources.configs import (post_url)
from test_book_service.resources.test_data import header, post_json
from test_book_service.modules.basic_api.base_api_requsts import (post_request)
from test_book_service.modules.additional.specific_func import json_param_value_changing
from test_book_service.resources.schemas.schema_validation import check_response
from test_book_service.resources.schemas.post_schemas import post_response, post_response_neg


def post_book_creation(json_param: str, json_value: str, success: bool = True):
    """Verify that book created successful

    :param json_param: parameter that will be changed in json request
    :param json_value: value that will be changed in json request
    :param success: boolean flag to verify success of the response
    :return: response obj
    """
    request_body = json_param_value_changing(json_body=post_json,
                                             json_param=json_param,
                                             json_value=json_value)
    post_resp = post_request(request_url=post_url,
                             request_json=request_body,
                             header=header)

    if success:
        check_response(response=post_resp, status_code=200, schema=post_response())
    if not success:
        check_response(response=post_resp, status_code=400, body=post_response_neg())

    return post_resp


def post_book_creation_set_up(json_param: str = None, json_value: str = None):
    """Verify that book created successful

    :param json_param: parameter that will be changed in json request (if None taken full default json)
    :param json_value: value that will be changed in json request (if None taken full default json)
    :return: response obj
    """
    if json_param and json_value:
        request_body = json_param_value_changing(json_body=post_json,
                                                 json_param=json_param,
                                                 json_value=json_value)
    else:
        request_body = post_json

    post_resp = post_request(request_url=post_url,
                             request_json=request_body,
                             header=header)

    return post_resp
