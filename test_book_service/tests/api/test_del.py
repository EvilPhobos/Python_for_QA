import json
from assertpy import assert_that
from types import SimpleNamespace
from test_book_service.modules.book_service.delete import delete_book, Book
from test_book_service.modules.book_service.get import get_created_book
from test_book_service.resources.schemas.schema_validation import compare_values
from test_book_service.modules.additional.specific_func import uuid4
from test_book_service.resources.schemas.schema_validation import schema_validation, body_validation
from test_book_service.resources.schemas.delete_schemas import delete_response, delete_response_neg
from test_book_service.resources.configs import get_info_url
from test_book_service.resources.schemas.get_schemas import get_info_response_neg


class TestDelMethods:

    def test_del_manipulation_positive(self, add_book):
        """
        Execute request with all available body parameters:
           DELETE /v1/books/manipulation
        Check:
           1) response status => 200 OK
           2) response structure fields(contract testing)

        Check get response contain same values as post request

        Execute request:
           GET /v1/books/info?.....
        Check:
           1) response status => 400 OK
           2) response structure fields(contract testing)
        """
        post_response = add_book

        del_response = delete_book(book_id=post_response.json()["id"])

        assert_that(del_response.status_code).is_equal_to(200)
        schema_validation(del_response.json(), delete_response())  # schema validation

        # convert response body to object
        actual_resp_body = Book().from_json_text(del_response.text)
        print(actual_resp_body.type)
        expected_resp_body = json.loads(post_response.text, object_hook=lambda d: SimpleNamespace(**d))

        # value validation
        assert_that(actual_resp_body.id).is_equal_to(expected_resp_body.id)
        assert_that(actual_resp_body.title).is_equal_to(expected_resp_body.title)
        assert_that(actual_resp_body.type).is_equal_to(expected_resp_body.type)
        assert_that(actual_resp_body.creation_date).is_equal_to(expected_resp_body.creation_date)

        # left for example, future swap by assert_that -----------
        compare_values(actual_resp_body.id, expected_resp_body.id, "id")
        compare_values(actual_resp_body.title, expected_resp_body.title, "title")
        compare_values(actual_resp_body.type, expected_resp_body.type, "type")
        compare_values(actual_resp_body.creation_date, expected_resp_body.creation_date, "creation_date")

        get_created_book(parameter_name="id",
                         parameter_value=expected_resp_body.id,
                         request_url=get_info_url,
                         success=False,
                         response_status_code=404,
                         validation_body_or_schema=get_info_response_neg())

    def test_del_manipulation_negative(self):
        """
        Execute request with wrong type body parameter:
           POST /v1/books/manipulation
        Check:
           1) response status => 404 Bad Request
           2) body structure and fields
        """
        del_response = delete_book(book_id=uuid4())

        assert_that(del_response.status_code).is_equal_to(404)
        body_validation(del_response.json(), delete_response_neg())
