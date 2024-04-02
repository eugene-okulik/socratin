import requests
import allure

from api_test_project_sedelnikov.endpoints.endpoint import Endpoint


class UpdateObject(Endpoint):

    @allure.step('Обновление товара put')
    def make_changes_in_item_put(self, item_id, payload, headers=None):
        headers = headers if headers else self.headers
        self.response = requests.put(
            f'{self.url}/{item_id}',
            json=payload,
            headers=headers
        )
        self.json = self.response.json()
        return self.response

    @allure.step('Обновление товара patch')
    def make_changes_in_item_patch(self, item_id, payload, headers=None):
        headers = headers if headers else self.headers
        self.response = requests.patch(
            f'{self.url}/{item_id}',
            json=payload,
            headers=headers
        )
        self.json = self.response.json()
        return self.response
