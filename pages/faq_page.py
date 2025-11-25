import allure
from pages.base_page import BasePage
from locators.faq_page_locators import FAQPageLocators


class FAQPage(BasePage):

    @allure.step("Открываю вопрос FAQ: {question_locator}")
    def open_question(self, question_locator):
        self.scroll_to(question_locator)
        self.click(question_locator)

    @allure.step("Получаю текст ответа FAQ: {answer_locator}")
    def get_answer_text(self, answer_locator):
        return self.get_text(answer_locator)
