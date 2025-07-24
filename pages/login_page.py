# pages/login_page.py
import allure
from locators import LoginLocators
from .base_page import BasePage


class LoginPage(BasePage):
    """Страница входа в аккаунт (/login)."""
    path = "/login"

    @allure.step("Кликнуть ссылку «Восстановить пароль» на форме входа")
    def go_to_forgot_password(self):
        self.click(LoginLocators.FORGOT_PASSWORD_LINK)

    @allure.step("Ввести логин и пароль, нажать «Войти»")
    def login(self, email: str, password: str):
        self.type(LoginLocators.EMAIL_INPUT, email)
        self.type(LoginLocators.PASSWORD_INPUT, password)
        self.click(LoginLocators.SUBMIT_BUTTON)
