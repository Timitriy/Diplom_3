import allure

from pages import Header, LoginPage, ConstructorPage
from pages.base_page import BasePage

@allure.title("Авторизация и переход по клику «Конструктор»")
def test_open_constructor_from_header(browser, base_url, test_user):
    # 1. главная → логин
    page = BasePage(browser, base_url)
    page.open()                                 # главная
    Header(browser, base_url).go_to_personal_account()
    LoginPage(browser, base_url).login(
        test_user["email"], test_user["password"]
    )
    page.wait_url_not_contains("/login")

    # 2. «Личный кабинет»
    Header(browser, base_url).go_to_personal_account()
    page.wait_url_contains("/account/profile")

    # 3. кликаем «Конструктор»
    Header(browser, base_url).go_to_constructor()

    # 4. должны оказаться на главной
    assert page.get_url() == base_url.rstrip(
        "/"
    ), "Не открылась главная / конструктор"


@allure.title("Залогиненный пользователь может оформить заказ")
def test_place_order(browser, base_url, test_user):
    page = BasePage(browser, base_url)

    # 1. Авторизация 
    with allure.step("Авторизация пользователя"):
        page.open()
        Header(browser, base_url).go_to_personal_account()
        LoginPage(browser, base_url).login(
            test_user["email"], test_user["password"]
        )
        page.wait_url_not_contains("/login")

    constructor = ConstructorPage(browser, base_url)

    # 2. Добавление булки 
    with allure.step("Добавляем булку и проверяем изменение суммы"):
        price_before = constructor.get_total_price()
        constructor.drag_bun_to_constructor()
        price_after = constructor.get_total_price()

        assert price_after > price_before, (
            f"Сумма заказа не изменилась (было {price_before}, стало {price_after})"
        )

    # 3. Оформление заказа 
    with allure.step("Оформляем заказ"):
        constructor.place_order()

    # 4. Проверка модального окна 
    with allure.step("Проверяем модальное окно с номером заказа"):
        constructor.assert_order_modal_opened()
        order_number = constructor.get_order_id_from_modal()
        assert order_number.isdigit(), f"Некорректный номер заказа: {order_number}"


@allure.title("Перетаскивание ингредиента увеличивает сумму заказа")
def test_ingredient_total_changed(browser, base_url, test_user):
    page = BasePage(browser, base_url)

    # 1. авторизация
    page.open()
    Header(browser, base_url).go_to_personal_account()
    LoginPage(browser, base_url).login(
        test_user["email"], test_user["password"]
    )
    page.wait_url_not_contains("/login")

    constructor = ConstructorPage(browser, base_url)

    total_before = constructor.get_total_price()
    assert total_before == 0

    constructor.drag_bun_to_constructor()
    constructor.wait_total_price_greater_than(total_before)

    assert (
        constructor.get_total_price() > 0
    ), "Сумма заказа не изменилась"


@allure.title("Клик по ингредиенту открывает модальное окно с деталями")
def test_ingredient_modal(browser, base_url, test_user):
    page = BasePage(browser, base_url)

    # 1. авторизация
    page.open()
    Header(browser, base_url).go_to_personal_account()
    LoginPage(browser, base_url).login(
        test_user["email"], test_user["password"]
    )
    page.wait_url_not_contains("/login")

    # 2. На главной (конструктор) кликаем ингредиент
    constructor = ConstructorPage(browser, base_url)
    constructor.open_ingredient_modal()

    # 3. Проверяем, что модалка действительно открылась
    constructor.assert_modal_opened()


@allure.title("Модальное окно ингредиента закрывается по крестику")
def test_modal_close_by_cross(browser, base_url, test_user):
    page = BasePage(browser, base_url)

    # 1. авторизация
    page.open()
    Header(browser, base_url).go_to_personal_account()
    LoginPage(browser, base_url).login(
        test_user["email"], test_user["password"]
    )
    page.wait_url_not_contains("/login")

    # 2. открываем модалку ингредиента
    constructor = ConstructorPage(browser, base_url)
    constructor.open_ingredient_modal()
    constructor.assert_modal_opened()

    # 3. жмём крестик и убеждаемся, что окно исчезло
    assert constructor.close_modal(), "Модальное окно не закрылось"
