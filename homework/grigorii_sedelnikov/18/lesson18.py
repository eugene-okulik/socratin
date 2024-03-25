import requests


def test_create_object():
    url = 'https://api.restful-api.dev/objects'
    data = {
        "name": "mac",
        "data": {
            "year": 2004,
            "price": 4000,
            "CPU model": 'core 11',
            "Hard disk size": '4tb'
        }
    }
    response = requests.post(url, json=data)
    assert response.status_code == 200
    print(response.json())
    return response.json().get("id")


def test_update_object():
    url = 'https://api.restful-api.dev/objects/ff8081818e21ce2d018e76087ef15db1'
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


def test_patch_objects():
    url = 'https://api.restful-api.dev/objects/ff8081818e21ce2d018e76087ef15db1'
    data = {
        "name": "newmac_version2",
    }
    response = requests.patch(url, json=data)
    assert response.status_code == 200


def test_delete_objects():
    url = 'https://api.restful-api.dev/objects/ff8081818e21ce2d018e76087ef15db1'
    response = requests.delete(url)
    assert response.status_code == 200
