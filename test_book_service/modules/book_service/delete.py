import json
from test_book_service.resources.configs import (delete_url)
from test_book_service.resources.test_data import header
from test_book_service.modules.basic_api.base_api_requsts import (delete_request)
from test_book_service.modules.additional.specific_func import url_param_generation
from types import SimpleNamespace


def delete_book(book_id: str):
    """Send delete book request

    :param book_id: id of the book
    :return: response obj
    """
    formed_param = url_param_generation("id", book_id)
    del_response = delete_request(request_url=delete_url,
                                  header=header,
                                  param=formed_param)

    return del_response


def delete_book_tear_down(book_id: str):  # kept as tear down method may be changed by fixture
    """Send delete book request

    :param book_id: id of the book
    :return: response obj
    """
    return delete_book(book_id)  # if this method will be changed, need to keep base here


class Book:
    def from_json_text(self, response):
        self.book = json.loads(response, object_hook=lambda d: SimpleNamespace(**d))
        return self.book
