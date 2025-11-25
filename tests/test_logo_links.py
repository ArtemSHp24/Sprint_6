import allure
from selenium.webdriver.common.by import By
from pages.main_page import MainPage
from data.order_data import BASE_URL
from locators.main_page_locators import MainPageLocators


@allure.feature("Переходы по логотипам")
@allure.story("Редиректы с главной страницы")
class TestLogoLinks:

    @allure.title("Переход по лого 'Самокат' → главная страница")
    def test_scooter_logo_redirects_to_main_page(self, driver):
        main_page = MainPage(driver)

        main_page.open_main_page(BASE_URL)
        main_page.click_logo_scooter()

        assert main_page.get_current_url() == BASE_URL


    @allure.title("Переход по лого 'Яндекс' → Дзен (новая вкладка)")
    def test_yandex_logo_opens_dzen(self, driver):
        main_page = MainPage(driver)

        main_page.open_main_page(BASE_URL)
        main_page.click_logo_yandex()

        main_page.switch_to_new_tab()

        assert main_page.element_exists(MainPageLocators.DZEN_META)