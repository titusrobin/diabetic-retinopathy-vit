from locust import HttpUser, task, between

class WebsiteUser(HttpUser):
    wait_time = between(1, 5)

    @task
    def load_main_page(self):
        self.client.get("/")

    @task(3)
    def load_predict_page(self):
        # Assuming this is a GET request
        # For POST, you need to include the data and headers
        self.client.get("/predict/<filename>")