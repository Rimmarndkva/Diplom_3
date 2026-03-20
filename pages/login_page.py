from selenium.webdriver.common.by import By
from pages.base_page import BasePage
import allure

class LoginPageLocators:
    EMAIL_INPUT = (By.XPATH, ".//input[@type='text']")
    PASS_INPUT = (By.XPATH, ".//input[@type='password']")
    LOGIN_SUBMIT_BUTTON = (By.XPATH, ".//button[text()='Войти']")

class LoginPage(BasePage):
    
    @allure.step('Ввод email при авторизации')
    def set_email(self, email):
        self.set_text_to_element(LoginPageLocators.EMAIL_INPUT, email)

    @allure.step('Ввод пароля при авторизации')
    def set_password(self, password):
        self.set_text_to_element(LoginPageLocators.PASS_INPUT, password)

    @allure.step('Клик по кнопке "Войти"')
    def click_login_submit_button(self):
        self.click_to_element(LoginPageLocators.LOGIN_SUBMIT_BUTTON)

    @allure.step('Заполнение формы авторизации и вход')
    def login(self, email, password):
        self.set_email(email)
        self.set_password(password)
        self.click_login_submit_button()