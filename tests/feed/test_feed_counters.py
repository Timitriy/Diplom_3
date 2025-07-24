import allure, pytest
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from pages import Header, LoginPage, ConstructorPage, FeedPage

@pytest.mark.order
@allure.title('«Выполнено за всё время» увеличивается после создания заказа')
def test_completed_all_time_counter(browser, base_url, test_user):
    # 1. Авторизация
    browser.get(base_url + "/")
    Header(browser, base_url).go_to_personal_account()
    LoginPage(browser, base_url).login(test_user["email"], test_user["password"])
    WebDriverWait(browser, 10).until_not(EC.url_contains("/login"))

    # 2‑3. Переходим в «Ленту» и запоминаем счётчик
    Header(browser, base_url).go_to_feed()
    feed = FeedPage(browser, base_url)
    total_before = feed.get_completed_all_time()

    # 4‑6. Создаём новый заказ через конструктор
    Header(browser, base_url).go_to_constructor()
    constructor = ConstructorPage(browser, base_url)
    constructor.drag_bun_to_constructor()
    constructor.place_order()
    constructor.assert_order_modal_opened()
    constructor.close_order_modal()

    # 7‑8. Возвращаемся в «Ленту» и сравниваем
    Header(browser, base_url).go_to_feed()
    total_after = feed.get_completed_all_time()

    assert total_after > total_before, (
        f"Счётчик не вырос: было {total_before}, стало {total_after}"
    )

@pytest.mark.order
@allure.title('«Выполнено за сегодня» увеличивается после создания заказа')
def test_completed_today_counter(browser, base_url, test_user):
    # Авторизация
    browser.get(base_url + "/")
    Header(browser, base_url).go_to_personal_account()
    LoginPage(browser, base_url).login(test_user["email"], test_user["password"])
    WebDriverWait(browser, 10).until_not(EC.url_contains("/login"))

    # Запоминаем счётчик «за сегодня» в ленте
    Header(browser, base_url).go_to_feed()
    feed = FeedPage(browser, base_url)
    today_before = feed.get_completed_today()

    # Формируем новый заказ
    Header(browser, base_url).go_to_constructor()
    constructor = ConstructorPage(browser, base_url)
    constructor.drag_bun_to_constructor()
    constructor.place_order()
    constructor.assert_order_modal_opened()
    constructor.close_order_modal()

    # Проверяем, что счётчик вырос
    Header(browser, base_url).go_to_feed()
    assert feed.get_completed_today() > today_before, \
        "Счётчик «Выполнено за сегодня» не увеличился"