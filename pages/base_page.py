from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver import ActionChains

class BasePage:
    def __init__(self, driver):
        self.driver = driver
      
        self.base_url = "https://stellarburgers.education-services.ru"

    def go_to_site(self):
        """Открывает главную страницу сайта"""
        return self.driver.get(self.base_url)

    def find_element_with_wait(self, locator, timeout=10):
        """Ждет, пока элемент появится в DOM, и возвращает его"""
        return WebDriverWait(self.driver, timeout).until(
            EC.presence_of_element_located(locator),
            message=f"Не смогли найти элемент по локатору {locator}"
        )

    def click_to_element(self, locator, timeout=10):
        """Ждет, пока элемент станет кликабельным, и кликает по нему через JS"""
        element = WebDriverWait(self.driver, timeout).until(
            EC.element_to_be_clickable(locator),
            message=f"Элемент не кликабелен по локатору {locator}"
        )
        # Выполняем клик через встроенный JavaScript (решает проблему перекрытия элементов)
        self.driver.execute_script("arguments[0].click();", element)

    def get_text_from_element(self, locator, timeout=10):
        """Ждет элемент и забирает из него текст"""
        element = self.find_element_with_wait(locator, timeout)
        return element.text

    def drag_and_drop(self, source_locator, target_locator, timeout=10):
        """Берет элемент (source) и перетаскивает его в корзину (target) с микропаузами"""
        source_element = self.find_element_with_wait(source_locator, timeout)
        target_element = self.find_element_with_wait(target_locator, timeout)
    
        ActionChains(self.driver)\
            .click_and_hold(source_element)\
            .pause(0.5)\
            .move_to_element(target_element)\
            .pause(0.5)\
            .release()\
            .perform()
