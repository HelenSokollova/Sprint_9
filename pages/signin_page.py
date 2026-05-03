from .base_page import BasePage
import pages.signup_page
from pages.main_page import MainPage
from locators.signin_page_locators import *
import allure

class SigninPage(BasePage):
    @allure.step('Кликаем на кнопку Создать аккаунт')
    def click_button_create_account(self):
        self.click(BUTTON_CREATE_ACCOUNT)
        return pages.signup_page.SignupPage(self.driver)
    
    @allure.step('Проверяем наличие формы авторизации')
    def is_login_form_present(self):
        return bool(self.find_element(LOGIN_FORM))
    
    @allure.step('Заполняем поле Электронная почта')
    def fill_email(self, email):
        self.find_element(INPUT_EMAIL_LOGIN).send_keys(email)

    @allure.step('Заполняем поле Пароль')
    def fill_password(self, password):
        self.find_element(INPUT_PASSWORD_LOGIN).send_keys(password)

    @allure.step('Кликаем на нижнюю кнопку Войти')
    def click_button_login_account(self):
        self.click(BUTTON_LOGIN_ACCOUNT)

    def login_user(self, random_user_data):
        self.fill_email(random_user_data['username'])
        self.fill_password(random_user_data['password'])
        self.click_button_login_account()
        return MainPage(self.driver)
    