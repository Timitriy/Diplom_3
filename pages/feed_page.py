# pages/feed_page.py
import allure
import re
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from locators import FeedLocators
from .base_page import BasePage


class FeedPage(BasePage):
    """Страница /feed («Лента заказов»)."""
    path = "/feed"

    @allure.step("Открыть модалку первого заказа в ленте")
    def open_first_order_modal(self):
        self.click(FeedLocators.ORDER_CARD)
        WebDriverWait(self.driver, 10).until(
            EC.visibility_of_element_located(FeedLocators.ORDER_MODAL_BOX)
        )

    @allure.step("Закрыть модальное окно заказа")
    def close_modal(self):
        self.click(FeedLocators.MODAL_CLOSE_BTN)
        WebDriverWait(self.driver, 10).until(
            EC.invisibility_of_element_located(FeedLocators.ORDER_MODAL_BOX)
        )

    @allure.step("Проверить, что модалка заказа открылась")
    def assert_modal_opened(self):
        assert self.element(FeedLocators.ORDER_MODAL_BOX), "Модальное окно заказа не открылось"

    allure.step('Получить счётчик «Выполнено за всё время»')
    def get_completed_all_time(self) -> int:
        WebDriverWait(self.driver, 20).until(
            lambda d: len(d.find_elements(*FeedLocators.COMPLETED_NUMBERS)) >= 2
        )
        counters = self.driver.find_elements(*FeedLocators.COMPLETED_NUMBERS)
        elem = counters[0]               
        WebDriverWait(self.driver, 10).until(
            lambda d: re.fullmatch(r"\d+", elem.text or "")
        )
        return int(elem.text)
    
    @allure.step('Получить счётчик «Выполнено за сегодня»')
    def get_completed_today(self) -> int:
        nums = WebDriverWait(self.driver, 20).until(
            lambda d: (els := d.find_elements(*FeedLocators.COMPLETED_NUMBERS)) and len(els) >= 2 and els
        )
        elem = nums[1]                          
        return int(elem.text.replace("\u202f", ""))

    allure.step('Получить список заказов «В работе»')
    def get_in_work_numbers(self) -> list[str]:
        """
        Возвращает номера заказов из правого блока «В работе».
        """
        els = WebDriverWait(self.driver, 20).until(
            lambda d: (items := d.find_elements(*FeedLocators.IN_WORK_NUMBERS)) and items
        )
        return [
            el.text.replace("\u202f", "").lstrip("#0")
            for el in els
        ]