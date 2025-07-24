import time
import pytest
import allure
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from pages import Header, LoginPage, ConstructorPage, FeedPage

@pytest.mark.order
@allure.title('Новый заказ появляется в списке «В работе»')
def test_order_appears_in_work(browser, base_url, test_user):
    # 1. авторизация
    browser.get(base_url + "/")
    Header(browser, base_url).go_to_personal_account()
    LoginPage(browser, base_url).login(test_user["email"], test_user["password"])
    WebDriverWait(browser, 10).until_not(EC.url_contains("/login"))

    # 2‑4. создаём заказ и берём его id
    constructor = ConstructorPage(browser, base_url)
    constructor.drag_bun_to_constructor()
    constructor.place_order()
    order_id = constructor.get_order_id_from_modal()
    constructor.close_order_modal()

    # 5‑6. переходим в «Ленту заказов»
    Header(browser, base_url).go_to_feed()
    feed = FeedPage(browser, base_url)

    # 7. даём бекенду время обработать заказ (достаточно 10 секунд)
    time.sleep(10)

    # 8. проверяем, что номер есть в блоке «В работе»
    in_work = feed.get_in_work_numbers()
    assert order_id in in_work, f"Заказ {order_id} не найден в разделе «В работе»"
