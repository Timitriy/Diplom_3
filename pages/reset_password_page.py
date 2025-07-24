# pages/reset_password_page.py
import allure
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

from .base_page import BasePage            
from locators import ResetPasswordLocators

class ResetPasswordPage(BasePage):
    """Страница ввода нового пароля (/reset-password)."""
    path = "/reset-password"

    # ───────────── действия ─────────────
    @allure.step("Кликнуть иконку «глаз» у поля пароля")
    def click_eye_icon(self):
        self.click(ResetPasswordLocators.TOGGLE_PASSWORD_VISIBILITY)

    @allure.step("Ввести новый пароль: {password}")
    def enter_password(self, password: str):
        """Вводит пароль в активное (открытое) поле."""
        self.type(ResetPasswordLocators.PASSWORD_INPUT, password)

    # ───────────── проверки ─────────────
    @allure.step("Проверить, что поле пароля активно (в фокусе)")
    def assert_password_field_focused(self):
        """Оставляем прежнюю проверку — её могут звать другие тесты."""
        input_elem = self.element(ResetPasswordLocators.PASSWORD_INPUT)
        is_focused = self.driver.execute_script(
            "return document.activeElement === arguments[0];", input_elem
        )
        assert is_focused, "Поле пароля не стало активным после клика на «глаз»"

    def get_password_value(self) -> str:
        """Возвращает текущее значение поля (удобно для ассертов)."""
        return self.element(ResetPasswordLocators.PASSWORD_INPUT).get_attribute("value")