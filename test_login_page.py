from pages.login_page import LoginPage

LOGIN_LINK = "http://selenium1py.pythonanywhere.com"
LOGIN_PAGE = "http://selenium1py.pythonanywhere.com/ru/accounts/login/"

def test_guest_can_see_login_url(browser):
    page = LoginPage(browser, LOGIN_LINK)  # инициализируем Page Object, передаем в конструктор экземпляр драйвера и url адрес
    page.open()                      # открываем страницу
    page.should_be_login_url()       # выполняем метод страницы — проверяем урл страницы

def test_guest_should_see_login_form(browser):
    page = LoginPage(browser, LOGIN_PAGE)
    page.open()
    page.should_be_login_form()

def test_guest_should_see_register_form(browser):
    page = LoginPage(browser, LOGIN_PAGE)
    page.open()
    page.should_be_register_form()