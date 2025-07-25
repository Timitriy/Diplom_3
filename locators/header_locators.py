from selenium.webdriver.common.by import By

class HeaderLocators:
    """Локаторы элементов шапки сайта."""

    PERSONAL_ACCOUNT = (By.CSS_SELECTOR, "a[href='/account']")
    CONSTRUCTOR_LINK = (By.CSS_SELECTOR, "a[href='/']")
    FEED_LINK         = (By.CSS_SELECTOR, "a[href='/feed']")
    ORDER_HISTORY_LINK = (By.CSS_SELECTOR, "a[href='/account/order-history']")