import allure
from pages import Header, LoginPage, ForgotPasswordPage, ResetPasswordPage

TEST_EMAIL = "12399900@ya.ru"

@allure.title("Отправка e‑mail на странице «Восстановление пароля»")
def test_forgot_password_submit(browser, base_url):
    # 1. Открыть главную
    browser.get(base_url + "/")

    # 2. Клик «Личный Кабинет» в шапке → страница логина
    Header(browser, base_url).go_to_personal_account()

    # 3. Клик «Восстановить пароль» на форме логина
    LoginPage(browser, base_url).go_to_forgot_password()

    # 4–5. Ввод e‑mail + клик кнопки «Восстановить»
    forgot_page = ForgotPasswordPage(browser, base_url)
    forgot_page.restore_password(TEST_EMAIL)

    # Проверяем, что нас перекинуло на шаг ввода кода (URL содержит /reset-password)
    assert "/reset-password" in browser.current_url, "Не перешли к шагу ввода кода из письма"
