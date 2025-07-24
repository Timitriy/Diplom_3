import allure
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from pages import Header, LoginPage, ProfilePage

@allure.title("Авторизация и переход во вкладку «История заказов»")
def test_open_order_history(browser, base_url, test_user):
    browser.get(base_url + "/")

    # авторизация
    Header(browser, base_url).go_to_personal_account()
    LoginPage(browser, base_url).login(test_user["email"], test_user["password"])
    WebDriverWait(browser, 10).until_not(EC.url_contains("/login"))

    # снова «Личный кабинет» → профиль
    Header(browser, base_url).go_to_personal_account()
    WebDriverWait(browser, 10).until(EC.url_contains("/account/profile"))

    # переход «История заказов»
    ProfilePage(browser, base_url).go_to_order_history()
    assert "/account/order-history" in browser.current_url
