import requests
import allure

from api_test_project_sedelnikov.endpoints.endpoint import Endpoint


class DeleteObject(Endpoint):

    @allure.step('Удаление товара')
    def delete_item(self, item_id, headers=None):
        headers = headers if headers else self.headers
        self.response = requests.delete(
            f'{self.url}/{item_id}',
            headers=headers
        )
        self.json = self.response.json()
        return self.response
