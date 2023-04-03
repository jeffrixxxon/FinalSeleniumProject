from typing import NoReturn
from .base_page import BasePage
from .locators import BasketPageLocators


class BasketPage(BasePage):
    def should_basket_is_empty(self) -> NoReturn:
        assert self.is_not_element_present(*BasketPageLocators.EMPTY_BASKET), (
            'Cart is not empty, but should'
        )

    def should_basket_is_not_empty(self) -> NoReturn:
        assert self.is_element_present(*BasketPageLocators.EMPTY_BASKET), (
            'Cart is empty, but should'
        )
