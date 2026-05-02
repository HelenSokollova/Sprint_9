from .base_page import BasePage
import pages.signin_page
from locators.signup_page_locators import *
import allure

class SignupPage(BasePage):
    @allure.step('Заполняем поле Имя')
    def fill_name(self, name):
        self.find_element(INPUT_NAME).send_keys(name)

    @allure.step('Заполняем поле Фамилия')
    def fill_surname(self, surname):
        self.find_element(INPUT_SURNAME).send_keys(surname)

    @allure.step('Заполняем поле Имя пользователя')
    def fill_username(self, username):
        self.find_element(INPUT_USERNAME).send_keys(username)

    @allure.step('Заполняем поле Адрес электронной почты')
    def fill_email(self, email):
        self.find_element(INPUT_EMAIL).send_keys(email)

    @allure.step('Заполняем поле Пароль')
    def fill_password(self, password):
        self.find_element(INPUT_PASSWORD).send_keys(password)

    @allure.step('Кликаем на нижнюю кнопку Создать аккаунт')
    def click_button_create_account_down(self):
        self.click(BUTTON_CREATE_ACCOUNT_DOWN)

    def register_user(self, random_user_data):
        self.fill_name(random_user_data['name'])
        self.fill_surname(random_user_data['surname'])
        self.fill_username(random_user_data['username'])
        self.fill_email(random_user_data['email'])
        self.fill_password(random_user_data['password'])
        self.click_button_create_account_down()
        return pages.signin_page.SigninPage(self.driver)
    