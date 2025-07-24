import allure
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from pages import Header, LoginPage, ConstructorPage

@allure.title("Перетаскивание ингредиента увеличивает сумму заказа")
def test_ingredient_total_changed(browser, base_url, test_user):
    # авторизация
    browser.get(base_url + "/")
    Header(browser, base_url).go_to_personal_account()
    LoginPage(browser, base_url).login(test_user["email"], test_user["password"])
    WebDriverWait(browser, 10).until_not(EC.url_contains("/login"))

    constructor = ConstructorPage(browser, base_url)

    # сумма до перетаскивания
    total_before = constructor.get_total_price()
    assert total_before == 0

    # drag‑and‑drop булки
    constructor.drag_bun_to_constructor()

    # ждём, пока сумма изменится
    WebDriverWait(browser, 10).until(
        lambda d: constructor.get_total_price() > total_before
    )
    assert constructor.get_total_price() > 0, "Сумма заказа не изменилась"
