from selenium.webdriver.common.by import By


class MainPageLocators:
    LOGIN_LINK: tuple = (By.CSS_SELECTOR, "#login_link")


class LoginPageLocators:
    LOGIN_FORM: tuple = (By.CSS_SELECTOR, '[id="login_form"]')
    REG_FORM: tuple = (By.CSS_SELECTOR, '[id="register_form"]')


class ProductPageLocators:
    BUTTON_ADD_TO_BASKET = (By.CSS_SELECTOR, ".btn-add-to-basket")
    MESSAGE_ABOUT_ADDING = (By.CSS_SELECTOR, "div.alertinner strong")
    PRODUCT_NAME = (By.CSS_SELECTOR, ".product_main h1")
    MESSAGE_BASKET_TOTAL = (By.CSS_SELECTOR, ".alert-info .alertinner strong")
    PRODUCT_PRICE = (By.CSS_SELECTOR, ".product_main .price_color")

