from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC


class BasePage:
    def __init__(self, driver):
        self.driver = driver
        self.wait = WebDriverWait(self.driver, 10)

    def wait_for_visible(self, locator):
        return self.wait.until(EC.visibility_of_element_located(locator))

    def wait_for_clickable(self, locator):
        return self.wait.until(EC.element_to_be_clickable(locator))

    def click(self, locator):
        self.wait_for_clickable(locator).click()

    def send_keys(self, locator, text):
        element = self.wait_for_visible(locator)
        element.clear()
        element.send_keys(text)

    def get_text(self, locator):
        return self.wait_for_visible(locator).text

    def scroll_to(self, locator):
        element = self.wait_for_visible(locator)
        self.driver.execute_script("arguments[0].scrollIntoView();", element)

    def open_url(self, url):
        self.driver.get(url)
