import pytest
from test_book_service.modules.book_service.post import post_book_creation_set_up
from test_book_service.modules.book_service.delete import delete_book_tear_down
from test_book_service.modules.book_service.get import get_created_book
from test_book_service.modules.book_service.put import put_book_manipulation
from test_book_service.resources.schemas.schema_validation import check_list_specific_values
from test_book_service.modules.additional.specific_func import uuid4


class TestPutMethods:

    def test_put_manipulation_positive(self):
        """
        Tear up:
            create the  book via POST /v1/books/manipulation

        Execute request:
           PUT /v1/books/manipulation?...
        Check:
           1) response status => 200 OK
           2) response structure fields(contract testing)
           3) check get response contain same values as post request

        Tear down:
            delete created book
        """
        post_request = post_book_creation_set_up(json_param=None,
                                                 json_value=None)

        get_request = get_created_book(parameter_value=post_request.json()["id"],
                                       success=True)
        put_book_manipulation(book_id=post_request.json()["id"],
                              json_param="title",
                              json_value=str(uuid4())[:8],
                              success=True)

        get_request_2 = get_created_book(parameter_value=post_request.json()["id"],
                                         success=True)

        check_list_specific_values(params_list=["updated_date_time", "title"],
                                   body_before_upd=get_request.json(),
                                   body_after_upd=get_request_2.json(),
                                   value_conformity=False)

        check_list_specific_values(params_list=["creation_date", "type"],
                                   body_before_upd=get_request.json(),
                                   body_after_upd=get_request_2.json(),
                                   value_conformity=True)

        delete_book_tear_down(book_id=post_request.json()["id"])
