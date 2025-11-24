from selenium.webdriver.common.by import By


class MainPageLocators:
   
    ORDER_BUTTON_TOP = (By.XPATH, "(//button[text()='Заказать'])[1]")

    ORDER_BUTTON_BOTTOM = (By.XPATH, "(//button[text()='Заказать'])[2]")

    LOGO_SCOOTER = (By.CSS_SELECTOR, "img[alt='Scooter']")

    LOGO_YANDEX = (By.CSS_SELECTOR, "a[href='//yandex.ru']")
