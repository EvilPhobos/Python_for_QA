from test_book_service.resources.configs import (put_url)
from test_book_service.resources.test_data import header, post_json
from test_book_service.modules.basic_api.base_api_requsts import put_request
from test_book_service.modules.additional.specific_func import json_param_value_changing
from test_book_service.resources.schemas.schema_validation import check_response
from test_book_service.resources.schemas.put_schemas import put_response, put_response_neg
from test_book_service.modules.additional.specific_func import url_param_generation


def put_book_manipulation(book_id: str, json_param: str, json_value: str, success: bool = True):
    """Verify that book created successful

    :param book_id: id of the book
    :param json_param: parameter that will be changed in json request
    :param json_value: value that will be changed in json request
    :param success: boolean flag to verify success of the response
    :return: response obj
    """
    request_body = json_param_value_changing(json_body=post_json,
                                             json_param=json_param,
                                             json_value=json_value)
    formed_param = url_param_generation("id", book_id)

    put_resp = put_request(request_url=put_url,
                           request_json=request_body,
                           header=header,
                           param=formed_param)

    if success:
        check_response(response=put_resp, status_code=200, schema=put_response())
    if not success:
        check_response(response=put_resp, status_code=400, body=put_response_neg())

    return put_resp
