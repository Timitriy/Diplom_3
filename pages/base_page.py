import allure
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.common.exceptions import ElementClickInterceptedException
from config import BASE_URL, DEFAULT_TIMEOUT

class BasePage:
    """Базовый класс для всех Page Object'ов."""

    path = ""  # относительный путь страницы; переопределяется в наследниках

    def __init__(self, driver, base_url: str = None, timeout: int = DEFAULT_TIMEOUT):
        self.driver = driver
        self.base_url = base_url or BASE_URL
        self.wait = WebDriverWait(driver, timeout)

    # --- базовые действия ---
    @allure.step("Открыть страницу: {url}")
    def open(self, url: str = None):
        """Открыть конкретный URL либо self.path от BASE_URL."""
        target = url or (self.base_url + self.path)
        self.driver.get(target)

    @allure.step("Клик по элементу")
    def click(self, locator):
        element = self.wait.until(EC.element_to_be_clickable(locator))
        try:
            element.click()
        except ElementClickInterceptedException:
            # если что‑то перекрывает элемент (оверлей и т.д.) — кликаем через JS
            self.driver.execute_script(
                "arguments[0].scrollIntoView({block:'center'});", element
            )
            self.driver.execute_script("arguments[0].click();", element)

    @allure.step("Ввод текста: {2}")
    def type(self, locator, text: str):
        elem = self.wait.until(EC.visibility_of_element_located(locator))
        elem.clear()
        elem.send_keys(text)

    def element(self, locator):
        return self.wait.until(EC.visibility_of_element_located(locator))

    def elements(self, locator):
        return self.driver.find_elements(*locator)

    def current_url(self):
        return self.driver.current_url.rstrip('/')

    def expected_url(self):
        return (self.base_url + self.path).rstrip('/')

    def assert_url(self):
        assert self.current_url() == self.expected_url(), (
            f"Ожидали URL {self.expected_url()}, получили {self.current_url()}"
        )