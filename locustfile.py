from locust import HttpUser, between, task


class WebsiteUser(HttpUser):
    wait_time = between(5.0, 9.0)

    @task
    def index(self):
        self.client.get("/")
