from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from locators.main_page_locators import MainPageLocators


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

    def scroll_element(self, element):
        self.driver.execute_script("arguments[0].scrollIntoView(true);", element)

    def js_click(self, locator):
        element = self.wait_for_visible(locator)
        self.driver.execute_script("arguments[0].click();", element)

    def wait_for_new_tab_opened(self):
        self.wait.until(lambda d: len(d.window_handles) > 1)

    def get_current_url(self):
        return self.driver.current_url

    def switch_to_new_tab(self):
        self.wait.until(lambda d: len(d.window_handles) > 1)
        new_tab = self.driver.window_handles[-1]
        self.driver.switch_to.window(new_tab)
        self.wait.until(lambda d: d.current_url != "about:blank")

    def get_tabs_count(self):
        return len(self.driver.window_handles)
    
    def element_exists(self, locator):
        try:
            self.wait.until(EC.presence_of_element_located(locator))
            return True
        except:
            return False
        
    
    def accept_cookies(self):
        try:
            btn = WebDriverWait(self.driver, 3).until(
                EC.element_to_be_clickable(MainPageLocators.COOKIE_ACCEPT)
            )
            btn.click()
        except:
            pass