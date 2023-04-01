import typing
from selenium import webdriver
from selenium.common.exceptions import NoSuchElementException
from selenium.webdriver.common.by import By


class BasePage:
    def __init__(self, browser: webdriver, url: str, timeout: int = 10):
        self.browser: webdriver = browser
        self.url: str = url
        self.browser.implicitly_wait(timeout)

    def open(self) -> typing.NoReturn:
        self.browser.get(self.url)

    def is_element_present(self, how: By, what: str):
        try:
            self.browser.find_element(how, what)
        except NoSuchElementException:
            return False
        else:
            return True
