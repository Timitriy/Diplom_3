import allure
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from pages import Header, LoginPage

EMAIL_PWD = "12345678"  # пароль задаём один раз

@allure.title("Авторизация в профиле валидным тестовым юзером")
def test_login_success(browser, base_url, test_user):
    browser.get(base_url + "/")

    Header(browser, base_url).go_to_personal_account()

    LoginPage(browser, base_url).login(test_user["email"], test_user["password"])

    # ждём, пока URL перестанет содержать /login
    WebDriverWait(browser, 10).until_not(EC.url_contains("/login"))
    assert browser.current_url.rstrip("/") == base_url, "Не вернулись на главную после логина"
