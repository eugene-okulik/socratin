import warnings

import pytest
import requests

warnings.filterwarnings("ignore")


@pytest.fixture(autouse=True)
def ignore_warnings():
    with warnings.catch_warnings():
        warnings.simplefilter("ignore")
        yield


@pytest.fixture(scope="session")
def print_start_and_end():
    print("Start testing")
    yield
    print("Testing completed")


@pytest.fixture(scope="function")
def start_print_test():
    print("before test")
    yield
    print("after test")


@pytest.fixture(scope="function")
def create_object_and_delete():
    url = 'https://api.restful-api.dev/objects'
    data = {
        "name": "Test",
        "data": {
            "year": 2000,
            "price": 3429,
            "CPU model": "A3 Max",
            "Hard disk size": "8tb SSD"
        }
    }
    response = requests.post(url, json=data)
    yield response.json().get("id")
    url = f'https://api.restful-api.dev/objects/{response.json().get("id")}'
    requests.delete(url)


@pytest.mark.parametrize("name, year, price, cpu_model, hard_disk_size",
                         [("acer", 2020, 1000, "i5", "8GB"), ("msi", 2020, 2000, "i7", "16GB"),
                          ("asus", 2021, 3000, "i7", "32GB")])
def test_create_object(print_start_and_end, start_print_test, name, year, price, cpu_model, hard_disk_size):
    url = 'https://api.restful-api.dev/objects'
    data = {
        "name": name,
        "data": {
            "year": year,
            "price": price,
            "CPU model": cpu_model,
            "Hard disk size": hard_disk_size
        }
    }
    response = requests.post(url, json=data)
    assert response.status_code == 200
    return response.json().get("id")


def test_update_object(create_object_and_delete, print_start_and_end, start_print_test):
    url = f'https://api.restful-api.dev/objects/{create_object_and_delete}'
    data = {
        "name": "newmac",
        "data": {
            "year": 2009,
            "price": 5000,
            "CPU model": "air m3",
            "Hard disk size": "5tb"
        }
    }
    response = requests.put(url, json=data)
    assert response.status_code == 200


@pytest.mark.medium
def test_patch_objects(create_object_and_delete, print_start_and_end, start_print_test):
    url = f'https://api.restful-api.dev/objects/{create_object_and_delete}'
    data = {
        "name": "newmac_version2",
    }
    response = requests.patch(url, json=data)
    assert response.status_code == 200


@pytest.mark.critical
def test_delete_objects(print_start_and_end, start_print_test):
    id_object = create_object_only("asus", 2021, 3000, "i7", "32GB")
    url = f'https://api.restful-api.dev/objects/{id_object}'
    response = requests.delete(url)
    assert response.status_code == 200


# Вспомогательная функция для создания объекта
def create_object_only(name, year, price, cpu_model, hard_disk_size):
    url = 'https://api.restful-api.dev/objects'
    data = {
        "name": name,
        "data": {
            "year": year,
            "price": price,
            "CPU model": cpu_model,
            "Hard disk size": hard_disk_size
        }
    }
    response = requests.post(url, json=data)
    return response.json().get("id")
