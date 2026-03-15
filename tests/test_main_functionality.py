import allure
from pages.main_page import MainPage

class TestMainFunctionality:

    @allure.title('Переход по клику на "Лента заказов" и "Конструктор"')
    def test_navigation_menu(self, driver):
        main_page = MainPage(driver)
        main_page.go_to_site()
        
        main_page.click_order_feed_button()
        assert "feed" in driver.current_url
        
        main_page.click_constructor_button()
        assert driver.current_url == main_page.base_url + "/"

    @allure.title('Открытие модального окна с деталями ингредиента')
    def test_open_ingredient_modal(self, driver):
        main_page = MainPage(driver)
        main_page.go_to_site()
        

        main_page.click_first_ingredient()
      
        assert main_page.get_ingredient_modal_header_text() == "Детали ингредиента"

    @allure.title('Закрытие всплывающего окна кликом по крестику')
    def test_close_ingredient_modal(self, driver):
        main_page = MainPage(driver)
        main_page.go_to_site()
        
    
        main_page.click_first_ingredient()
        main_page.close_ingredient_modal()
        
        assert True

    @allure.title('Увеличение счетчика ингредиента при добавлении в заказ')
    def test_ingredient_counter_increases(self, driver):
        main_page = MainPage(driver)
        main_page.go_to_site()
        
        main_page.drag_ingredient_to_basket()
      
        counter_text = main_page.get_first_ingredient_counter()
        assert int(counter_text) > 0