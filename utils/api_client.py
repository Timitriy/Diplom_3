import random
import string
import requests
from config import BASE_URL


def _random_email() -> str:
    suffix = "".join(random.choices(string.ascii_lowercase + string.digits, k=6))
    return f"test_{suffix}@ya.ru"


class ApiClient:
    """Примитивный клиент Stellar Burgers API (только register / delete)."""

    def __init__(self):
        self.base = f"{BASE_URL}/api/auth"
        self.session = requests.Session()

    def register_user(self, password: str, name: str = "test") -> dict:
        email = _random_email()
        payload = {"email": email, "password": password, "name": name}
        resp = self.session.post(f"{self.base}/register", json=payload)
        resp.raise_for_status()
        data = resp.json()
        self.access_token = data["accessToken"]
        return {"email": email, "password": password}

    def delete_user(self):
        if hasattr(self, "access_token"):
            self.session.delete(
                f"{self.base}/user",
                headers={"Authorization": self.access_token},
            )
