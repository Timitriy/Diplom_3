import allure
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

from pages import Header, LoginPage


@allure.title("Авторизация и переход по клику «Конструктор»")
def test_open_constructor_from_header(browser, base_url, test_user):
    # 1. главная → логин
    browser.get(base_url + "/")
    Header(browser, base_url).go_to_personal_account()
    LoginPage(browser, base_url).login(test_user["email"], test_user["password"])
    WebDriverWait(browser, 10).until_not(EC.url_contains("/login"))

    # 2. снова «Личный кабинет» (чтобы быть на /account/profile)
    Header(browser, base_url).go_to_personal_account()
    WebDriverWait(browser, 10).until(EC.url_contains("/account/profile"))

    # 3. кликаем «Конструктор»
    Header(browser, base_url).go_to_constructor()

    # ➜ должны оказаться на главной
    assert browser.current_url.rstrip("/") == base_url, "Не открылась главная / конструктор"
