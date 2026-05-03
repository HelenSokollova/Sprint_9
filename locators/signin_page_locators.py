from selenium.webdriver.common.by import By

BUTTON_CREATE_ACCOUNT = (By.XPATH, "//a[text()='Создать аккаунт']")

LOGIN_FORM = (By.TAG_NAME, "form")

INPUT_EMAIL_LOGIN = (By.XPATH, "//input[@name='email']")

INPUT_PASSWORD_LOGIN = (By.XPATH, "//input[@name='password']")

BUTTON_LOGIN_ACCOUNT = (By.XPATH, "//button[text()='Войти']")
