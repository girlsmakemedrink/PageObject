from .base_page import BasePage
from .locators import LoginPageLocators
from .locators import MainPageLocators

class LoginPage(BasePage):
    def should_be_login_page(self):
        self.should_be_login_url()
        self.should_be_login_form()
        self.should_be_register_form()

    def should_be_login_url(self):
        login_link = self.browser.find_element(*MainPageLocators.LOGIN_LINK)
        assert login_link.is_displayed(), 'Login link is not displayed'
        assert login_link.is_enabled(), 'Login link is not clickable'

        login_link.click()
        assert '/login' in self.browser.current_url, 'No "login" substring in the URL'

    def should_be_login_form(self):
        assert self.is_element_present(*LoginPageLocators.LOGIN_EMAIL), '"Email" field not present in the login form'
        assert self.is_element_present(*LoginPageLocators.LOGIN_PASSWORD), '"Password" field not present in the login form'
        assert self.is_element_present(*LoginPageLocators.FORGOTTEN_PASSWORD), '"Forgot password" field not present in the login form'
        assert self.is_element_present(*LoginPageLocators.LOGIN_BUTTON), '"Login button" not present in the login form'

    def should_be_register_form(self):
        assert self.is_element_present(*LoginPageLocators.REGISTRATION_EMAIL), '"Email" field not present in the registration form'
        assert self.is_element_present(*LoginPageLocators.REGISTRATION_PASSWORD), '"Password" field not present in the registration form'
        assert self.is_element_present(*LoginPageLocators.REGISTRATION_CONFIRM_PASSWORD), '"Confirm password" field not present in the registration form'
        assert self.is_element_present(*LoginPageLocators.REGISTRATION_BUTTON), 'Registration button not present in the registration form'
