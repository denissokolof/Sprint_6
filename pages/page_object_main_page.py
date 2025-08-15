from selenium import webdriver
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.wait import WebDriverWait
from Sprint_6.locators import *

# Класс главная страница
class MainPageScooter:

    def __init__(self, driver):
        self.driver = driver
    
    # метод ожидания загрузки заголовка раздела "Вопросы о важном"
    def wait_for_header_question(self, header_question_about_important):
        WebDriverWait(self.driver, 3).until(EC.visibility_of_element_located(header_question_about_important))
    
    # метод прокрутки до раздела "Вопросы о важном"
    def scroll_to_element(self, header_question_about_important):
        element = self.driver.find_element(*header_question_about_important)
        self.driver.execute_script("arguments[0].scrollIntoView();", element)

    # метод нажатия кнопки вопроса
    def click_on_the_question_button(self, question_name_on_button):
        self.driver.find_element(*question_name_on_button).click()

    def wait_for_text_question(self, text_inside_section):
        WebDriverWait(self.driver, 3).until(EC.visibility_of_element_located(text_inside_section))

    # метод для получения текста элемента в заголовке
    def get_text_inside_section(self, text_inside_section):
        return self.driver.find_element(*text_inside_section).text
    
    # метод нажатия в лого кнопки Яндекс
    def click_on_button_logo_yandex(self):
        self.driver.find_element(*button_yandex).click()
    
    # метод ожидания загрузки кнопки Яндекс
    def wait_logo(self):
        WebDriverWait(self.driver, 5).until(EC.visibility_of_element_located(button_yandex))

   # метод нажатия в лого кнопки Самокат
    def click_on_button_logo_scooter(self):
        self.driver.find_element(*button_scooter).click()

