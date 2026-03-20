import allure
import pytest
from pages.main_page import MainPage
from pages.order_feed_page import OrderFeedPage
from pages.login_page import LoginPage

class TestOrderFeed:

    @allure.title('Атомарные проверки: счетчики заказов и появление в разделе "В работе"')
    @pytest.mark.parametrize("check_type", ["total_counter", "today_counter", "in_progress"])
    def test_order_counters_and_progress(self, driver, create_user_api, check_type):
        main_page = MainPage(driver)
        feed_page = OrderFeedPage(driver)
        login_page = LoginPage(driver)
        
        email = create_user_api["email"]
        password = create_user_api["password"]
        
       
        main_page.go_to_site()
        main_page.click_order_feed_button()
        total_before = feed_page.get_total_orders_counter()
        today_before = feed_page.get_today_orders_counter()
        
    
        main_page.click_constructor_button()
        main_page.click_login_account_button()
        login_page.login(email, password)
        
    
        main_page.wait_for_load_main_page()
        main_page.drag_ingredient_to_basket()
        main_page.click_place_order_button()
        
     
        order_number = main_page.get_new_order_number()
        main_page.close_ingredient_modal()
        
     
        main_page.click_order_feed_button()
        total_after = feed_page.get_total_orders_counter()
        today_after = feed_page.get_today_orders_counter()
        orders_in_progress = feed_page.get_orders_in_progress()
        
       
        if check_type == "total_counter":
            with allure.step("Проверка увеличения счетчика за все время"):
                assert int(total_after) > int(total_before)
                
        elif check_type == "today_counter":
            with allure.step("Проверка увеличения счетчика за сегодня"):
                assert int(today_after) > int(today_before)
                
        elif check_type == "in_progress":
            with allure.step("Проверка появления номера заказа в списке 'В работе'"):
                assert str(int(order_number)) in orders_in_progress
