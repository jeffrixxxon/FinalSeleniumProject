from selenium.webdriver.common.by import By


class MainPageLocators:
    LOGIN_LINK: tuple = (By.CSS_SELECTOR, "#login_link")


class LoginPageLocators:
    LOGIN_FORM: tuple = (By.CSS_SELECTOR, '[id="login_form"]')
    REG_FORM: tuple = (By.CSS_SELECTOR, '[id="register_form"]')

