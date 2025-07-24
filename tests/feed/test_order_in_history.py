import allure, pytest
from pages import Header, LoginPage, ConstructorPage, OrderHistoryPage

@pytest.mark.order
@allure.title("Заказ из «Истории заказов» виден в «Ленте заказов»")
def test_order_number_present_in_history(browser, base_url, test_user):
    # 1‑2. авторизация + формирование заказа
    browser.get(base_url + "/")
    Header(browser, base_url).go_to_personal_account()
    LoginPage(browser, base_url).login(test_user["email"], test_user["password"])

    constructor = ConstructorPage(browser, base_url)
    constructor.drag_bun_to_constructor()
    constructor.place_order()

    # 3. сохраняем id из модалки
    order_id = constructor.get_order_id_from_modal()     
    constructor.close_order_modal()

    # 4‑6. переходим «Личный кабинет» → «История заказов»
    Header(browser, base_url).go_to_personal_account()
    header = Header(browser, base_url)
    header.go_to_order_history()                          
    history = OrderHistoryPage(browser, base_url)

    # 7. сравниваем
    assert order_id in history.get_order_numbers(), \
        f"Заказ {order_id} не найден в «Истории заказов»"
