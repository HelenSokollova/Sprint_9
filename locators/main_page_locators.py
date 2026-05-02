from selenium.webdriver.common.by import By

BUTTON_LOGIN_ACCOUNT = (By.XPATH, "//a[text()='Войти']")

EXIT_BUTTON = (By.XPATH, "//a[text()='Выход']")

BUTTON_CREATE_RECIPE = (By.XPATH, "//a[text()='Создать рецепт']")

INPUT_RECIPE_NAME = (By.XPATH, "//input[contains(@class, 'styles_inputField__3eqTj')]")

INPUT_INGREDIENT_NAME = (By.XPATH, "//input[contains(@class, 'styles_ingredientsInput')]")

BUTTON_SELECT_INGREDIENT = (By.XPATH, "//div[text()='повидло']")

INPUT_INGREDIENT_QUANTITY = (By.XPATH, "//input[contains(@class, 'styles_ingredientsAmountValue')]")

BUTTON_ADD_INGREDIENT = (By.XPATH, "//div[text()='Добавить ингредиент']")

INPUT_COOKING_TIME = (By.XPATH, "//label[contains(@class, 'styles_inputLabel__u_wTn') and contains(., 'Время приготовления')]//input")

INPUT_DESCRIPTION = (By.XPATH, "//textarea[contains(@class, 'styles_textareaField')]")

UPLOAD_IMAGE_INPUT = (By.XPATH, "//input[@type='file']")

BUTTON_CREATE = (By.XPATH, "//button[text()='Создать рецепт']")

RECIPE_CARD = (By.XPATH, "//div[contains(@class, 'styles_single-card__1yTTj')]")

RECIPE_NAME_TEXT = (By.XPATH, "//h1[contains(@class, 'styles_single-card__title')]")
