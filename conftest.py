import pytest
import requests
import string
import random
from selenium import webdriver
from selenium.webdriver.chrome.service import Service as ChromeService
from selenium.webdriver.firefox.service import Service as FirefoxService
from webdriver_manager.chrome import ChromeDriverManager
from webdriver_manager.firefox import GeckoDriverManager
from urls import BASE_URL

def generate_random_string(length=10):
    letters = string.ascii_lowercase
    return ''.join(random.choice(letters) for _ in range(length))

@pytest.fixture(params=['chrome', 'firefox'])
def driver(request):
    if request.param == 'chrome':
        service = ChromeService(ChromeDriverManager().install())
        driver = webdriver.Chrome(service=service)
    elif request.param == 'firefox':
        service = FirefoxService(GeckoDriverManager().install())
        driver = webdriver.Firefox(service=service)
        
    driver.maximize_window()
    yield driver
    driver.quit()

@pytest.fixture
def create_user_api():
    """Создает пользователя через API и возвращает его данные для авторизации"""
    email = f"test_{generate_random_string()}@yandex.ru"
    password = "Password123"
    
    requests.post(f"{BASE_URL}/api/auth/register",
          json={"email": email, "password": password, "name": "Test"})
    
    return {"email": email, "password": password}