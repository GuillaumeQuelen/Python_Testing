from locust import HttpUser, task, between


class SecretaryUser(HttpUser):
    wait_time = between(1, 2)

    def on_start(self):
        self.client.post("/showSummary", data={"email": "john@simplylift.co"})

    @task(3)
    def home(self):
        self.client.get("/")

    @task(3)
    def points_board(self):
        self.client.get("/points")

    @task(2)
    def booking_page(self):
        self.client.get("/book/Winter%20Open/Simply%20Lift")

    @task(1)
    def purchase(self):
        self.client.post("/purchasePlaces", data={
            "competition": "Winter Open",
            "club": "Simply Lift",
            "places": "1",
        })