from selenium.webdriver.common.by import By

class ForgotPasswordLocators:
    """Локаторы страницы восстановления пароля."""

    # Заголовок страницы
    HEADING = (By.XPATH, "//h2[contains(text(),'Восстановление пароля')]")

    # Поле ввода e-mail
    EMAIL_INPUT = (By.CSS_SELECTOR, "input[name='name']")
    EMAIL_INPUT   = (By.CSS_SELECTOR, "input.input__textfield[name='name']")
    RESTORE_BTN   = (By.XPATH, "//button[.='Восстановить']")

    # Кнопка «Восстановить»
    RESTORE_BUTTON = (By.XPATH, "//button[.='Восстановить']")

    # Кнопка показать/скрыть пароль (иконка-«глаз») — станет активной после шага ввода кода/пароля
    TOGGLE_PASSWORD_VISIBILITY = (By.CSS_SELECTOR, "svg[type='password']")