import allure
from pages import Header, LoginPage, ConstructorPage

@allure.title("Клик по ингредиенту открывает модальное окно с деталями")
def test_ingredient_modal(browser, base_url, test_user):
    # 1. авторизация
    browser.get(base_url + "/")
    Header(browser, base_url).go_to_personal_account()
    LoginPage(browser, base_url).login(test_user["email"], test_user["password"])

    # 2. На главной (конструктор) кликаем ингредиент
    constructor = ConstructorPage(browser, base_url)
    constructor.open_ingredient_modal()

    # 3. Проверяем, что модалка действительно открылась
    constructor.assert_modal_opened()
