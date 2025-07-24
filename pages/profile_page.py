import allure
from locators import ProfileLocators
from .base_page import BasePage

class ProfilePage(BasePage):
    path = "/account/profile"

    @allure.step("Перейти во вкладку «История заказов»")
    def go_to_order_history(self):
        self.click(ProfileLocators.ORDER_HISTORY_LINK)
    
    @allure.step("Нажать кнопку «Выход»")
    def logout(self):
        self.click(ProfileLocators.LOGOUT_BUTTON)
