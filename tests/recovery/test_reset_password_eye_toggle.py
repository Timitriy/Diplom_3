import allure
from pages import Header, LoginPage, ForgotPasswordPage, ResetPasswordPage

TEST_EMAIL    = "12399900@ya.ru"
TEST_PASSWORD = "12345678"

@allure.title("Иконка «глаз» активирует поле: ввод пароля проходит")
def test_password_eye_icon_input(browser, base_url):
    browser.get(base_url + "/")                        

    Header(browser, base_url).go_to_personal_account() 
    LoginPage(browser, base_url).go_to_forgot_password()  

    forgot = ForgotPasswordPage(browser, base_url)
    forgot.restore_password(TEST_EMAIL)                

    reset = ResetPasswordPage(browser, base_url)
    reset.click_eye_icon()                             
    reset.enter_password(TEST_PASSWORD)                # вводим «12345678»

    # Проверяем, что пароль действительно ввёлся
    assert reset.get_password_value() == TEST_PASSWORD, "Пароль не ввёлся в поле"
