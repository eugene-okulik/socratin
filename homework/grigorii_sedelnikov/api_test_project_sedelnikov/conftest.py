import pytest

from api_test_project_sedelnikov.endpoints.create_object import CreateObject
from api_test_project_sedelnikov.endpoints.delete_object import DeleteObject
from api_test_project_sedelnikov.endpoints.update_object import UpdateObject


@pytest.fixture()
def create_object_endpoint():
    return CreateObject()


@pytest.fixture()
def update_object_endpoint():
    return UpdateObject()


@pytest.fixture()
def delete_object_endpoint():
    return DeleteObject()


@pytest.fixture()
def item_id(create_object_endpoint):
    payload = {"name": "acer swift", "year": 2025, "price": 9000,
               "cpu_model": "i9", "hard_disk_size": 750}
    create_object_endpoint.create_new_item(payload)
    return create_object_endpoint.id_object
