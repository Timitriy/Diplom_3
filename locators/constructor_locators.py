from selenium.webdriver.common.by import By

class ConstructorLocators:
    INGREDIENT_CARD = (By.CSS_SELECTOR, "img[alt='Флюоресцентная булка R2-D3']")
    MODAL_TITLE     = (By.XPATH, "//h2[contains(text(),'Детали ингредиента')]")
    MODAL_CLOSE_BTN = (By.CSS_SELECTOR, "button.Modal_modal__close__TnseK")
    CONSTRUCTOR_DROP_ZONE = (
        By.CSS_SELECTOR, "div.constructor-element_pos_top"
    )
    INGREDIENT_COUNTER = (
        By.XPATH,
        "//img[@alt='Флюоресцентная булка R2-D3']"
        "/following-sibling::span[contains(@class,'Counter_counter__num')]"
    )
    BASKET_TOTAL = (
        By.CSS_SELECTOR,
        "div.BurgerConstructor_basket__totalContainer__2Z-ho p.text_type_digits-medium"
    )
    ORDER_BUTTON      = (By.CSS_SELECTOR, "button.button_button_size_large__G21Vg")  
    ORDER_MODAL_ID    = (By.CSS_SELECTOR, "div.Modal_modal__contentBox__sCy8X h2")
    ORDER_ID = (By.CSS_SELECTOR, "h2.Modal_modal__title__2L34m")

