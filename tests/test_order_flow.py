import allure
import pytest
from pages.main_page import MainPage
from pages.order_page import OrderPage
from data.order_data import BASE_URL, order_data


@allure.feature("Оформление заказа")
class TestOrderFlow:


    @allure.story("Пользователь оформляет заказ через верхнюю кнопку")
    @pytest.mark.parametrize("data", order_data)
    def test_order_scooter_flow_top(self, data, driver):
        main_page = MainPage(driver)
        order_page = OrderPage(driver)

        main_page.open_main_page(BASE_URL)
        main_page.click_order_button_top()

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


    @allure.story("Пользователь оформляет заказ через нижнюю кнопку")
    @pytest.mark.parametrize("data", order_data)
    def test_order_scooter_flow_bottom(self, data, driver):
        main_page = MainPage(driver)
        order_page = OrderPage(driver)

        main_page.open_main_page(BASE_URL)
        main_page.scroll_to_main_order_button()
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
