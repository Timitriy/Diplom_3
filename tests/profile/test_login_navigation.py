import allure

from pages.base_page import BasePage
from pages import Header, LoginPage, ProfilePage


@allure.title("Авторизация в профиле валидным тестовым юзером")
def test_login_success(browser, base_url, test_user):
    page = BasePage(browser, base_url)
    page.open()                                          # главная

    Header(browser, base_url).go_to_personal_account()
    LoginPage(browser, base_url).login(
        test_user["email"], test_user["password"]
    )

    page.wait_url_not_contains("/login")
    assert (
        page.get_url() == base_url.rstrip("/")
    ), "Не вернулись на главную после логина"


@allure.title("Авторизация и выход из аккаунта")
def test_logout(browser, base_url, test_user):
    page = BasePage(browser, base_url)
    page.open()

    # 1. Авторизация
    Header(browser, base_url).go_to_personal_account()
    LoginPage(browser, base_url).login(
        test_user["email"], test_user["password"]
    )
    page.wait_url_not_contains("/login")

    # 2. Переход в профиль 
    Header(browser, base_url).go_to_personal_account()
    page.wait_url_contains("/account/profile")

    # 3. Выход 
    ProfilePage(browser, base_url).logout()

    # 4. Проверяем, что открыта форма входа
    assert "/login" in page.get_url(), "Не попали на форму входа после выхода"


@allure.title("Авторизация и переход во вкладку «История заказов»")
def test_open_order_history(browser, base_url, test_user):
    page = BasePage(browser, base_url)
    page.open()

    # 1. Авторизация 
    Header(browser, base_url).go_to_personal_account()
    LoginPage(browser, base_url).login(
        test_user["email"], test_user["password"]
    )
    page.wait_url_not_contains("/login")

    # 2. Профиль 
    Header(browser, base_url).go_to_personal_account()
    page.wait_url_contains("/account/profile")

    # 3. «История заказов»
    ProfilePage(browser, base_url).go_to_order_history()
    page.wait_url_contains("/account/order-history")

    assert "/account/order-history" in page.get_url(), (
        "Не открылась вкладка «История заказов»"
    )
