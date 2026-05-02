from pages.signin_page import SigninPage
from urls import TestUrls
import allure
import data


class TestSigninPage:
    @allure.title('Проверка перехода на страницу авторизации по кнопке Создать аккаунт после заполнения формы регистрации')
    @allure.description('Проверяем соответствие урла страницы, открывающейся по клику на кнопку Создать аккаунт после заполнения формы регистрации, заданному урлу')
    def test_correct_button_create_account_click(self, driver,random_user_data):
        signin_page = SigninPage(driver)
        signin_page.open_page(TestUrls.base_url)
        signup_page = signin_page.click_button_create_account()
        signin_page_after = signup_page.register_user(random_user_data)
        signin_page_after.wait_url_contains(data.signin_text)
        current_url = signin_page_after.get_current_url()
        actual_url = TestUrls.base_url    
        assert current_url == actual_url
        assert signin_page_after.is_login_form_present()
        