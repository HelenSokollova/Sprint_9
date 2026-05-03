from pages.main_page import MainPage
from urls import TestUrls
import allure
import data


class TestSigninPage:
    @allure.title('Проверка успешного создания рецепта авторизованным пользователем')
    @allure.description('Проверяем корректное отображение карточки созданного рецепта')
    def test_create_recipe_success(self, driver, registered_user):
        main_page = MainPage(driver)
        main_page.open_page(TestUrls.main_page_url)
        signin_page = main_page.click_button_login_account()
        main_page_after_login = signin_page.login_user(registered_user)
        main_page_after_login.wait_url_contains(data.main_text)
        main_page_after_login.is_exit_button_present()
        main_page_after_login.click_button_create_recipe()
        main_page_after_login.fill_recipe()
        main_page_after_login.click_button_create()
        assert main_page_after_login.is_recipe_card_present()
        assert main_page_after_login.get_name_text()== data.recipe_name
