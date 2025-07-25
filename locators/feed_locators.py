from selenium.webdriver.common.by import By

class FeedLocators:
    FEED_LINK        = (By.CSS_SELECTOR, "a[href='/feed']")

    ORDER_CARD       = (By.CSS_SELECTOR, "a.OrderHistory_link__1iNby")
    ORDER_MODAL_BOX  = (By.CSS_SELECTOR, "div.Modal_orderBox__1xWdi")
    MODAL_CLOSE_BTN  = (By.CSS_SELECTOR, "button.Modal_modal__close__TnseK")
    COMPLETED_ALL_TIME = (By.XPATH,"//p[contains(text(),'Выполнено за всё время')]/following-sibling::p",)
    COMPLETED_NUMBERS = (By.CSS_SELECTOR, "p.OrderFeed_number__2MbrQ")
    COMPLETED_TODAY = (By.XPATH,"//p[normalize-space()='Выполнено за сегодня:']/following-sibling::p")
    IN_WORK_NUMBERS = (By.CSS_SELECTOR,"ul.OrderFeed_orderListReady__1YFem li")