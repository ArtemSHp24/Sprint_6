import allure
from pages.base_page import BasePage
from locators.order_page_locators import OrderPageLocators
from selenium.webdriver.common.keys import Keys


class OrderPage(BasePage):

    @allure.step("Ввожу имя: {name}")
    def set_first_name(self, name):
        self.send_keys(OrderPageLocators.FIRST_NAME_INPUT, name)

    @allure.step("Ввожу фамилию: {last_name}")
    def set_last_name(self, last_name):
        self.send_keys(OrderPageLocators.LAST_NAME_INPUT, last_name)

    @allure.step("Ввожу адрес: {address}")
    def set_address(self, address):
        self.send_keys(OrderPageLocators.ADDRESS_INPUT, address)

    @allure.step("Выбираю станцию метро: {station_name}")
    def set_metro_station(self, station_name):
        element = self.wait_for_visible(OrderPageLocators.METRO_INPUT)
        element.click()
        element.clear()
        element.send_keys(station_name)
        element.send_keys(Keys.ARROW_DOWN)
        element.send_keys(Keys.ENTER)

    @allure.step("Ввожу телефон: {phone}")
    def set_phone(self, phone):
        self.send_keys(OrderPageLocators.PHONE_INPUT, phone)

    @allure.step("Нажимаю кнопку Далее")
    def click_next(self):
        self.click(OrderPageLocators.NEXT_BUTTON)

    @allure.step("Выбираю дату: {day} число")
    def set_date(self, day):
        self.click(OrderPageLocators.DATE_INPUT)
        self.click(OrderPageLocators.DATE_DAY(day))

    @allure.step("Устанавливаю срок аренды: {rent_text}")
    def set_rent_term(self, rent_text):
        self.click(OrderPageLocators.RENT_TIME_INPUT)
        self.wait_for_visible(OrderPageLocators.RENT_TIME_MENU)
        self.click(OrderPageLocators.RENT_TIME_OPTION(rent_text))

    @allure.step("Выбираю чёрный цвет самоката")
    def choose_black_color(self):
        self.click(OrderPageLocators.COLOR_BLACK)

    @allure.step("Выбираю серый цвет самоката")
    def choose_grey_color(self):
        self.click(OrderPageLocators.COLOR_GREY)

    @allure.step("Пишу комментарий: {text}")
    def set_comment(self, text):
        self.send_keys(OrderPageLocators.COMMENT_INPUT, text)

    @allure.step("Нажимаю кнопку Заказать")
    def click_order_button(self):
        element = self.wait_for_visible(OrderPageLocators.ORDER_SUBMIT_BUTTON)
        self.driver.execute_script("arguments[0].scrollIntoView(true);", element)
        self.driver.execute_script("arguments[0].click();", element)

    @allure.step("Проверяю, что модальное окно заказа отображается")
    def is_order_modal_visible(self):
        return self.wait_for_visible(OrderPageLocators.ORDER_MODAL)

    @allure.step("Получаю текст заголовка модального окна")
    def get_order_modal_text(self):
        element = self.wait_for_visible(OrderPageLocators.ORDER_MODAL_HEADER)
        return element.text.strip()
