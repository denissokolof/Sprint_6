from selenium.webdriver.common.by import By
import allure
from Sprint_6.locators import *
from Sprint_6.pages.page_object_base_page import *
    
# Заказ самоката
class OrderScooter(BasePage):
    
    @allure.step("Клик по верхней кнопке 'Заказать' на главной странице")
    def click_on_top_button_order(self):
        self.click(top_button_order)

    @allure.step("Клик по нижней кнопке 'Заказать' на главной странице")
    def click_on_bottom_button_order(self):
        self.scroll_and_click(bottom_button_order)    
    
    @allure.step("Первая часть регистрации")
    def login_part_one(self, name, surname, address, metro, telephon):
    
        #Поле "Имя"
        self.click(name_input)
        self.find_element(name_input).send_keys(name)
        
        #Поле "Фамилия"
        self.click(surname_input)
        self.find_element(surname_input).send_keys(surname)
        
        #Поле "Адрес"
        self.click(adress_input)
        self.find_element(adress_input).send_keys(address)
        
        #Поле "Станция метро"
        self.click(metro_station_input)
        self.find_element(metro_station_input).send_keys(metro)

        option_locator = (By.XPATH, f"//div[contains(@class,'select-search__select')]//*[normalize-space()='{metro}']")
        self.wait_and_click(option_locator)

        #Поле "Телефон" 
        self.click(telephon_input)
        self.find_element(telephon_input).send_keys(telephon)

        #Клик по кнопке "Далее"
        self.click(next_button)
    
    @allure.step("Вторая часть регистрации")
    def login_part_two(self, data, comment):

        #Поле "Когда привезти самокат" 
        self.click(data_input)
        self.find_element(data_input).send_keys(data)
        
        #Поле "Срок аренды" 
        self.click(rent_input)
        self.click(time_rent_input)
        
        #Поле "Цвет самоката"
        self.click(color_scooter_input)
        
        #Поле "Комментарий для курьера"
        self.click(comment_input)
        self.find_element(comment_input).send_keys(comment)
        
        #Клик по кнопке "Заказать"
        self.click(button_order)
    
    @allure.step("Клик по нижней кнопке 'Заказать' на главной странице")
    def click_on_botton_consent(self):
        self.click(botton_consent)
    
    @allure.step("Текст заголовка 'Заказ оформлен'")
    def get_header_order_placed(self):
        return self.find_element(header_order_placed).text


