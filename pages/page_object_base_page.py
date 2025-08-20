import allure
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.wait import WebDriverWait
from Sprint_6.locators import *

# Класс главная страница
class BasePage:

    def __init__(self, driver):
        self.driver = driver

    def find_element(self, locator):
        return self.driver.find_element(*locator)
    
    def click(self, locator):
        return self.driver.find_element(*locator).click()
    
    def wait_for_element(self, locator, timeout=5):
        return WebDriverWait(self.driver, timeout).until(EC.visibility_of_any_elements_located(locator))
    
    def wait_and_click(self, locator, timeout=5):
        element = WebDriverWait(self.driver, timeout).until(EC.element_to_be_clickable(locator))
        element.click()
    
    def scroll_and_click(self, locator, timeout=5):
        WebDriverWait(self.driver, timeout).until(EC.element_to_be_clickable(locator))
        element = self.find_element(locator)
        self.driver.execute_script("arguments[0].scrollIntoView({block: 'center'});", element)   
        self.click(locator)
    
    def js_click(self, locator, timeout=5):
        WebDriverWait(self.driver, timeout).until(EC.presence_of_element_located(locator))
        element = self.find_element(locator)
        self.driver.execute_script("arguments[0].click();", element)
    
    def current_url(self):
        return self.driver.current_url
    
    @allure.step("метод ожидания загрузки заголовка раздела 'Вопросы о важном'")
    def wait_for_header_question(self, header_question_about_important):
        WebDriverWait(self.driver, 3).until(EC.visibility_of_element_located(header_question_about_important))
    
    @allure.step("метод прокрутки до раздела 'Вопросы о важном'")
    def scroll_to_element(self, header_question_about_important):
        element = self.driver.find_element(*header_question_about_important)
        self.driver.execute_script("arguments[0].scrollIntoView();", element)
    
    @allure.step("метод ожидания текста ответа на вопрос")
    def wait_for_text_question(self, text_inside_section):
        WebDriverWait(self.driver, 3).until(EC.visibility_of_element_located(text_inside_section))
    
    @allure.step("метод ожидания загрузки кнопки Яндекс")
    def wait_logo(self):
        WebDriverWait(self.driver, 5).until(EC.visibility_of_element_located(button_yandex))

    @allure.step("метод перехода на другую страницу")
    def transition_to_another_page(self):
        self.driver.switch_to.window(self.driver.window_handles[1])
    
    @allure.step("метод ожидания страницы Яндекс Дзен")
    def wait_page_yandexdzen(self):
        WebDriverWait(self.driver, 5).until(EC.url_contains("dzen.ru"))

