from locust import task, HttpUser


class MemeUser(HttpUser):
    id_object = None

    def on_start(self):
        response = self.client.post('/objects', json={"name": "acer", "year": 2020, "price": 1000, "cpu_model": "i7",
                                                      "hard_disk_size": 500})
        self.id_object = response.json()['id']

    @task(1)
    def create_object(self):
        self.client.post('/objects',
                         json={"name": "acer", "year": 2020, "price": 1000, "cpu_model": "i7", "hard_disk_size": 500})

    @task(2)
    def update_object(self):
        self.client.put(f'/objects/{self.id_object}',
                        json={"name": "acer", "year": 2520, "price": 1500, "cpu_model": "i7", "hard_disk_size": 550})

    @task(3)
    def delete_object(self):
        self.client.delete(f'/objects/{self.id_object}')
