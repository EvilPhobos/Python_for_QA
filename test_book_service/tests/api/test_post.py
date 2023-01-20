import pytest
from test_book_service.resources.test_data import book_types_neg, param_creation_date_neg, book_types
from test_book_service.modules.book_service.post import post_book_creation
from test_book_service.modules.book_service.delete import delete_book_tear_down
from test_book_service.modules.book_service.get import get_created_book
from test_book_service.resources.configs import get_info_url
from test_book_service.resources.schemas.get_schemas import get_info_response


class TestPostMethods:

    @pytest.mark.parametrize('param_type', book_types)
    def test_post_parameters_positive(self, param_type):
        """
        Execute request with all available body parameters:
           POST /v1/books/manipulation
        Check:
           1) response status => 200 OK
           2) response structure fields(contract testing)

        Execute request:
           GET /v1/books/info?.....
        Check:
           1) response status => 200 OK
           2) response structure fields(contract testing)
           3) Check created book

        Tear down:
            delete created book
        """
        post_request = post_book_creation(json_param="type",
                                          json_value=param_type,
                                          success=True)

        get_created_book(parameter_name="id",
                         parameter_value=post_request.json()["id"],
                         request_url=get_info_url,
                         success=True,
                         response_status_code=200,
                         validation_body_or_schema=get_info_response())

        delete_book_tear_down(book_id=post_request.json()["id"])

    @pytest.mark.parametrize('param_type_neg', book_types_neg)
    def test_post_type_value_negative(self, param_type_neg):
        """
        Execute request with wrong type body parameter:
           POST /v1/books/manipulation
        Check:
           1) response status => 404 Bad Request
           2) body structure and fields
        """
        post_book_creation(json_param="type",
                           json_value=param_type_neg,
                           success=False)

    def test_post_creation_date_value_negative(self):
        """
        Execute request with wrong creation_date body parameter:
           POST /v1/books/manipulation
        Check:
           1) response status => 404 Bad Request
           2) body structure and fields
        """
        post_book_creation(json_param="creation_date",
                           json_value=param_creation_date_neg,
                           success=False)
