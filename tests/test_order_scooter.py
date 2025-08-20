import pytest
import allure
from Sprint_6.pages.page_object_order_scooter import *

@pytest.mark.usefixtures("driver")
class TestOrderScooter:
    
    @allure.title('Проверка заказа самоката через кнопку "Заказать" в шапке сайта')
    def test_order_scooter_top_button(self):
             
        #"перешли на страницу тестового приложения"
        self.driver.get('https://qa-scooter.praktikum-services.ru')

        # создай объект класса страницы
        order_scooter = OrderScooter(self.driver)

        #"Клик по верхней кнопке 'Заказать' на главной странице"
        order_scooter.click_on_top_button_order()
        
        #"Первая часть регистрации"
        order_scooter.login_part_one("Денис", "Соколов", "Советская", "Черкизовская", "89103575888")
        
        #"Вторая часть регистрации"
        order_scooter.login_part_two("09.02.2025", "Всем самокат!")

        #"Клик по кнопке 'Да' в разделе хотите оформить заказ"
        order_scooter.click_on_botton_consent()

        header_resalt = order_scooter.get_header_order_placed()

        assert "Заказ оформлен" in header_resalt

    @allure.title('Проверка заказа самоката через кнопку "Заказать" на главной странице')
    def test_order_scooter_bottom_button(self):
             
        #"перешли на страницу тестового приложения"
        self.driver.get('https://qa-scooter.praktikum-services.ru')

        # создай объект класса страницы
        order_scooter = OrderScooter(self.driver)

        #"Клик по нижней кнопке 'Заказать' на главной странице"
        order_scooter.click_on_bottom_button_order()
        
        #"Первая часть регистрации"
        order_scooter.login_part_one("Иван", "Иванов", "Фрунзе", "Комсомольская", "89103573333")
        
        #"Вторая часть регистрации"
        order_scooter.login_part_two("09.03.2025", "Всем штраф!")

        #"Клик по кнопке 'Да' в разделе хотите оформить заказ"
        order_scooter.click_on_botton_consent()

        header_resalt = order_scooter.get_header_order_placed()

        assert "Заказ оформлен" in header_resalt


