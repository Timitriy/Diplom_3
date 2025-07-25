from selenium.webdriver.common.by import By

class LoginLocators:
    """Локаторы страницы логина / входа в аккаунт."""

    # Для авторизации
    EMAIL_INPUT   = (By.CSS_SELECTOR, "input.input__textfield[name='name']")
    PASSWORD_INPUT = (By.CSS_SELECTOR, "input.input__textfield[name='Пароль']")
    SUBMIT_BUTTON  = (By.XPATH, "//button[.='Войти' or @type='submit']")

    # Ссылка «Восстановить пароль» на форме входа
    FORGOT_PASSWORD_LINK = (By.CSS_SELECTOR, "a[href='/forgot-password']")

    # Заголовок «Вход» (опционально, для проверок)
    HEADING_LOGIN = (By.XPATH, "//h2[contains(text(),'Вход')]")