import pytest
import requests
from test_book_service.resources.configs import (post_url, delete_url)
from test_book_service.resources.test_data import header, post_json


@pytest.fixture
def add_book():
    post_response = requests.post(url=post_url, json=post_json, headers=header)
    return post_response


@pytest.fixture  # in  perspective for get method
def add_and_delete_book():
    post_response = requests.post(url=post_url, json=post_json, headers=header)
    yield post_response
    book_id = {"id": post_response.json()["id"]}
    delete_response = requests.delete(url=delete_url, headers=header, params=book_id)
    if delete_response.status_code != 200:
        assert delete_response.status_code == 200
