import allure
import pytest


TEST_DATA = [
    {"name": "acer", "year": 2020, "price": 1000, "cpu_model": "i7", "hard_disk_size": 500},
    {"name": "msi", "year": 2020, "price": 2000, "cpu_model": "i5", "hard_disk_size": 800},
    {"name": "asus", "year": 2021, "price": 3000, "cpu_model": "i7", "hard_disk_size": 1600}
]


@allure.title("Создание товара методом POST")
@pytest.mark.parametrize("data", TEST_DATA)
@pytest.mark.critical
def test_create_object(create_object_endpoint, data):
    create_object_endpoint.create_new_item(payload=data)
    create_object_endpoint.check_that_status_is_200()
    create_object_endpoint.check_response_name_is_correct(data["name"])


@allure.title('Обновление полей объекта методом PUT')
def test_update_object(item_id, update_object_endpoint):
    payload = {
        "name": "newmac",
        "data": {
            "year": 2009,
            "price": 5000,
            "CPU model": "air m3",
            "Hard disk size": "5tb"
        }
    }
    update_object_endpoint.make_changes_in_item_put(item_id, payload)
    update_object_endpoint.check_that_status_is_200()
    update_object_endpoint.check_that_name_is_correct(payload["name"])


@allure.title('Изменение объекта методом PATCH')
def test_patch_objects(item_id, update_object_endpoint):
    data = {
        "name": "newmac_version2",
    }
    update_object_endpoint.make_changes_in_item_put(item_id, data)
    update_object_endpoint.check_that_status_is_200()
    update_object_endpoint.check_that_name_is_correct(data["name"])


@allure.title('Удаление объекта')
@pytest.mark.critical
def test_delete_objects(item_id, delete_object_endpoint):
    delete_object_endpoint.delete_item(item_id)
    delete_object_endpoint.check_that_status_is_200()
