from Sprint_6.locators import *

questions_data = {
    "what_is_the_price": {
        "button": button_question_what_is_the_price,
        "text_locator": text_question_what_is_the_price,
        "expected": "Сутки — 400 рублей. Оплата курьеру — наличными или картой."
    },
    "how_many_scooters": {
        "button": button_question_several_scooters,
        "text_locator": text_question_several_scooters,
        "expected": (
            "Пока что у нас так: один заказ — один самокат. Если хотите покататься с друзьями, "
            "можете просто сделать несколько заказов — один за другим."
        )
    },
    "rental_time": {
        "button": button_question_rental_time,
        "text_locator": text_question_rental_time,
        "expected": (
            "Допустим, вы оформляете заказ на 8 мая. Мы привозим самокат 8 мая в течение дня. "
            "Отсчёт времени аренды начинается с момента, когда вы оплатите заказ курьеру. "
            "Если мы привезли самокат 8 мая в 20:30, суточная аренда закончится 9 мая в 20:30."
        )
    },
    "today_order": {
        "button": button_question_scooter_today,
        "text_locator": text_question_scooter_today,
        "expected": "Только начиная с завтрашнего дня. Но скоро станем расторопнее."
    },
    "extend_or_return": {
        "button": button_question_extend_order,
        "text_locator": text_question_extend_order,
        "expected": (
            "Пока что нет! Но если что-то срочное — всегда можно позвонить в поддержку по красивому номеру 1010."
        )
    },
    "charger": {
        "button": button_question_charging_scooter,
        "text_locator": text_question_charging_scooter,
        "expected": (
            "Самокат приезжает к вам с полной зарядкой. Этого хватает на восемь суток — даже если будете "
            "кататься без передышек и во сне. Зарядка не понадобится."
        )
    },
    "cancel_order": {
        "button": button_question_order_concellation,
        "text_locator": text_question_order_concellation,
        "expected": (
            "Да, пока самокат не привезли. Штрафа не будет, объяснительной записки тоже не попросим. "
            "Все же свои."
        )
    },
    "far_from_mkad": {
        "button": button_question_life_outside_Moscow,
        "text_locator": text_question_life_outside_Moscow,
        "expected": "Да, обязательно. Всем самокатов! И Москве, и Московской области."
    },
}