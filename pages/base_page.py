from selenium.webdriver.support import expected_conditions
from selenium.webdriver.support.wait import WebDriverWait
import allure


class BasePage:
    def __init__(self, driver):
        self.driver = driver

    @allure.step('Открываем страницу')    
    def open_page(self, url):
        self.driver.get(url)

    @allure.step('Находим элемент')
    def find_element(self, locator):
        return WebDriverWait(self.driver, 10).until(expected_conditions.presence_of_element_located(locator))
    
    @allure.step('Кликаем по элементу')
    def click(self, locator):
        element = WebDriverWait(self.driver, 10).until(expected_conditions.element_to_be_clickable(locator))
        element.click()

    @allure.step('Вводим текст в поле')
    def send_keys(self, locator, text):
        element = self.find_element(locator)
        element.clear()
        element.send_keys(text)
    
    @allure.step('Скроллим к элементу')
    def scroll_to_element(self, locator):
        element = self.find_element(locator)
        self.driver.execute_script("arguments[0].scrollIntoView();", element)


    @allure.step('Получаем текущий URL')
    def get_current_url(self):
        return self.driver.current_url
    
        
    @allure.step('Ожидаем, что URL содержит текст "{text}"')
    def wait_url_contains(self, text):
        return WebDriverWait(self.driver, 10).until(expected_conditions.url_contains(text))
    
    @allure.step('Получаем текст элемента')
    def get_text(self, locator):
        element = self.find_element(locator)
        return element.text
    