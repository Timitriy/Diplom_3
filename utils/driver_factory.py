from selenium import webdriver
from selenium.webdriver.chrome.options import Options as ChromeOptions
from selenium.webdriver.chrome.service import Service as ChromeService
from selenium.webdriver.firefox.options import Options as FirefoxOptions
from selenium.webdriver.firefox.service import Service as FirefoxService

from webdriver_manager.chrome import ChromeDriverManager
from webdriver_manager.firefox import GeckoDriverManager


def _chrome_options(headless: bool = False) -> ChromeOptions:
    opts = ChromeOptions()
    opts.add_argument("--window-size=1920,1080")
    if headless:
        opts.add_argument("--headless=new")
        opts.add_argument("--disable-gpu")
    return opts


def _firefox_options(headless: bool = False) -> FirefoxOptions:
    opts = FirefoxOptions()
    if headless:
        opts.add_argument("-headless")
    return opts


class DriverFactory:
    """Фабрика веб‑драйверов Chrome/Firefox."""

    @staticmethod
    def create(browser_name: str = "chrome", headless: bool = False):
        browser = browser_name.lower()

        if browser == "chrome":
            return webdriver.Chrome(
                service=ChromeService(ChromeDriverManager().install()),
                options=_chrome_options(headless=headless),
            )

        if browser == "firefox":
            return webdriver.Firefox(
                service=FirefoxService(GeckoDriverManager().install()),
                options=_firefox_options(headless=headless),
            )

        raise ValueError(f"Неизвестный браузер: {browser_name}")
