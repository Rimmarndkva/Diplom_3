from selenium.webdriver.common.by import By
from pages.base_page import BasePage
import allure

class MainPageLocators:
 
    CONSTRUCTOR_LINK = (By.XPATH, ".//p[text()='Конструктор']")
    ORDER_FEED_LINK = (By.XPATH, ".//p[text()='Лента Заказов']")
    
    FIRST_INGREDIENT = (By.XPATH, ".//a[contains(@class, 'BurgerIngredient_ingredient')]")
    FIRST_INGREDIENT_COUNTER = (By.XPATH, ".//a[contains(@class, 'BurgerIngredient_ingredient')]//p[contains(@class, 'counter_counter__num')]")
    CONSTRUCTOR_BASKET = (By.XPATH, ".//section[contains(@class, 'BurgerConstructor_basket')]")
    
    MODAL_HEADER = (By.XPATH, ".//h2[text()='Детали ингредиента']")
    MODAL_CLOSE_BUTTON = (By.XPATH, ".//section[contains(@class, 'Modal_modal_')]//button")

   
    LOGIN_ACCOUNT_BUTTON = (By.XPATH, ".//button[text()='Войти в аккаунт']")
    PLACE_ORDER_BUTTON = (By.XPATH, ".//button[text()='Оформить заказ']")
    ORDER_MODAL_NUMBER = (By.XPATH, ".//section[contains(@class, 'Modal_modal_')]//h2")


class MainPage(BasePage):
    
    @allure.step('Клик по кнопке "Конструктор"')
    def click_constructor_button(self):
        self.click_to_element(MainPageLocators.CONSTRUCTOR_LINK)

    @allure.step('Клик по кнопке "Лента Заказов"')
    def click_order_feed_button(self):
        self.click_to_element(MainPageLocators.ORDER_FEED_LINK)

    @allure.step('Клик по первому ингредиенту')
    def click_first_ingredient(self):
        self.click_to_element(MainPageLocators.FIRST_INGREDIENT)

    @allure.step('Проверка, что появилось окно "Детали ингредиента"')
    def get_ingredient_modal_header_text(self):
        return self.get_text_from_element(MainPageLocators.MODAL_HEADER)

    @allure.step('Клик по крестику закрытия модального окна')
    def close_ingredient_modal(self):
        self.click_to_element(MainPageLocators.MODAL_CLOSE_BUTTON)

    @allure.step('Добавление первого ингредиента в корзину (drag-and-drop)')
    def drag_ingredient_to_basket(self):
        self.drag_and_drop(MainPageLocators.FIRST_INGREDIENT, MainPageLocators.CONSTRUCTOR_BASKET)

    @allure.step('Получение значения счетчика первого ингредиента')
    def get_first_ingredient_counter(self):
        return self.get_text_from_element(MainPageLocators.FIRST_INGREDIENT_COUNTER)

    @allure.step('Проверка, что окно "Детали ингредиента" закрылось')
    def check_ingredient_modal_is_closed(self):
        return self.wait_for_element_to_disappear(MainPageLocators.MODAL_HEADER)


    @allure.step('Клик по кнопке "Войти в аккаунт" на главной')
    def click_login_account_button(self):
        self.click_to_element(MainPageLocators.LOGIN_ACCOUNT_BUTTON)

    @allure.step('Ожидание загрузки кнопки "Оформить заказ"')
    def wait_for_load_main_page(self):
        self.find_element_with_wait(MainPageLocators.PLACE_ORDER_BUTTON)

    @allure.step('Клик по кнопке "Оформить заказ"')
    def click_place_order_button(self):
        self.click_to_element(MainPageLocators.PLACE_ORDER_BUTTON)

    @allure.step('Ожидание и получение номера сформированного заказа')
    def get_new_order_number(self):
        self.wait_for_text_to_change(MainPageLocators.ORDER_MODAL_NUMBER, "9999", 15)
        return self.get_text_from_element(MainPageLocators.ORDER_MODAL_NUMBER)