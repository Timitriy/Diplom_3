from selenium.webdriver.common.by import By

class ProfileLocators:
    ORDER_HISTORY_LINK = (By.CSS_SELECTOR, "a[href='/account/order-history']")
    LOGOUT_BUTTON      = (By.XPATH, "//button[normalize-space()='Выход']")
