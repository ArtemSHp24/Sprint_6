import allure
from pages.main_page import MainPage
from selenium.webdriver.support.wait import WebDriverWait

BASE_URL = "https://qa-scooter.praktikum-services.ru/"


@allure.feature("Переходы по логотипам")
@allure.story("Редиректы с главной страницы")
@allure.title("Переход по лого 'Самокат' → главная страница")
def test_scooter_logo_redirects_to_main_page(driver):
    main_page = MainPage(driver)

    main_page.open_main_page(BASE_URL)
    main_page.click_logo_scooter()

    assert driver.current_url == BASE_URL


@allure.feature("Переходы по логотипам")
@allure.story("Редиректы с главной страницы")
@allure.title("Переход по лого 'Яндекс' → Дзен (новая вкладка)")
def test_yandex_logo_opens_dzen(driver):
    main_page = MainPage(driver)

    main_page.open_main_page(BASE_URL)
    main_page.click_logo_yandex()

    WebDriverWait(driver, 10).until(lambda d: len(d.window_handles) > 1)

    assert len(driver.window_handles) == 2