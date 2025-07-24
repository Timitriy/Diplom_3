import allure
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from pages import Header, LoginPage, ConstructorPage, FeedPage

@allure.title("Клик по заказу в ленте открывает модальное окно деталей")
def test_feed_order_modal(browser, base_url, test_user):
    # авторизация
    browser.get(base_url + "/")
    Header(browser, base_url).go_to_personal_account()
    LoginPage(browser, base_url).login(test_user["email"], test_user["password"])
    WebDriverWait(browser, 10).until_not(EC.url_contains("/login"))

    # создаём любой заказ (булку перетаскиваем в конструктор)
    constructor = ConstructorPage(browser, base_url)
    constructor.drag_bun_to_constructor()
    constructor.place_order()
    constructor.assert_order_modal_opened()
    constructor.close_modal()          # закрыли всплывающее окно заказа

    # переходим в «Ленту заказов»
    Header(browser, base_url).go_to_order_feed()

    # кликаем первый заказ и проверяем модалку
    feed = FeedPage(browser, base_url)
    feed.open_first_order_modal()
    feed.assert_modal_opened()
