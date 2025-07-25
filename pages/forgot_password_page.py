import allure
from locators import ForgotPasswordLocators
from .base_page import BasePage

class ForgotPasswordPage(BasePage):
    path = "/forgot-password"

    @allure.step("Убедиться, что открыта страница восстановления пароля")
    def assert_on_page(self):
        self.element(ForgotPasswordLocators.HEADING)
        self.assert_url()

    @allure.step("Ввести e‑mail {email} и нажать «Восстановить»")
    def restore_password(self, email: str):
        self.type(ForgotPasswordLocators.EMAIL_INPUT, email)
        self.click(ForgotPasswordLocators.RESTORE_BTN)
        
        self.wait_url_contains("/reset-password")
