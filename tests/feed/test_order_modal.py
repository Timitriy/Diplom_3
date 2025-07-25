import time
import allure

from pages.base_page import BasePage
from pages import (
    Header,
    LoginPage,
    ConstructorPage,
    FeedPage,
    OrderHistoryPage,
)
from locators import FeedLocators

@allure.title("Авторизация и переход по клику «Лента заказов»")
def test_open_feed_from_header(browser, base_url, test_user):
    page = BasePage(browser, base_url)

    # 1. Главная → логин
    page.open()
    Header(browser, base_url).go_to_personal_account()
    LoginPage(browser, base_url).login(test_user["email"], test_user["password"])
    page.wait_url_not_contains("/login")

    # 2. «Лента заказов» в шапке
    Header(browser, base_url).go_to_feed()
    page.wait_url_contains("/feed")

    # 3. Проверяем переход
    assert "/feed" in page.get_url(), "Не открылась «Лента заказов»"


@allure.title("Клик по заказу в ленте открывает модальное окно деталей")
def test_feed_order_modal(browser, base_url, test_user):
    page = BasePage(browser, base_url)

    # 1. Авторизация
    page.open()
    Header(browser, base_url).go_to_personal_account()
    LoginPage(browser, base_url).login(test_user["email"], test_user["password"])
    page.wait_url_not_contains("/login")

    # 2. Создаём любой заказ
    constructor = ConstructorPage(browser, base_url)
    constructor.drag_bun_to_constructor()
    constructor.place_order()
    constructor.assert_order_modal_opened()
    constructor.close_modal()

    # 3. Переходим в ленту заказов
    Header(browser, base_url).go_to_order_feed()
    feed = FeedPage(browser, base_url)
    page.wait_url_contains("/feed")

    # 4. Берём id первого заказа в списке
    first_card = feed.element(FeedLocators.ORDER_CARD)
    order_id_on_card = first_card.text.split()[0]

    # 5. Открываем модалку и проверяем номер
    feed.open_first_order_modal()
    feed.assert_modal_opened()
    modal_text = feed.element(FeedLocators.ORDER_MODAL_BOX).text
    assert order_id_on_card in modal_text, (
        f"Ожидали номер заказа {order_id_on_card} в модалке, получили: {modal_text}"
    )

    # 6. Закрываем модальное окно и проверяем
    assert feed.close_modal(), "Модальное окно не закрылось"


@allure.title("Заказ из «Истории заказов» виден в «Ленте заказов»")
def test_order_number_present_in_history(browser, base_url, test_user):
    page = BasePage(browser, base_url)

    # 1. Авторизация + формирование заказа
    page.open()
    Header(browser, base_url).go_to_personal_account()
    LoginPage(browser, base_url).login(test_user["email"], test_user["password"])
    page.wait_url_not_contains("/login")

    constructor = ConstructorPage(browser, base_url)
    constructor.drag_bun_to_constructor()
    constructor.place_order()

    # 2. Сохраняем id заказа
    order_id = constructor.get_order_id_from_modal()
    constructor.close_order_modal()

    # 3. «Личный кабинет» → «История заказов»
    header = Header(browser, base_url)
    header.go_to_personal_account()
    header.go_to_order_history()
    history = OrderHistoryPage(browser, base_url)

    assert order_id in history.get_order_numbers(), (
        f"Заказ {order_id} не найден в «Истории заказов»"
    )


@allure.title("Новый заказ появляется в списке «В работе»")
def test_order_appears_in_work(browser, base_url, test_user):
    page = BasePage(browser, base_url)

    # 1. Авторизация
    page.open()
    Header(browser, base_url).go_to_personal_account()
    LoginPage(browser, base_url).login(test_user["email"], test_user["password"])
    page.wait_url_not_contains("/login")

    # 2. Формируем заказ и получаем id
    constructor = ConstructorPage(browser, base_url)
    constructor.drag_bun_to_constructor()
    constructor.place_order()
    order_id = constructor.get_order_id_from_modal()
    constructor.close_order_modal()

    # 3. Лента заказов
    Header(browser, base_url).go_to_feed()
    feed = FeedPage(browser, base_url)
    page.wait_url_contains("/feed")

    # 4. Даем бекенду время обновить статус
    time.sleep(10)

    assert order_id in feed.get_in_work_numbers(), (
        f"Заказ {order_id} не найден в разделе «В работе»"
    )


@allure.title("«Выполнено за всё время» увеличивается после создания заказа")
def test_completed_all_time_counter(browser, base_url, test_user):
    page = BasePage(browser, base_url)

    # 1. Авторизация
    page.open()
    Header(browser, base_url).go_to_personal_account()
    LoginPage(browser, base_url).login(test_user["email"], test_user["password"])
    page.wait_url_not_contains("/login")

    # 2. Запоминаем счётчик
    Header(browser, base_url).go_to_feed()
    feed = FeedPage(browser, base_url)
    page.wait_url_contains("/feed")
    total_before = feed.get_completed_all_time()

    # 3. Создаём заказ
    Header(browser, base_url).go_to_constructor()
    constructor = ConstructorPage(browser, base_url)
    constructor.drag_bun_to_constructor()
    constructor.place_order()
    constructor.close_order_modal()

    # 4. Проверяем, что счётчик вырос
    Header(browser, base_url).go_to_feed()
    page.wait_url_contains("/feed")
    total_after = feed.get_completed_all_time()

    assert total_after > total_before, (
        f"Счётчик не вырос: было {total_before}, стало {total_after}"
    )


@allure.title("«Выполнено за сегодня» увеличивается после создания заказа")
def test_completed_today_counter(browser, base_url, test_user):
    page = BasePage(browser, base_url)

    # 1. Авторизация
    page.open()
    Header(browser, base_url).go_to_personal_account()
    LoginPage(browser, base_url).login(test_user["email"], test_user["password"])
    page.wait_url_not_contains("/login")

    # 2. Сохраняем счётчик «за сегодня»
    Header(browser, base_url).go_to_feed()
    feed = FeedPage(browser, base_url)
    page.wait_url_contains("/feed")
    today_before = feed.get_completed_today()

    # 3. Создаём новый заказ
    Header(browser, base_url).go_to_constructor()
    constructor = ConstructorPage(browser, base_url)
    constructor.drag_bun_to_constructor()
    constructor.place_order()
    constructor.close_order_modal()

    # 4. Проверяем увеличение счётчика
    Header(browser, base_url).go_to_feed()
    page.wait_url_contains("/feed")
    assert feed.get_completed_today() > today_before, (
        "Счётчик «Выполнено за сегодня» не увеличился"
    )
