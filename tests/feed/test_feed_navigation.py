import allure
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from pages import Header, LoginPage

@allure.title("Авторизация и переход по клику «Лента заказов»")
def test_open_feed_from_header(browser, base_url, test_user):
    # 1. Главная → логин
    browser.get(base_url + "/")
    Header(browser, base_url).go_to_personal_account()
    LoginPage(browser, base_url).login(test_user["email"], test_user["password"])
    WebDriverWait(browser, 10).until_not(EC.url_contains("/login"))

    # 2. Кликаем «Лента заказов» в шапке
    Header(browser, base_url).go_to_feed()

    # 3. Проверяем, что перешли на /feed
    assert "/feed" in browser.current_url, "Не открылась «Лента заказов»"
