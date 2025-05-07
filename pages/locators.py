class BasePageLocators():
    LOGIN_LINK = ("css selector", "#login_link")
    LOGIN_LINK_INVALID = ("css selector", "#login_link_inc")

class MainPageLocators():
    LOGIN_LINK = ("css selector", "#login_link")

class LoginPageLocators():
    LOGIN_URL = ("css selector", "#login_url")

    LOGIN_EMAIL = ("css selector", "#id_login-username")
    LOGIN_PASSWORD = ("css selector", "#id_login-password")
    LOGIN_BUTTON = ("xpath", "//button[@value='Log In']")
    FORGOTTEN_PASSWORD = ("xpath", "//a[contains(@href, '/password-reset/')]")

    REGISTRATION_EMAIL = ("css selector", "#id_registration-email")
    REGISTRATION_PASSWORD = ("css selector", "#id_registration-password1")
    REGISTRATION_CONFIRM_PASSWORD = ("css selector", "#id_registration-password2")
    REGISTRATION_BUTTON = ("xpath", "//button[@name='registration_submit']")

class ProductPageLocators():
    ADD_TO_BASKET_BUTTON = ("xpath", "//button[@class='btn btn-lg btn-primary btn-add-to-basket']")
    SEE_BASKET_BUTTON = ("xpath", "(//a[contains(@href, '/basket/')])[4]")
    BUY_BUTTON = ("xpath", "(//a[contains(@href, '/checkout/')])[2]")
    CLOSE_BUTTON = ("xpath", "//div/a[contains(@class, 'close')]")

    MESSAGES = ("xpath", "//div[@id='messages']")

    MESSAGE_ADD = ("xpath", "(//div[@class ='alertinner '])[1]")
    MESSAGE_OFFER = ("xpath", "(//div[@class ='alertinner '])[2]")
    MESSAGE_BASKET = ("xpath", "(//div[@class ='alertinner '])[3]")

    PRODUCT_PRICE = ("xpath", "//p[@class ='price_color']")
    PRODUCT_PRICE_IN_MESSAGE = ("xpath", "//div[@class='alertinner ']/p/strong")
    PRODUCT_PRICE_IN_BASKET = ("xpath", "//p[@class='price_color align-right']")

    PRODUCT_NAME = ("xpath", "//h1")
    PRODUCT_NAME_IN_MESSAGE = ("xpath", "(//div[@class='alertinner ']/strong)[1]")
    PRODUCT_NAME_IN_BASKET = ("xpath", "//div[@class='col-sm-4']/h3/a")

    REMOVE_BUTTON_IN_BASKET = ("xpath", "//a[@data-behaviours='remove']")
    PRODUCT_QUANTITY = ("xpath", "//input[@name='form-0-quantity']")
