import os
from dotenv import load_dotenv
from httpx import Client

class ApiClient(Client):
    def __init__(self):
        super().__init__(base_url=f'{os.getenv("BASE_URL")}/api/v3')