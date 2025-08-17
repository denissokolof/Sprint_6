from selenium.webdriver.common.by import By
import allure
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.wait import WebDriverWait
from Sprint_6.locators import *
    
# Заказ самоката
class OrderScooter:
    
    def __init__(self, driver):
        self.driver = driver
    
    @allure.step("Клик по верхней кнопке 'Заказать' на главной странице")
    def click_on_top_button_order(self):
        self.driver.find_element(*top_button_order).click()

    @allure.step("Клик по нижней кнопке 'Заказать' на главной странице")
    def click_on_bottom_button_order(self):
        element = self.driver.find_element(*bottom_button_order)
        self.driver.execute_script("arguments[0].scrollIntoView({block: 'center'});", element)   
        self.driver.find_element(*bottom_button_order).click()
    
    @allure.step("Первая часть регистрации")
    def login_part_one(self, name, surname, address, metro, telephon):
    
        #Поле "Имя"
        self.driver.find_element(*name_input).click()
        self.driver.find_element(*name_input).send_keys(name)
        
        #Поле "Фамилия"
        self.driver.find_element(*surname_input).click()
        self.driver.find_element(*surname_input).send_keys(surname)
        
        #Поле "Адрес"
        self.driver.find_element(*adress_input).click()
        self.driver.find_element(*adress_input).send_keys(address)
        
        #Поле "Станция метро"
        self.driver.find_element(*metro_station_input).click()
        self.driver.find_element(*metro_station_input).send_keys(metro)

        option_locator = (By.XPATH, f"//div[contains(@class,'select-search__select')]//*[normalize-space()='{metro}']")
        WebDriverWait(self.driver, 5).until(EC.element_to_be_clickable(option_locator)).click()

        #Поле "Телефон" 
        self.driver.find_element(*telephon_input).click()
        self.driver.find_element(*telephon_input).send_keys(telephon)

        #Клик по кнопке "Далее"
        self.driver.find_element(*next_button).click()
    
    @allure.step("Вторая часть регистрации")
    def login_part_two(self, data, comment):

        #Поле "Когда привезти самокат" 
        self.driver.find_element(*data_input).click()
        self.driver.find_element(*data_input).send_keys(data)
        
        #Поле "Срок аренды" 
        self.driver.find_element(*rent_input).click()
        self.driver.find_element(*time_rent_input).click()
        
        #Поле "Цвет самоката"
        self.driver.find_element(*color_scooter_input).click()
        
        #Поле "Комментарий для курьера"
        self.driver.find_element(*comment_input).click()
        self.driver.find_element(*comment_input).send_keys(comment)
        
        #Клик по кнопке "Заказать"
        self.driver.find_element(*button_order).click()
    
    @allure.step("Клик по нижней кнопке 'Заказать' на главной странице")
    def click_on_botton_consent(self):
        self.driver.find_element(*botton_consent).click()
    
    @allure.step("Текст заголовка 'Заказ оформлен'")
    def get_header_order_placed(self):
        return self.driver.find_element(*header_order_placed).text


