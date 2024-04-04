import requests
import allure

from api_test_project_sedelnikov.endpoints.endpoint import Endpoint


class CreateObject(Endpoint):
    id_object = None

    @allure.step('Создание нового товара')
    def create_new_item(self, payload, headers=None):
        headers = headers if headers else self.headers
        self.response = requests.post(
            self.url,
            json=payload,
            headers=headers
        )
        self.json = self.response.json()
        self.id_object = self.json['id']
        return self.response

    @allure.step('Проверка имени созданного объекта')
    def check_response_name_is_correct(self, name):
        assert self.json['name'] == name
