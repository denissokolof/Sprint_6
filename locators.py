from selenium.webdriver.common.by import By

#Локаторы Яндекс Самокат вопросы о важном

header_question_about_important = (By.XPATH, "//div[@id= 'accordion__heading-0']") #Заголовок "Вопросы о важном"


button_question_what_is_the_price = (By.XPATH, "//div[@id= 'accordion__heading-0']")  #Кнопка "Сколько это стоит? И как оплатить?"

text_question_what_is_the_price = (By.ID, "accordion__panel-0") #Текст ответа "Сколько это стоит? И как оплатить?"


button_question_several_scooters = (By.XPATH, "//div[@id= 'accordion__heading-1']") #Кнопка "Хочу сразу несколько самокатов! Так можно?"

text_question_several_scooters = (By.ID, "accordion__panel-1") #Текст ответа "Хочу сразу несколько самокатов! Так можно?"


button_question_rental_time = (By.XPATH, "//div[@id= 'accordion__heading-2']") #Кнопка "Как рассчитывается время аренды?"

text_question_rental_time = (By.ID, "accordion__panel-2") #Текст ответа "Как рассчитывается время аренды?"


button_question_scooter_today = (By.XPATH, "//div[@id= 'accordion__heading-3']") #Кнопка "Можно ли заказать самокат прямо на сегодня?"

text_question_scooter_today = (By.ID, "accordion__panel-3") #Текст ответа "Можно ли заказать самокат прямо на сегодня?"


button_question_extend_order = (By.XPATH, "//div[@id= 'accordion__heading-4']") #Кнопка "Можно ли продлить заказ или вернуть самокат раньше?"

text_question_extend_order = (By.ID, "accordion__panel-4") #Текст ответа "Можно ли продлить заказ или вернуть самокат раньше?"


button_question_charging_scooter = (By.XPATH, "//div[@id= 'accordion__heading-5']") #Кнопка "Вы привозите зарядку вместе с самокатом?"

text_question_charging_scooter = (By.ID, "accordion__panel-5") #Текст ответа "Вы привозите зарядку вместе с самокатом?"


button_question_order_concellation = (By.XPATH, "//div[@id= 'accordion__heading-6']") #Кнопка "Можно ли отменить заказ?"

text_question_order_concellation = (By.ID, "accordion__panel-6") #Текст ответа "Можно ли отменить заказ?"


button_question_life_outside_Moscow = (By.XPATH, "//div[@id= 'accordion__heading-7']") #Кнопка "Я жизу за МКАДом, привезёте?"

text_question_life_outside_Moscow = (By.ID, "accordion__panel-7") #Текст ответа "Я жизу за МКАДом, привезёте?"

#Локаторы главной страницы Яндекс Самокат

top_button_order = (By.CLASS_NAME, "Button_Button__ra12g") #Верхняя кнопка "Заказать" на странице

bottom_button_order = (By.XPATH, "//div[@class = 'Home_FinishButton__1_cWm']/button[text()='Заказать']") #Нижняя кнопка "Заказать" на странице

button_yandex = (By.XPATH, "//a[contains(@class, 'Header_LogoYandex__3TSOI')]") #Кнопка "Yandex" 

button_scooter = (By.XPATH, "//a[contains(@class, 'Header_LogoScooter__3lsAR')]") #Кнопка "Самокат" 

#Локаторы раздела "Для кого самокат"

name_input = (By.XPATH, "//div/input[@placeholder= '* Имя']") #Поле "Имя" 

surname_input = (By.XPATH, "//div/input[@placeholder= '* Фамилия']") #Поле "Фамилия" 

adress_input = (By.XPATH, "//div/input[@placeholder= '* Адрес: куда привезти заказ']") #Поле "Адрес"

metro_station_input = (By.XPATH, "//div/input[@placeholder= '* Станция метро']") #Поле "Станция метро"



telephon_input = (By.XPATH, "//div/input[@placeholder= '* Телефон: на него позвонит курьер']") #Поле "Телефон" 

next_button = (By.XPATH, "//div/button[text()='Далее']") #Кнопка "Далее" 

#Локаторы раздела "Про аренду"

data_input = (By.XPATH, "//div/input[@placeholder= '* Когда привезти самокат']") #Поле "Когда привезти самокат" 

rent_input = (By.CLASS_NAME, "Dropdown-arrow") #Поле "Срок аренды" 

time_rent_input = (By.XPATH, "//div/div[text()='сутки']") #Период"Срок аренды" 

color_scooter_input = (By.XPATH, "//input[@id='black']") #Поле "Цвет самоката"

comment_input = (By.XPATH, "//div/input[@placeholder= 'Комментарий для курьера']") #Поле "Комментарий для курьера" 

button_order = (By.XPATH, "//div[@class = 'Order_Buttons__1xGrp']/button[text()='Заказать']" ) #Кнопка "Заказать" в разделе "Про аренду"


#Локаторы раздела "Хотите оформить заказ?"

botton_consent = (By.XPATH, "//button[text()='Да']")

#Локаторы раздела "Заказ оформлен"

header_order_placed = (By.XPATH, "//div[@class = 'Order_ModalHeader__3FDaJ']") #Заголовок "Заказ оформлен"

