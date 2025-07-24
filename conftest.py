import os
import pytest

from utils.driver_factory import DriverFactory
from config import BASE_URL
from utils.api_client import ApiClient

# ───────────────────────────────
# Опции командной строки PyTest
# ───────────────────────────────

def pytest_addoption(parser):
    parser.addoption(
        "--browser", action="store", default=os.getenv("BROWSER", "chrome"),
        help="Браузер: chrome или firefox",
    )
    parser.addoption(
        "--headless", action="store_true", default=False,
        help="Запуск без интерфейса браузера",
    )
    parser.addoption(
        "--base-url", action="store", default=os.getenv("BASE_URL", BASE_URL),
        help="Базовый URL тестируемого стенда",
    )


# ───────────────────────────────
# Фикстуры
# ───────────────────────────────

@pytest.fixture(scope="session")
def base_url(request):
    """Возвращает базовый URL стенда для всех тестов."""
    return request.config.getoption("--base-url")


@pytest.fixture
def browser(request):
    browser_name = request.config.getoption("--browser")
    headless = request.config.getoption("--headless")

    driver = DriverFactory.create(browser_name=browser_name, headless=headless)
    yield driver
    driver.quit()

@pytest.fixture
def test_user():
    client = ApiClient()
    creds = client.register_user(password="12345678")
    yield creds          # передаём словарь {email, password}
    client.delete_user() # удаляем в конце