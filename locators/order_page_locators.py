from selenium.webdriver.common.by import By


class OrderPageLocators:

    FIRST_NAME_INPUT = (By.CSS_SELECTOR, "input[placeholder='* Имя']")
    LAST_NAME_INPUT = (By.CSS_SELECTOR, "input[placeholder='* Фамилия']")
    ADDRESS_INPUT = (By.CSS_SELECTOR, "input[placeholder='* Адрес: куда привезти заказ']")
    METRO_INPUT = (By.CSS_SELECTOR, "input[placeholder='* Станция метро']")
    METRO_ITEM = lambda name: (
    By.XPATH, f"//button[contains(@class, 'select-search__option') and text()='{name}']"
)
    PHONE_INPUT = (By.CSS_SELECTOR, "input[placeholder='* Телефон: на него позвонит курьер']")
    NEXT_BUTTON = (By.CSS_SELECTOR, "div.Order_NextButton__1_rCA button")

    
    DATE_INPUT = (By.CSS_SELECTOR, "input[placeholder='* Когда привезти самокат']")
    DATE_DAY = lambda day: (By.XPATH,
    f"//div[contains(@class,'react-datepicker__day') and text()='{day}']"
)    
    RENT_TIME_INPUT = (By.CSS_SELECTOR, "div.Dropdown-control")
    RENT_TIME_MENU = (By.CSS_SELECTOR, "div.Dropdown-menu")
    RENT_TIME_OPTION = lambda text: (
    By.XPATH, f"//div[@class='Dropdown-option' and text()='{text}']")

    COLOR_BLACK = (By.CSS_SELECTOR, "label[for='black']")
    COLOR_GREY = (By.CSS_SELECTOR, "label[for='grey']")

    COMMENT_INPUT = (By.CSS_SELECTOR, "input[placeholder='Комментарий для курьера']")
    ORDER_SUBMIT_BUTTON = (
    By.XPATH,
    "//div[contains(@class, 'Order_Content')]//button[text()='Заказать']"
)


    ORDER_MODAL = (By.CSS_SELECTOR, "div[class^='Order_Modal']")
    ORDER_MODAL_HEADER = (By.CSS_SELECTOR, "div[class^='Order_ModalHeader']")
