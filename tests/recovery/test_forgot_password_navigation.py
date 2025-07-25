import allure

from pages.base_page import BasePage
from pages import (
    Header,
    LoginPage,
    ForgotPasswordPage,
    ResetPasswordPage,
)

TEST_EMAIL    = "12399900@ya.ru"
TEST_PASSWORD = "12345678"

@allure.title("Переход на страницу восстановления пароля через «Личный Кабинет»")
def test_forgot_password_navigation(browser, base_url):
    page = BasePage(browser, base_url)

    # 1. /forgot-password
    forgot = ForgotPasswordPage(browser, base_url)
    forgot.open()                               

    # 2. «Личный кабинет» в шапке
    Header(browser, base_url).go_to_personal_account()

    # 3. На форме входа — «Восстановить пароль»
    LoginPage(browser, base_url).go_to_forgot_password()

    # 4. Проверяем, что снова оказались на forgot‑странице
    forgot.assert_on_page()


@allure.title("Отправка e‑mail на странице «Восстановление пароля»")
def test_forgot_password_submit(browser, base_url):
    page = BasePage(browser, base_url)
    page.open()                                  # главная

    Header(browser, base_url).go_to_personal_account()
    LoginPage(browser, base_url).go_to_forgot_password()

    # ввод e‑mail + «Восстановить»
    ForgotPasswordPage(browser, base_url).restore_password(TEST_EMAIL)

    # ➜ должны быть на шаге /reset-password
    ResetPasswordPage(browser, base_url).assert_on_page()


@allure.title("Иконка «глаз» активирует поле: ввод пароля проходит")
def test_password_eye_icon_input(browser, base_url):
    page = BasePage(browser, base_url)
    page.open()

    Header(browser, base_url).go_to_personal_account()
    LoginPage(browser, base_url).go_to_forgot_password()

    ForgotPasswordPage(browser, base_url).restore_password(TEST_EMAIL)

    reset = ResetPasswordPage(browser, base_url)
    reset.click_eye_icon()
    reset.enter_password(TEST_PASSWORD)

    assert (
        reset.get_password_value() == TEST_PASSWORD
    ), "Пароль не ввёлся в поле"
