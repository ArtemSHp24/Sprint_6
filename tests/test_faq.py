import allure
import pytest
from pages.faq_page import FAQPage
from locators.faq_page_locators import FAQPageLocators
from data.faq_data import faq_expected
from data.order_data import BASE_URL


questions = [
    (FAQPageLocators.QUESTION_0, FAQPageLocators.ANSWER_0, faq_expected[0]),
    (FAQPageLocators.QUESTION_1, FAQPageLocators.ANSWER_1, faq_expected[1]),
    (FAQPageLocators.QUESTION_2, FAQPageLocators.ANSWER_2, faq_expected[2]),
    (FAQPageLocators.QUESTION_3, FAQPageLocators.ANSWER_3, faq_expected[3]),
    (FAQPageLocators.QUESTION_4, FAQPageLocators.ANSWER_4, faq_expected[4]),
    (FAQPageLocators.QUESTION_5, FAQPageLocators.ANSWER_5, faq_expected[5]),
    (FAQPageLocators.QUESTION_6, FAQPageLocators.ANSWER_6, faq_expected[6]),
    (FAQPageLocators.QUESTION_7, FAQPageLocators.ANSWER_7, faq_expected[7]),
]

@allure.feature("FAQ")
class TestFAQ:

    @allure.title("Проверка текста ответов FAQ")
    @pytest.mark.parametrize("question, answer, expected", questions)
    def test_faq_answers(self, question, answer, expected, driver):
        page = FAQPage(driver)
        page.open_url(BASE_URL)

        page.open_question(question)
        actual = page.get_answer_text(answer).strip()

        assert actual == expected
