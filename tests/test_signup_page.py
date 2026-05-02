from pages.main_page import MainPage
from urls import TestUrls
import allure
import data


class TestSigninPage:
    @allure.title('Проверка перехода на главную страницу после успешной авторизации по кнопке Войти')
    @allure.description('Проверяем соответствие урла страницы, открывающейся по клику на кнопку Войти после заполнения формы авторизации, заданному урлу')
    def test_correct_button_login_account_click(self, driver, registered_user):
        main_page = MainPage(driver)
        main_page.open_page(TestUrls.main_page_url)
        signin_page = main_page.click_button_login_account()
        main_page_after_login = signin_page.login_user(registered_user)
        main_page_after_login.wait_url_contains(data.main_text)
        current_url = main_page.get_current_url()
        actual_url = TestUrls.main_page_url    
        assert current_url == actual_url
        assert main_page.is_exit_button_present()
