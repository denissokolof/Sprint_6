import allure
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.wait import WebDriverWait
from Sprint_6.locators import *

# Класс главная страница
class MainPageScooter:

    def __init__(self, driver):
        self.driver = driver

    @allure.step("метод нажатия кнопки вопроса")
    def click_on_the_question_button(self, question_name_on_button):
        element = self.driver.find_element(*question_name_on_button)
        self.driver.execute_script("arguments[0].click();", element)

    @allure.step("метод для получения текста элемента в заголовке")
    def get_text_inside_section(self, text_inside_section):
        return self.driver.find_element(*text_inside_section).text
    
    @allure.step("метод нажатия в лого кнопки Яндекс")
    def click_on_button_logo_yandex(self):
        self.driver.find_element(*button_yandex).click()

    @allure.step("метод нажатия в лого кнопки Самокат")
    def click_on_button_logo_scooter(self):
        self.driver.find_element(*button_scooter).click()

    

