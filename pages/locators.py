from selenium.webdriver.common.by import By


class MainPageLocators:
    LOGIN_LINK = (By.CSS_SELECTOR, "#login_link")


class LoginPageLocators:
    PART_URL = "login"
    LOGIN_FORM = (By.ID, "login_form")
    REGISTER_FORM = (By.ID, "register_form")


class ProductPageLocators:
    BTN_ADD_TO_BUSKET = (By.CSS_SELECTOR, ".product_main form button.btn-add-to-basket")
    PRODUCT_NAME = (By.CSS_SELECTOR, ".product_main h1")
    PRODUCT_PRICE = (By.CSS_SELECTOR, ".product_main p.price_color")
    PRODUCT_DESCRIPTION = (By.CSS_SELECTOR, "#product_description+p")
    SUCCESS_MESSAGES = (By.CSS_SELECTOR, ".alertinner strong")

