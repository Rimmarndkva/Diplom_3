import allure
import requests
import string
import random
from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait
from pages.main_page import MainPage
from pages.order_feed_page import OrderFeedPage
from pages.base_page import BasePage

def generate_random_string(length=10):
    letters = string.ascii_lowercase
    return ''.join(random.choice(letters) for _ in range(length))

class TestOrderFeed:

    LOGIN_BUTTON = (By.XPATH, ".//button[text()='Войти в аккаунт']")
    LOGIN_EMAIL_INPUT = (By.XPATH, ".//fieldset[1]//input")
    LOGIN_PASS_INPUT = (By.XPATH, ".//fieldset[2]//input")
    LOGIN_SUBMIT = (By.XPATH, ".//button[text()='Войти']")
    PLACE_ORDER_BUTTON = (By.XPATH, ".//button[text()='Оформить заказ']")
    ORDER_MODAL_NUMBER = (By.XPATH, ".//section[contains(@class, 'Modal_modal_')]//h2")
    MODAL_CLOSE = (By.XPATH, ".//section[contains(@class, 'Modal_modal_')]//button")

    @allure.title('Увеличение счетчиков и появление заказа в разделе "В работе"')
    def test_order_counters_and_progress(self, driver):
        base = BasePage(driver)
        main_page = MainPage(driver)
        feed_page = OrderFeedPage(driver)
        
        # 1. Хитрость: регистрируем юзера через API, чтобы быстро получить аккаунт
        email = f"test_{generate_random_string()}@yandex.ru"
        password = "Password123"
        requests.post("https://stellarburgers.education-services.ru/api/auth/register",
              json={"email": email, "password": password, "name": "Test"})
        
     
        main_page.go_to_site()
        main_page.click_order_feed_button()
        total_before = feed_page.get_total_orders_counter()
        today_before = feed_page.get_today_orders_counter()
        

        main_page.click_constructor_button()
        base.click_to_element(self.LOGIN_BUTTON)
        base.find_element_with_wait(self.LOGIN_EMAIL_INPUT).send_keys(email)
        base.find_element_with_wait(self.LOGIN_PASS_INPUT).send_keys(password)
        base.click_to_element(self.LOGIN_SUBMIT)
        
      
        base.find_element_with_wait(self.PLACE_ORDER_BUTTON)
        main_page.drag_ingredient_to_basket()
        base.click_to_element(self.PLACE_ORDER_BUTTON)
        
  
        WebDriverWait(driver, 15).until(
            lambda d: d.find_element(*self.ORDER_MODAL_NUMBER).text != "9999"
        )
        order_number = base.get_text_from_element(self.ORDER_MODAL_NUMBER)
        base.click_to_element(self.MODAL_CLOSE)
        

        main_page.click_order_feed_button()
        total_after = feed_page.get_total_orders_counter()
        today_after = feed_page.get_today_orders_counter()
        
        assert int(total_after) > int(total_before)
        assert int(today_after) > int(today_before)

        orders_in_progress = feed_page.get_orders_in_progress()

        assert str(int(order_number)) in orders_in_progress