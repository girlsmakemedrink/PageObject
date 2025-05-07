import pytest

from pages.basket_page import BasketPage
from pages.product_page import ProductPage

# @pytest.mark.parametrize('promo', ["promo=offer0", "promo=offer1", "promo=offer2", "promo=offer3", "promo=offer4", "promo=offer5", "promo=offer6", "promo=offer7", "promo=offer8", "promo=offer9"])
def test_guest_can_add_product_to_basket(browser):
    # PRODUCT_PAGE = f"http://selenium1py.pythonanywhere.com/catalogue/coders-at-work_207/?{promo}/"
    PRODUCT_PAGE = 'http://selenium1py.pythonanywhere.com/catalogue/coders-at-work_207/?promo=offer0/'
    page = ProductPage(browser, PRODUCT_PAGE)  # инициализируем Page Object, передаем в конструктор экземпляр драйвера и url адрес

    page.open()                                # открываем страницу
    page.add_product_to_basket()               # выполняем метод страницы


def test_guest_cant_see_success_message(browser):
    PRODUCT_PAGE = 'http://selenium1py.pythonanywhere.com/catalogue/coders-at-work_207/?promo=offer1/'
    page = ProductPage(browser, PRODUCT_PAGE)  # инициализируем Page Object, передаем в конструктор экземпляр драйвера и url адрес

    page.open()
    page.should_not_be_success_message()

def test_guest_can_go_to_login_page_from_product_page(browser):
    link = "http://selenium1py.pythonanywhere.com/en-gb/catalogue/the-city-and-the-stars_95/"
    page = ProductPage(browser, link)
    page.open()
    page.go_to_login_page()

def test_guest_should_see_login_link_on_product_page(browser):
    link = "http://selenium1py.pythonanywhere.com/en-gb/catalogue/the-city-and-the-stars_95/"
    page = ProductPage(browser, link)
    page.open()
    page.should_be_login_link()

@pytest.mark.xfail
def test_message_disappeared_after_adding_product_to_basket(browser):
    PRODUCT_PAGE = 'http://selenium1py.pythonanywhere.com/catalogue/coders-at-work_207/?promo=offer1/'
    page = ProductPage(browser, PRODUCT_PAGE)
    page.open()
    page.message_should_disappear()

def test_guest_cant_see_product_in_basket_opened_from_product_page(browser):
    PRODUCT_PAGE = 'http://selenium1py.pythonanywhere.com/catalogue/coders-at-work_207/?promo=offer1/'
    page = ProductPage(browser, PRODUCT_PAGE)
    page.open()
    page.go_in_basket()
    basket_page = BasketPage(browser, browser.current_url)
    basket_page.guest_cant_see_product_in_basket()