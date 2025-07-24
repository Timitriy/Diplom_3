import allure
from pages import Header, LoginPage, ConstructorPage

@allure.title("Модальное окно ингредиента закрывается по крестику")
def test_modal_close_by_cross(browser, base_url, test_user):
    # 1. авторизация
    browser.get(base_url + "/")
    Header(browser, base_url).go_to_personal_account()
    LoginPage(browser, base_url).login(test_user["email"], test_user["password"])

    # 2. открываем модалку ингредиента
    constructor = ConstructorPage(browser, base_url)
    constructor.open_ingredient_modal()
    constructor.assert_modal_opened()

    # 3. жмём крестик и убеждаемся, что окно исчезло
    constructor.close_modal()
