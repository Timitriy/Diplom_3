import allure
import re
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.common.exceptions import TimeoutException, WebDriverException
from selenium.webdriver.common.action_chains import ActionChains
from selenium.common.exceptions import WebDriverException
from time import sleep
from locators import ConstructorLocators
from .base_page import BasePage

# ─── вспомогательные константы / regex ─────────────────────────────────────
ORDER_ID_RE = re.compile(r"^\d{5,}$")     # 5‑6 цифр без «#»

# ─────────────────────────────────────────────────────────────────────────────
HTML5_DND = """
const src = arguments[0], tgt = arguments[1];
const dt  = new DataTransfer();
src.dispatchEvent(new DragEvent('dragstart', {dataTransfer: dt}));
tgt.dispatchEvent(new DragEvent('dragenter', {dataTransfer: dt}));
tgt.dispatchEvent(new DragEvent('dragover',  {dataTransfer: dt}));
tgt.dispatchEvent(new DragEvent('drop',      {dataTransfer: dt}));
src.dispatchEvent(new DragEvent('dragend',   {dataTransfer: dt}));
"""
# ─────────────────────────────────────────────────────────────────────────────

POINTER_DND = """
const src = arguments[0], tgt = arguments[1];
function fire(type, el) {
  el.dispatchEvent(new PointerEvent(type, {bubbles:true, pointerId:1}));
}
fire('pointerdown', src);
fire('pointerenter', tgt);
fire('pointerover',  tgt);
fire('pointermove',  tgt);
fire('pointerup',    tgt);
"""
# ─────────────────────────────────────────────────────────────────────────────

class ConstructorPage(BasePage):
    path = "/"

    @allure.step("Кликнуть ингредиент «Флюоресцентная булка R2-D3»")
    def open_ingredient_modal(self):
        try:
            WebDriverWait(self.driver, 2).until(
                EC.invisibility_of_element_located(
                    (By.CSS_SELECTOR, "div.Modal_modal_overlay__x2ZCr")
                )
            )
        except TimeoutException:
            pass

        self.driver.execute_script(
            "arguments[0].scrollIntoView({block:'center'});",
            self.element(ConstructorLocators.INGREDIENT_CARD),
        )
        self.click(ConstructorLocators.INGREDIENT_CARD)
        WebDriverWait(self.driver, 5).until(
            EC.visibility_of_element_located(ConstructorLocators.MODAL_TITLE)
        )

    @allure.step("Проверить, что модалка с деталями открыта")
    def assert_modal_opened(self):
        assert self.element(ConstructorLocators.MODAL_TITLE), "Модалка не открылась"

    @allure.step("Закрыть модальное окно крестиком")
    def close_modal(self):
        self.click(ConstructorLocators.MODAL_CLOSE_BTN)
        WebDriverWait(self.driver, 5).until(
            EC.invisibility_of_element_located(ConstructorLocators.MODAL_TITLE)
        )

    @allure.step("Перетащить булку в конструктор")
    def drag_bun_to_constructor(self):
        src = self.element(ConstructorLocators.INGREDIENT_CARD)
        tgt = self.element(ConstructorLocators.CONSTRUCTOR_DROP_ZONE)

        for el in (src, tgt):
            self.driver.execute_script(
                "arguments[0].scrollIntoView({block:'center'});", el
                )

        before = self.get_total_price()

        try:
            box = tgt.rect
            center_x = box["width"]  // 2
            center_y = box["height"] // 2 

            ActionChains(self.driver)\
                .move_to_element(src)\
                .click_and_hold()\
                .move_to_element_with_offset(tgt, center_x, center_y)\
                .pause(0.25)\
                .release()\
                .perform()
        except WebDriverException:
            pass

        if self.get_total_price() == before:
            self.driver.execute_script(HTML5_DND, src, tgt)

        if self.get_total_price() == before:
            self.driver.execute_script(POINTER_DND, src, tgt)

    @allure.step("Получить значение счётчика булки")
    def get_bun_counter(self) -> int:
        try:
            counter = self.element(ConstructorLocators.INGREDIENT_COUNTER)
            return int(counter.text)
        except Exception:
            return 0  # счётчика нет → 0

    def get_total_price(self) -> int:
        return int(self.element(ConstructorLocators.BASKET_TOTAL).text)
    
    @allure.step("Нажать кнопку «Оформить заказ»")
    def place_order(self) -> None:
        self.click(ConstructorLocators.ORDER_BUTTON)

    @allure.step("Убедиться, что открылось модальное окно с номером заказа")
    def assert_order_modal_opened(self) -> None:
        WebDriverWait(self.driver, 15).until(
            EC.visibility_of_element_located(ConstructorLocators.ORDER_MODAL_ID)
        )

    @allure.step("Получить номер заказа из модального окна")
    def get_order_id_from_modal(self) -> str:
        elem = WebDriverWait(self.driver, 30).until(
            EC.visibility_of_element_located(ConstructorLocators.ORDER_ID)
        )
        # ждём, пока в тексте появятся _только_ цифры
        WebDriverWait(self.driver, 30).until(
            lambda _: ORDER_ID_RE.match(elem.text.lstrip("#"))
        )
        return elem.text.lstrip("#")      

    @allure.step("Закрыть модальное окно заказа")
    def close_order_modal(self):
        self.click(ConstructorLocators.MODAL_CLOSE_BTN)
        WebDriverWait(self.driver, 5).until(
            EC.invisibility_of_element_located(ConstructorLocators.ORDER_ID)
        )
