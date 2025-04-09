from playwright.sync_api import sync_playwright

class APIClient:
    def __init__(self):
        self.playwright = sync_playwright().start()
        self.request = self.playwright.request.new_context()
        self.base_url = "https://jsonplaceholder.typicode.com"  # Replace with your API base URL

    def get(self, endpoint):
        return self.request.get(f"{self.base_url}{endpoint}")

    def post(self, endpoint, data):
        return self.request.post(f"{self.base_url}{endpoint}", data=data)

    def close(self):
        self.playwright.stop()
