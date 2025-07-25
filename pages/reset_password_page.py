import allure

from .base_page import BasePage
from locators import ResetPasswordLocators


class ResetPasswordPage(BasePage):
    """Страница ввода нового пароля (`/reset-password`)."""

    path = "/reset-password"

    # ──────────────── действия ────────────────
    @allure.step("Кликнуть иконку \u00abглаз\u00bb у поля пароля")
    def click_eye_icon(self) -> None:
        """Нажимает SVG‑иконку, раскрывающую пароль.
        Если иконка недоступна, фокусируем поле как запасной вариант.
        """
        try:
            self.click(ResetPasswordLocators.TOGGLE_PASSWORD_VISIBILITY)
        except Exception:
            # резервный сценарий: ставим фокус просто кликом по полю пароля
            self.click(ResetPasswordLocators.PASSWORD_INPUT)

    @allure.step("Ввести новый пароль: {password}")
    def enter_password(self, password: str) -> None:
        """Вводит текст в поле пароля (уже открытое)."""
        self.type(ResetPasswordLocators.PASSWORD_INPUT, password)

    # ──────────────── проверки ────────────────
    @allure.step("Убедиться, что открыта страница /reset-password")
    def assert_on_page(self) -> None:
        """Проверяет, что сейчас отображается страница сброса пароля."""
        self.element(ResetPasswordLocators.PASSWORD_INPUT)
        self.assert_url()

    def get_password_value(self) -> str:
        """Возвращает введённый пароль (значение input)."""
        return self.element(ResetPasswordLocators.PASSWORD_INPUT).get_attribute("value")