from selenium.webdriver.common.by import By


class BasePageLocators:
    LOGIN_LINK: tuple = (By.CSS_SELECTOR, "#login_link")
    LOGIN_LINK_INVALID: tuple = (By.CSS_SELECTOR, "#login_link")


class BasketPageLocators:
    BASKET_POSITION: tuple = (By.CSS_SELECTOR, '.btn-group a')
    EMPTY_BASKET: tuple = (By.CSS_SELECTOR, '.total')


class MainPageLocators:
    LOGIN_LINK: tuple = (By.CSS_SELECTOR, "#login_link")


class LoginPageLocators:
    LOGIN_FORM: tuple = (By.CSS_SELECTOR, '[id="login_form"]')
    REG_FORM: tuple = (By.CSS_SELECTOR, '[id="register_form"]')


class ProductPageLocators:
    BUTTON_ADD_TO_BASKET: tuple = (By.CSS_SELECTOR, ".btn-add-to-basket")
    MESSAGE_ABOUT_ADDING: tuple = (By.CSS_SELECTOR, "div.alertinner strong")
    PRODUCT_NAME: tuple = (By.CSS_SELECTOR, ".product_main h1")
    MESSAGE_BASKET_TOTAL: tuple = (By.CSS_SELECTOR, ".alert-info .alertinner strong")
    PRODUCT_PRICE: tuple = (By.CSS_SELECTOR, ".product_main .price_color")

