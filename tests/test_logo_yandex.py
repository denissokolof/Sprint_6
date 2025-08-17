import pytest
import allure
from Sprint_6.pages.page_object_main_page import *
from Sprint_6.pages.page_object_base_page import *

@pytest.mark.usefixtures("driver")
class TestLogoYandex:

    @allure.title('Проверка перехода на главную страницу при клике на логотип Яндекс')
    def test_click_logo_yandex(self):
             
        #"Переход на страницу тестового приложения"
        self.driver.get('https://qa-scooter.praktikum-services.ru')

        #Объект класса страницы
        logo_yandex = MainPageScooter(self.driver)
        base_logo_yandex = BasePage(self.driver)
        
        #"Ожидание закгрузки логотипа"
        base_logo_yandex.wait_logo()

        #"Клик по кнопке 'Яндекс' на главной странице"
        logo_yandex.click_on_button_logo_yandex()

        #"Переход на другую вкладку"
        base_logo_yandex.transition_to_another_page()

        #"Ожидание загрузки страницы 'Яндекс Дзен'"
        base_logo_yandex.wait_page_yandexdzen()

        assert "dzen.ru" in self.driver.current_url


