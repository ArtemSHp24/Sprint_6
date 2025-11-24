import allure
from pages.base_page import BasePage
from locators.main_page_locators import MainPageLocators


class MainPage(BasePage):

    @allure.step("Открываю главную страницу: {url}")
    def open_main_page(self, url):
        self.open_url(url)

    @allure.step("Нажимаю на верхнюю кнопку 'Заказать'")
    def click_order_button_top(self):
        self.click(MainPageLocators.ORDER_BUTTON_TOP)

    @allure.step("Прокручиваю вниз и нажимаю на нижнюю кнопку 'Заказать'")
    def click_order_button_bottom(self):
        self.scroll_to(MainPageLocators.ORDER_BUTTON_BOTTOM)
        self.click(MainPageLocators.ORDER_BUTTON_BOTTOM)

    @allure.step("Нажимаю на логотип 'Самокат'")
    def click_logo_scooter(self):
        self.click(MainPageLocators.LOGO_SCOOTER)

    @allure.step("Нажимаю на логотип Яндекса")
    def click_logo_yandex(self):
        self.click(MainPageLocators.LOGO_YANDEX)
