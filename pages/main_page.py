from .base_page import BasePage
from locators.main_page_locators import *
import pages.signin_page
import allure
import data
from pathlib import Path

class MainPage(BasePage):
    
    @allure.step('Кликаем на кнопку Войти')
    def click_button_login_account(self):
        self.click(BUTTON_LOGIN_ACCOUNT)
        return pages.signin_page.SigninPage(self.driver)

    @allure.step('Проверяем наличие кнопки Выход')
    def is_exit_button_present(self):
        return bool(self.find_element(EXIT_BUTTON))
    
    @allure.step('Кликаем на кнопку создать рецепт')
    def click_button_create_recipe(self):
        self.click(BUTTON_CREATE_RECIPE)
        
    @allure.step('Заполняем поле Название рецепта')
    def fill_recipe_name(self, recipe_name):
        self.find_element(INPUT_RECIPE_NAME).send_keys(recipe_name)

    @allure.step('Заполняем поле Ингредиенты')
    def fill_ingredient_name(self, ingredient_name):
        self.find_element(INPUT_INGREDIENT_NAME).send_keys(ingredient_name)

    @allure.step('Кликаем на ингредиент')
    def click_button_select_ingredient(self):
        self.click(BUTTON_SELECT_INGREDIENT)

    @allure.step('Заполняем поле граммовка ингредиента')
    def fill_ingredient_quantity(self, ingredient_quantity):
        self.find_element(INPUT_INGREDIENT_QUANTITY).send_keys(ingredient_quantity)

    @allure.step('Кликаем на Добавить ингредиент')
    def click_button_add_ingredient(self):
        self.click(BUTTON_ADD_INGREDIENT)

    @allure.step('Заполняем поле Время приготовления')
    def fill_cooking_time(self, cooking_time):
        self.find_element(INPUT_COOKING_TIME).send_keys(cooking_time)

    @allure.step('Заполняем поле Описание рецепта')
    def fill_description(self, description):
        self.find_element(INPUT_DESCRIPTION).send_keys(description)

    @allure.step('Загружаем изображение для рецепта')
    def upload_recipe_image(self, image_path):
        self.find_element(UPLOAD_IMAGE_INPUT).send_keys(image_path)

    @allure.step('Скроллим к кнопке Создать рецепт')
    def scroll_to_create_recipe(self):
        self.scroll_to_element(BUTTON_CREATE)

    @allure.step('Заполняем форму создания рецепта')
    def fill_recipe(self):
        self.fill_recipe_name(data.recipe_name)
        self.fill_ingredient_name(data.ingredient_name)
        self.click_button_select_ingredient()
        self.fill_ingredient_quantity(data.ingredient_quantity)
        self.click_button_add_ingredient()
        self.fill_cooking_time(data.cooking_time)
        self.fill_description(data.description)
        self.upload_recipe_image(str(Path(__file__).parent.parent / "assets" / "test.jpg"))
        self.scroll_to_create_recipe()

    @allure.step('Кликаем на кнопку Создать рецепт')
    def click_button_create(self):
        self.click(BUTTON_CREATE)

    @allure.step('Проверяем наличие карточки рецепта')
    def is_recipe_card_present(self):
        return bool(self.find_element(RECIPE_CARD))
    
    @allure.step('Получаем название на карточке рецепта')
    def get_name_text(self):
        return self.get_text(RECIPE_NAME_TEXT)
    