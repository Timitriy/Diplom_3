import allure
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC
from locators import HeaderLocators
from ..base_page import BasePage
from locators import FeedLocators


class Header(BasePage):
    OVERLAY = (By.CSS_SELECTOR, "div.Modal_modal_overlay__x2ZCr")

    @allure.step("Кликнуть «Личный Кабинет» в шапке")
    def go_to_personal_account(self):
        # ждём, когда оверлей станет невидим (или исчезнет из DOM)
        self.wait.until(EC.invisibility_of_element_located(self.OVERLAY))
        self.click(HeaderLocators.PERSONAL_ACCOUNT)
    
    @allure.step("Кликнуть «Конструктор» в шапке")
    def go_to_constructor(self):
        self.click(HeaderLocators.CONSTRUCTOR_LINK)

    @allure.step("Кликнуть «Лента заказов» в шапке")
    def go_to_feed(self):
        self.click(HeaderLocators.FEED_LINK)

    @allure.step("Переход «Лента заказов»")
    def go_to_order_feed(self):
        self.click(FeedLocators.FEED_LINK)
    
    @allure.step("Перейти в «Историю заказов» из личного кабинета")
    def go_to_order_history(self):
        self.click(HeaderLocators.ORDER_HISTORY_LINK)


    

