import allure
from Sprint_6.locators import *
from Sprint_6.pages.page_object_base_page import *

# Класс главная страница
class MainPageScooter(BasePage):

    @allure.step("метод ожидания загрузки кнопки Яндекс")
    def wait_logo(self):
        return super().wait_logo()
    
    @allure.step("метод получения URL")
    def current_url(self):
        return super().current_url()

    @allure.step("метод нажатия кнопки вопроса")
    def click_on_the_question_button(self, question_name_on_button):
        self.js_click(question_name_on_button)

    @allure.step("метод для получения текста элемента в заголовке")
    def get_text_inside_section(self, text_inside_section):
        return self.find_element(text_inside_section).text
    
    @allure.step("метод нажатия в лого кнопки Яндекс")
    def click_on_button_logo_yandex(self):
        self.click(button_yandex)

    @allure.step("метод нажатия в лого кнопки Самокат")
    def click_on_button_logo_scooter(self):
        self.click(button_scooter)

    

