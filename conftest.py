import pytest
import os
from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from helpers import generate_random_string
from pages.signup_page import SignupPage
from urls import TestUrls

@pytest.fixture(scope='function')
def driver():
    chrome_options = Options()
    chrome_options.add_argument('--no-sandbox')
    chrome_options.add_argument('--disable-dev-shm-usage')
    selenoid_url = os.getenv('SELENOID_URL', 'http://localhost:4444/wd/hub')
    
    driver = webdriver.Remote(
        command_executor=selenoid_url,
        options=chrome_options
    )
    yield driver
    driver.quit()
    
@pytest.fixture(scope='function')
def random_user_data():
    user_name = generate_random_string(10)
    user_surname = generate_random_string(10)
    user_username = generate_random_string(10)
    user_email= f'{generate_random_string(10)}@gmail.com'
    user_password = generate_random_string(10)
       
    user_data = {
        "name": user_name,
        "surname": user_surname,
        "username": user_username,
        "email": user_email,
        "password": user_password      
    }
    
    yield user_data 


@pytest.fixture(scope='function')
def registered_user(driver, random_user_data):
    signup_page = SignupPage(driver)
    signup_page.open_page(TestUrls.signup_url)
    signup_page.register_user(random_user_data)
        
    yield random_user_data
