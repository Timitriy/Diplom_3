import allure
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from pages import Header, LoginPage, ProfilePage

@allure.title("Авторизация и выход из аккаунта")
def test_logout(browser, base_url, test_user):
    # 1. авторизация
    browser.get(base_url + "/")
    Header(browser, base_url).go_to_personal_account()
    LoginPage(browser, base_url).login(test_user["email"], test_user["password"])
    WebDriverWait(browser, 10).until_not(EC.url_contains("/login"))

    # 2. «Личный кабинет» → профиль
    Header(browser, base_url).go_to_personal_account()
    WebDriverWait(browser, 10).until(EC.url_contains("/account/profile"))

    # 3. клик «Выход»
    ProfilePage(browser, base_url).logout()

    # Проверяем, что снова на странице логина
    WebDriverWait(browser, 10).until(EC.url_contains("/login"))
    assert "/login" in browser.current_url, "Не попали на форму входа после выхода"
