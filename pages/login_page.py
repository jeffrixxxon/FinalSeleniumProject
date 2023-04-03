from .base_page import BasePage
from .locators import LoginPageLocators


class LoginPage(BasePage):
    def should_be_login_page(self):
        self.should_be_login_url()
        self.should_be_login_form()
        self.should_be_register_form()

    def register_new_user(self, email: str, password: str):
        link = self.browser.current_url
        self.go_to_login_page()
        self.browser.find_element(*LoginPageLocators.EMAIL_FORM).send_keys(email)
        self.browser.find_element(*LoginPageLocators.PASSWORD_FORM).send_keys(password)
        self.browser.find_element(*LoginPageLocators.PASSWORD_CONFIRM_FORM).send_keys(password)
        self.browser.find_element(*LoginPageLocators.BUTTON_REGISTER).click()
        self.should_be_authorized_user()
        self.browser.get(link)

    def should_be_login_url(self):
        assert 'login' in self.browser.current_url, 'You are not on the registration page'

    def should_be_login_form(self):
        assert self.is_element_present(*LoginPageLocators.LOGIN_FORM), 'Login form missing'

    def should_be_register_form(self):
        assert self.is_element_present(*LoginPageLocators.REG_FORM), 'No registration form'
