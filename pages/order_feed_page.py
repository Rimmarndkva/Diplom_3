from selenium.webdriver.common.by import By
from pages.base_page import BasePage
import allure

class OrderFeedLocators:

    TOTAL_ORDERS_COUNTER = (By.XPATH, ".//p[text()='Выполнено за все время:']/following-sibling::p[contains(@class, 'OrderFeed_number')]")
    TODAY_ORDERS_COUNTER = (By.XPATH, ".//p[text()='Выполнено за сегодня:']/following-sibling::p[contains(@class, 'OrderFeed_number')]")
    

    ORDERS_IN_PROGRESS_LIST = (By.XPATH, ".//ul[contains(@class, 'OrderFeed_orderListReady')]//li")

class OrderFeedPage(BasePage):

    @allure.step('Получение значения счетчика "Выполнено за все время"')
    def get_total_orders_counter(self):
        return self.get_text_from_element(OrderFeedLocators.TOTAL_ORDERS_COUNTER)

    @allure.step('Получение значения счетчика "Выполнено за сегодня"')
    def get_today_orders_counter(self):
        return self.get_text_from_element(OrderFeedLocators.TODAY_ORDERS_COUNTER)

    @allure.step('Получение номеров заказов из раздела "В работе"')
    def get_orders_in_progress(self):
    
        self.find_element_with_wait(OrderFeedLocators.ORDERS_IN_PROGRESS_LIST)
      
        elements = self.driver.find_elements(*OrderFeedLocators.ORDERS_IN_PROGRESS_LIST)
        return [element.text for element in elements]