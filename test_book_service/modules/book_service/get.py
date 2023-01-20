from test_book_service.resources.configs import get_manipulation_url
from test_book_service.resources.test_data import header
from test_book_service.modules.basic_api.base_api_requsts import (get_request)
from test_book_service.resources.schemas.schema_validation import check_response
from test_book_service.resources.schemas.get_schemas import get_manipulation
from test_book_service.modules.additional.specific_func import url_param_generation


def get_created_book(parameter_name: str, parameter_value: str or int, request_url: str, success: bool = True,
                     response_status_code: int = 200, validation_body_or_schema: dict = None):
    """Verify that book created successful

    :param parameter_name: request parameter name
    :param parameter_value: id of the book
    :param request_url: URL path
    :param success: boolean flag to verify success of the response
    :param response_status_code: status code for positive scenario with schema validation
    :param validation_body_or_schema: dict for schema or body validation
    :return: response obj
    """
    formed_param = url_param_generation(parameter_name, parameter_value)
    get_info_resp = get_request(request_url=request_url,
                                param=formed_param,
                                header=header)

    if success:
        check_response(response=get_info_resp, status_code=response_status_code, schema=validation_body_or_schema)
    if not success:
        check_response(response=get_info_resp, status_code=response_status_code, body=validation_body_or_schema)

    return get_info_resp


def get_manipulation_req():
    """Verify that request successful

    :return: response obj
    """
    get_manipulation_resp = get_request(request_url=get_manipulation_url,
                                        header=header)

    check_response(response=get_manipulation_resp, status_code=200, body=get_manipulation())

    return get_manipulation_resp
