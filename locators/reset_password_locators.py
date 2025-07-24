from selenium.webdriver.common.by import By

class ResetPasswordLocators:
    # поле пароля (видимое и в режиме «password», и в режиме «text»)
    PASSWORD_INPUT = (By.CSS_SELECTOR, "input.input__textfield")

    # иконка «глаз»
    TOGGLE_PASSWORD_VISIBILITY = (By.CSS_SELECTOR, "div.input__icon-action svg")

