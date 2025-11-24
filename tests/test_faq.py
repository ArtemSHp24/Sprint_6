import pytest
from pages.faq_page import FAQPage
from pages.main_page import MainPage
from locators.faq_page_locators import FAQPageLocators


BASE_URL = "https://qa-scooter.praktikum-services.ru/"


@pytest.mark.parametrize("question, answer", [
    (FAQPageLocators.QUESTION_0, FAQPageLocators.ANSWER_0),
    (FAQPageLocators.QUESTION_1, FAQPageLocators.ANSWER_1),
    (FAQPageLocators.QUESTION_2, FAQPageLocators.ANSWER_2),
    (FAQPageLocators.QUESTION_3, FAQPageLocators.ANSWER_3),
    (FAQPageLocators.QUESTION_4, FAQPageLocators.ANSWER_4),
    (FAQPageLocators.QUESTION_5, FAQPageLocators.ANSWER_5),
    (FAQPageLocators.QUESTION_6, FAQPageLocators.ANSWER_6),
    (FAQPageLocators.QUESTION_7, FAQPageLocators.ANSWER_7),
])
def test_faq_answers(driver, question, answer):
    main_page = MainPage(driver)
    faq_page = FAQPage(driver)

    main_page.open_main_page(BASE_URL)
    faq_page.open_question(question)
    answer_text = faq_page.get_answer_text(answer)

    assert answer_text.strip() != ""
