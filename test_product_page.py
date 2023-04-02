import typing
import pytest
from pages.product_page import ProductPage


link: str = "http://selenium1py.pythonanywhere.com/catalogue/coders-at-work_207/?promo=offer{}"
urls = [pytest.param('bugged_link', marks=pytest.mark.xfail)
        if i == 7 else link.format(i) for i in range(10)]


@pytest.mark.parametrize('url', urls)
def test_guest_can_add_product_to_cart(browser, url) -> typing.NoReturn:
    page = ProductPage(browser, url)
    page.open()
    page.press_button_add_to_basket()
    page.solve_quiz_and_get_code()
    page.should_be_message_about_adding()
    page.should_be_message_basket_total()
