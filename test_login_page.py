from PageObject.pages.main_page import MainPage
from pages.login_page import LoginPage

MAIN_PAGE = "http://selenium1py.pythonanywhere.com"
LOGIN_PAGE = "http://selenium1py.pythonanywhere.com/ru/accounts/login/"

def test_guest_can_go_to_login_page(browser):
    page = MainPage(browser, MAIN_PAGE)  # инициализируем Page Object, передаем в конструктор экземпляр драйвера и url адрес
    page.open()                      # открываем страницу
    page.go_to_login_page()       # выполняем метод страницы — проверяем урл страницы
    login_page = LoginPage(browser, browser.current_url)
    login_page.should_be_login_page()

def test_guest_should_see_login_form(browser):
    page = LoginPage(browser, LOGIN_PAGE)
    page.open()
    page.should_be_login_form()

def test_guest_should_see_register_form(browser):
    page = LoginPage(browser, LOGIN_PAGE)
    page.open()
    page.should_be_register_form()