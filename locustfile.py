from locust import HttpUser, task, between

class HelloWorldUser(HttpUser):
    # Robot akan menunggu 1 sampai 5 detik antar permintaan
    wait_time = between(1, 5)

    @task
    def hello(self):
        # Robot melakukan GET ke endpoint /hello
        self.client.get("/hello")