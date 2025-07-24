import allure
from pages import Header, LoginPage, ForgotPasswordPage, ResetPasswordPage

@allure.title("Переход на страницу восстановления пароля через «Личный Кабинет»")
def test_forgot_password_navigation(browser, base_url):
    # 1. Открываем https://stellarburgers.nomoreparties.site/forgot-password
    forgot_page = ForgotPasswordPage(browser, base_url)
    forgot_page.open()

    # 2. Кликаем «Личный Кабинет» в шапке
    header = Header(browser, base_url)
    header.go_to_personal_account()

    # 3. На форме входа нажимаем «Восстановить пароль»
    login_page = LoginPage(browser, base_url)
    login_page.go_to_forgot_password()

    # 4. Проверяем заголовок «Восстановление пароля» и URL
    forgot_page.assert_on_page()