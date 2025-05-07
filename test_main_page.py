from pages.basket_page import BasketPage
from pages.main_page import MainPage

MAIN_PAGE_LINK = "http://selenium1py.pythonanywhere.com"

def test_guest_can_go_to_login_page(browser):
    page = MainPage(browser, MAIN_PAGE_LINK)   # инициализируем Page Object, передаем в конструктор экземпляр драйвера и url адрес
    page.open()                      # открываем страницу
    page.go_to_login_page()          # выполняем метод страницы — переходим на страницу логина

def test_guest_should_see_login_link(browser):
    page = MainPage(browser, MAIN_PAGE_LINK)
    page.open()
    page.should_be_login_link()

def test_guest_cant_see_product_in_basket_opened_from_main_page(browser):
    page = MainPage(browser, MAIN_PAGE_LINK)
    page.open()
    page.go_in_basket()
    basket_page = BasketPage(browser, browser.current_url)
    basket_page.guest_cant_see_product_in_basket()
