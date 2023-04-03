import typing
from .locators import BasePageLocators, BasketPageLocators
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.common.exceptions import NoSuchElementException, TimeoutException


class BasePage:
    def __init__(self, browser: webdriver, url: str, timeout: int = 10):
        self.browser: webdriver = browser
        self.url: str = url
        self.browser.implicitly_wait(timeout)

    def go_to_basket_page(self) -> typing.NoReturn:
        try:
            link = self.browser.find_element(*BasketPageLocators.BASKET_POSITION)
            link.click()
        except NoSuchElementException:
            assert False, 'NoSuchElementException: element is missing from the page'
        else:
            assert 'basket' in self.browser.current_url, 'You are not on the basket page'

    def go_to_login_page(self) -> typing.NoReturn:
        try:
            link = self.browser.find_element(*BasePageLocators.LOGIN_LINK_INVALID)
            link.click()
        except NoSuchElementException:
            assert False, 'NoSuchElementException: element is missing from the page'
        else:
            assert 'login' in self.browser.current_url, 'You are not on the login page'

    def should_be_login_link(self) -> typing.NoReturn:
        assert self.is_element_present(*BasePageLocators.LOGIN_LINK), "Login link is not presented"

    def open(self) -> typing.NoReturn:
        self.browser.get(self.url)

    def is_element_present(self, how: By, what: str) -> bool:
        try:
            self.browser.find_element(how, what)
        except NoSuchElementException:
            return False
        else:
            return True

    def is_not_element_present(self, how, what, timeout=4) -> bool:
        try:
            WebDriverWait(self.browser, timeout).until(EC.presence_of_element_located((how, what)))
        except TimeoutException:
            return True
        return False

    def is_disappeared(self, how, what, timeout=4) -> bool:
        try:
            WebDriverWait(self.browser, timeout, poll_frequency=1, ignored_exceptions=[TimeoutException]
                          ).until_not(EC.presence_of_element_located((how, what)))
        except TimeoutException:
            return False
        return True

