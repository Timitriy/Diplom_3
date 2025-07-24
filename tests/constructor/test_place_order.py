import allure
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from pages import Header, LoginPage, ConstructorPage

@allure.title("Залогиненный пользователь может оформить заказ")
def test_place_order(browser, base_url, test_user):
    # 1. авторизация
    browser.get(base_url + "/")
    Header(browser, base_url).go_to_personal_account()
    LoginPage(browser, base_url).login(test_user["email"], test_user["password"])
    WebDriverWait(browser, 10).until_not(EC.url_contains("/login"))

    constructor = ConstructorPage(browser, base_url)

    # 2‑3. перетаскиваем булку и убеждаемся, что сумма > 0
    constructor.drag_bun_to_constructor()
    assert constructor.get_total_price() > 0, "Булка не добавилась — сумма 0"

    # 4. кликаем «Оформить заказ»
    constructor.place_order()

    # 5. ждём модальное окно с номером заказа
    constructor.assert_order_modal_opened()
