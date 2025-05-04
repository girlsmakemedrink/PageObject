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