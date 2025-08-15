from selenium import webdriver
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import pytest
import allure
from Sprint_6.pages.page_object_main_page import *

# класс с автотестом
class TestLogoYandex:

    driver = None

    @classmethod
    def setup_class(cls):
        #Драйвер для браузера
        cls.driver = webdriver.Firefox()

    @allure.title('Проверка перехода на главную страницу при клике на логотип Яндекс')
    def test_click_logo_yandex(self):
             
        #Переход на страницу тестового приложения
        self.driver.get('https://qa-scooter.praktikum-services.ru')

        #Объект класса страницы
        logo_yandex = MainPageScooter(self.driver)
        
        # Ожидание закгрузки логотипа
        logo_yandex.wait_logo()

        #Клик по кнопке "Яндекс" на главной странице
        logo_yandex.click_on_button_logo_yandex()

        #Переход на другую вкладку
        self.driver.switch_to.window(self.driver.window_handles[1])

        #Ожидание закгрузки страницы "Яндекс Дзен"
        WebDriverWait(self.driver, 5).until(EC.url_contains("dzen.ru"))

        assert "dzen.ru" in self.driver.current_url
    
    @classmethod
    def teardown_class(cls):
        # Закрой браузер
        cls.driver.quit()
