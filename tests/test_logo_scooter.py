import pytest
import allure
from Sprint_6.pages.page_object_main_page import *

@pytest.mark.usefixtures("driver")
class TestLogoScooter:
    
    @allure.title('Проверка перехода на главную страницу при клике на логотип Самокат')
    def test_click_logo_scooter(self):
             
        #"Переход на страницу регистрации"
        self.driver.get('https://qa-scooter.praktikum-services.ru/order')
        
        #Объект класса страницы
        logo_scooter = MainPageScooter(self.driver)

        #"Ожидание закгрузки логотипа"
        logo_scooter.wait_logo()
        
        #"Клик по кнопке 'Самокат' на главной странице"
        logo_scooter.click_on_button_logo_scooter()

        assert logo_scooter.current_url() == "https://qa-scooter.praktikum-services.ru/"


    
    
