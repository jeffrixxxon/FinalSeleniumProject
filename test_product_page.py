import typing
import pytest
from pages.product_page import ProductPage


url: str = "http://selenium1py.pythonanywhere.com/catalogue/coders-at-work_207/?promo=offer0"
#urls = [pytest.param('bugged_link', marks=pytest.mark.xfail)
#        if i == 7 else link.format(i) for i in range(1)]


def test_guest_can_add_product_to_cart(browser) -> typing.NoReturn:
    page = ProductPage(browser, url)
    page.open()
    page.press_button_add_to_basket()
    page.solve_quiz_and_get_code()
    page.should_be_message_about_adding()
    page.should_be_message_basket_total()

@pytest.mark.xfail
def test_guest_cant_see_success_message_after_adding_product_to_basket(browser):
    page = ProductPage(browser, url)
    page.open()
    page.press_button_add_to_basket()
    page.solve_quiz_and_get_code()
    page.should_not_be_success_message()


def test_guest_cant_see_success_message(browser):
    page = ProductPage(browser, url)
    page.open()
    page.should_not_be_success_message()


@pytest.mark.xfail
def test_message_disappeared_after_adding_product_to_basket(browser):
    page = ProductPage(browser, url)
    page.open()
    page.press_button_add_to_basket()
    page.solve_quiz_and_get_code()
    page.should_disappear_success_message()
