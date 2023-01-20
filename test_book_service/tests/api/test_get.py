import pytest
from test_book_service.resources.test_data import book_types
from test_book_service.modules.book_service.post import post_book_creation_set_up
from test_book_service.modules.book_service.delete import delete_book_tear_down
from test_book_service.modules.book_service.get import get_created_book, get_manipulation_req
from test_book_service.resources.schemas.schema_validation import check_body_values
from test_book_service.resources.configs import (get_info_url, get_latest_url, get_ids_url)
from test_book_service.resources.schemas.get_schemas import get_info_response, get_info_response_neg, \
    get_latest_response, get_ids_response
from test_book_service.resources.schemas.invalid_schemas import get_created_response_neg, get_ids_response_neg


class TestGetMethods:
    def test_get_info_positive(self):
        """
        Tear up:
            create the  book via POST /v1/books/manipulation

        Execute request:
           GET /v1/books/info?.....
        Check:
           1) response status => 200 OK
           2) response structure fields(contract testing)
           3) check get response contain same values as post request

        Tear down:
            delete created book
        """
        post_request = post_book_creation_set_up(json_param=None,
                                                 json_value=None)

        get_request = get_created_book(parameter_name="id",
                                       parameter_value=post_request.json()["id"],
                                       request_url=get_info_url,
                                       success=True,
                                       response_status_code=200,
                                       validation_body_or_schema=get_info_response())

        check_body_values(post_request.json(),
                          get_request.json())

        delete_book_tear_down(book_id=post_request.json()["id"])

    def test_get_info_negative(self):
        """
        Tear up:
            create the  book via POST /v1/books/manipulation

        Execute request:
           GET /v1/books/info?.....
        Check:
           1) response status => 404 Bad Request
           2) body structure and fields

        Tear down:
            delete created book
        """
        post_request = post_book_creation_set_up(json_param=None,
                                                 json_value=None)

        get_created_book(parameter_name="id",
                         parameter_value=post_request.json()["id"] + "10",
                         request_url=get_info_url,
                         success=False,
                         response_status_code=404,
                         validation_body_or_schema=get_info_response_neg())

        delete_book_tear_down(book_id=post_request.json()["id"])

    def test_get_latest_positive(self):
        """
        Tear up:
            create the  book via POST /v1/books/manipulation

        Execute request:
           GET /v1/books/latest?.....
        Check:
           1) response status => 200 OK
           2) response structure fields(contract testing)
           3) check get response contain same values as post request

        Tear down:
            delete created book
        """
        book_quantity = 3
        element = 0
        post_request = []
        while element != book_quantity:
            post_request.append(post_book_creation_set_up(json_param=None,
                                                          json_value=None))
            element += 1

        get_created_book(parameter_name="limit",
                         parameter_value=book_quantity,
                         request_url=get_latest_url,
                         success=True,
                         response_status_code=200,
                         validation_body_or_schema=get_latest_response(int(book_quantity)))
        for element in post_request:
            delete_book_tear_down(book_id=element.json()["id"])

    def test_get_latest_negative(self):
        """
        Tear up:
            create the  book via POST /v1/books/manipulation

        Execute request:
           GET /v1/books/latest?.....
        Check:
           1) response status => 400 Bad Request
           2) body structure and fields

        Tear down:
            delete created book
        """
        post_request = post_book_creation_set_up(json_param=None,
                                                 json_value=None)

        get_created_book(parameter_name="limit",
                         parameter_value="3-2",
                         request_url=get_latest_url,
                         success=False,
                         response_status_code=400,
                         validation_body_or_schema=get_created_response_neg())

        delete_book_tear_down(book_id=post_request.json()["id"])

    @pytest.mark.parametrize('param_type', book_types)
    def test_get_ids_positive(self, param_type):
        """
        Tear up:
            create the  book via POST /v1/books/manipulation

        Execute request:
           GET /v1/books/ids?.....
        Check:
           1) response status => 200 OK
           2) response structure fields(contract testing)
           3) check get response contain same values as post request

        Tear down:
            delete created book
        """
        post_request = post_book_creation_set_up(json_param="type",
                                                 json_value=param_type)

        get_created_book(parameter_name="book_type",
                         parameter_value=param_type,
                         request_url=get_ids_url,
                         success=True,
                         response_status_code=200,
                         validation_body_or_schema=get_ids_response())

        delete_book_tear_down(book_id=post_request.json()["id"])

    def test_get_ids_negative(self):
        """
        Tear up:
            create the  book via POST /v1/books/manipulation

        Execute request:
           GET /v1/books/ids?.....
        Check:
           1) response status => 400 Bad Request
           2) body structure and fields

        Tear down:
            delete created book
        """
        post_request = post_book_creation_set_up(json_param=None,
                                                 json_value=None)

        get_created_book(parameter_name="book_type",
                         parameter_value=book_types[0] + "negative",
                         request_url=get_ids_url,
                         success=False,
                         response_status_code=400,
                         validation_body_or_schema=get_ids_response_neg())

        delete_book_tear_down(book_id=post_request.json()["id"])

    def test_get_manipulation_positive(self):
        """
        Tear up:
            create the  book via POST /v1/books/manipulation

        Execute request:
           GET /v1/books/manipulation
        Check:
           1) response status => 200 OK
           2) body structure and fields

        Tear down:
            delete created book
        """
        post_request = post_book_creation_set_up(json_param=None,
                                                 json_value=None)

        get_manipulation_req()

        delete_book_tear_down(book_id=post_request.json()["id"])
