import allure
import pytest
from pages.main_page import MainPage
from pages.order_page import OrderPage


BASE_URL = "https://qa-scooter.praktikum-services.ru/"


test_data = [
    {
        "first_name": "Иван",
        "last_name": "Иванов",
        "address": "Москва, Пушкина 10",
        "station": "Черкизовская",
        "phone": "+79993334455",
        "day": "10",
        "rent": "сутки",
        "color": "black",
        "comment": "Позвоните за час"
    },
    {
        "first_name": "Мария",
        "last_name": "Петрова",
        "address": "Москва, Арбат 12",
        "station": "Сокол",
        "phone": "+79998887766",
        "day": "15",
        "rent": "двое суток",
        "color": "grey",
        "comment": "Оставьте у двери"
    }
]

@allure.feature("Оформление заказа")
@allure.story("Полный пользовательский сценарий")
@pytest.mark.parametrize("button_position", ["top", "bottom"])
@pytest.mark.parametrize("data", test_data)
@allure.title("Заказ самоката через кнопку: {button_position} | Имя: {data[first_name]} | Станция: {data[station]}")
def test_order_scooter_flow(driver, button_position, data):

    main_page = MainPage(driver)
    order_page = OrderPage(driver)

    main_page.open_main_page(BASE_URL)

    if button_position == "top":
        main_page.click_order_button_top()
    else:
        main_page.click_order_button_bottom()

    order_page.set_first_name(data["first_name"])
    order_page.set_last_name(data["last_name"])
    order_page.set_address(data["address"])
    order_page.set_metro_station(data["station"])
    order_page.set_phone(data["phone"])
    order_page.click_next()

    order_page.set_date(data["day"])
    order_page.set_rent_term(data["rent"])

    if data["color"] == "black":
        order_page.choose_black_color()
    else:
        order_page.choose_grey_color()

    order_page.set_comment(data["comment"])
    order_page.click_order_button()

    assert order_page.is_order_modal_visible()
    assert order_page.get_order_modal_text() == "Хотите оформить заказ?"
