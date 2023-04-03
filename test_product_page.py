import pytest
import faker
from pages.product_page import ProductPage
from pages.basket_page import BasketPage
from pages.login_page import LoginPage


LINK: str = "http://selenium1py.pythonanywhere.com/catalogue/coders-at-work_207/"

@pytest.mark.login_user
class TestUserAddToBasketFromProductPage:
    @pytest.fixture(scope="function", autouse=True)
    def setup(self, browser):
        fake: faker = faker.Faker()
        email: str = fake.email()
        password: str = fake.password()
        self.login_page = LoginPage(browser, LINK)
        self.login_page.open()
        self.login_page.register_new_user(email=email, password=password)

    @pytest.mark.need_review
    def test_user_can_add_product_to_basket(self, browser):
        page: ProductPage = ProductPage(browser, LINK)
        page.press_button_add_to_basket()
        page.should_be_message_about_adding()
        page.should_be_message_basket_total()

    def test_user_cant_see_success_message(self, browser):
        page: ProductPage = ProductPage(browser, LINK)
        page.should_not_be_success_message()

@pytest.mark.need_review
def test_guest_cant_see_success_message(browser):
    page: ProductPage = ProductPage(browser, LINK)
    page.open()
    page.should_not_be_success_message()


@pytest.mark.xfail
def test_guest_cant_see_success_message_after_adding_product_to_basket(browser):
    page: ProductPage = ProductPage(browser, LINK)
    page.open()
    page.press_button_add_to_basket()
    page.solve_quiz_and_get_code()
    page.should_not_be_success_message()

@pytest.mark.xfail
def test_guest_can_add_product_to_basket(browser):
    page: ProductPage = ProductPage(browser, LINK)
    page.open()
    page.press_button_add_to_basket()
    page.should_be_message_about_adding()
    page.should_be_message_basket_total()


@pytest.mark.xfail
def test_message_disappeared_after_adding_product_to_basket(browser):
    page: ProductPage = ProductPage(browser, LINK)
    page.open()
    page.press_button_add_to_basket()
    page.solve_quiz_and_get_code()
    page.should_disappear_success_message()


def test_guest_should_see_login_link_on_product_page(browser):
    page: ProductPage = ProductPage(browser, LINK)
    page.open()
    page.should_be_login_link()

@pytest.mark.need_review
def test_guest_can_go_to_login_page_from_product_page(browser):
    page: ProductPage = ProductPage(browser, LINK)
    page.open()
    page.should_be_login_link()
    page.go_to_login_page()

@pytest.mark.need_review
def test_guest_cant_see_product_in_basket_opened_from_product_page(browser):
    page: BasketPage = BasketPage(browser, LINK)
    page.open()
    page.go_to_basket_page()
    page.should_basket_is_empty()


@pytest.mark.xfail
def test_guest_cant_not_see_product_in_basket_opened_from_product_page(browser):
    page: BasketPage = BasketPage(browser, LINK)
    page.open()
    page.go_to_basket_page()
    page.should_basket_is_not_empty()

