import pytest
import allure
from Sprint_6.locators import *
from Sprint_6.helpers import *
from Sprint_6.pages.page_object_main_page import *

@pytest.mark.usefixtures("driver")
class TestSectionQuestionAboutThings:

    # параметры проверки
    @allure.title('Проверка ответов на вопросы в разделе "Вопросы о важном"')
    @pytest.mark.parametrize("question_key", list(questions_data.keys()))
    def test_check_texts_inside_questions(self, question_key):
        
        data = questions_data[question_key]
        
        #'Перешли на страницу тестового приложения'
        self.driver.get('https://qa-scooter.praktikum-services.ru')

        # Объект класса страницы
        section_question = MainPageScooter(self.driver)
        
        #"Ожидание загрузки заголовка 'Вопросы о важном'"
        section_question.wait_for_header_question(header_question_about_important)
        
        #"Прокрутка до заголовка 'Вопросы о важном'"
        section_question.scroll_to_element(header_question_about_important)
        
        #"Клик по кнопке вопроса"
        section_question.click_on_the_question_button(data["button"])

        #"Ожидание загрузки текста ответа на вопрос"
        section_question.wait_for_text_question(data["text_locator"])

        #"Текст ответа на вопрос"
        text = section_question.get_text_inside_section(data["text_locator"])

        #"Проверка, что полученное значение текста совпадает"
        assert text == data["expected"]
    

