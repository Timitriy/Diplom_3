# pages/order_history_page.py
import re
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from .base_page import BasePage
from locators import OrderHistoryLocators   

ORDER_ID_RE = re.compile(r"\d+")  

class OrderHistoryPage(BasePage):

    def get_order_numbers(self) -> list[str]:
        """
        Возвращает список id заказов без «#» и ведущих нулей.
        """
        WebDriverWait(self.driver, 10).until(
            EC.visibility_of_all_elements_located(OrderHistoryLocators.ORDER_IDS)
        )
        ids = []
        for elem in self.driver.find_elements(*OrderHistoryLocators.ORDER_IDS):
            raw = elem.text            
            match = ORDER_ID_RE.search(raw)
            if match:
                ids.append(match.group().lstrip("0"))  
        return ids
