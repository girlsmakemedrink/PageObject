import time

from .base_page import BasePage
from .locators import ProductPageLocators, BasePageLocators, BasketLocators
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

class ProductPage(BasePage):

    def add_product_to_basket(self):
       add_to_basket_button = self.browser.find_element(*ProductPageLocators.ADD_TO_BASKET_BUTTON)

       assert self.is_element_present(*ProductPageLocators.ADD_TO_BASKET_BUTTON), 'Add to basket button not found'
       add_to_basket_button.click()
       self.solve_quiz_and_get_code()

       assert len(ProductPageLocators.MESSAGES) == 2, 'Should be 2 messages'

       assert WebDriverWait(self.browser, 10).until(
           EC.visibility_of_element_located(ProductPageLocators.CLOSE_BUTTON)
       ), 'CLOSE_BUTTON not found'

       assert WebDriverWait(self.browser, 10).until(
           EC.visibility_of_element_located(BasePageLocators.VIEW_BASKET_BUTTON)
       ), 'VIEW_BASKET_BUTTON not found'

       assert WebDriverWait(self.browser, 10).until(
           EC.visibility_of_element_located(ProductPageLocators.BUY_BUTTON)
       ), 'BUY_BUTTON not found'

       assert WebDriverWait(self.browser,10).until(
           EC.visibility_of_element_located(ProductPageLocators.PRODUCT_PRICE_IN_MESSAGE)
       ), 'MESSAGE_BASKET_PRICE not found'

       product_name = self.browser.find_element(*ProductPageLocators.PRODUCT_NAME).text
       product_name_in_message = self.browser.find_element(*ProductPageLocators.PRODUCT_NAME_IN_MESSAGE).text
       product_price = self.browser.find_element(*ProductPageLocators.PRODUCT_PRICE).text
       product_price_in_message = self.browser.find_element(*ProductPageLocators.PRODUCT_PRICE_IN_MESSAGE).text

       assert product_name == product_name_in_message, "Product names don't match"
       assert product_price == product_price_in_message, "Product prices don't match"

       # time.sleep(555)

       see_basket_button = self.browser.find_element(*BasePageLocators.VIEW_BASKET_BUTTON)
       see_basket_button.click()

       assert WebDriverWait(self.browser, 5).until(
           EC.visibility_of_element_located(BasketLocators.PRODUCT_NAME_IN_BASKET)
       ), 'PRODUCT_NAME_IN_BASKET not found'

       product_name_in_basket = self.browser.find_element(*BasketLocators.PRODUCT_NAME_IN_BASKET).text
       product_price_in_basket = self.browser.find_element(*BasketLocators.PRODUCT_PRICE_IN_BASKET).text

       assert product_name == product_name_in_basket, "Product names does not match"
       assert product_name_in_message == product_name_in_basket, "Product names don't match"
       assert product_price == product_price_in_basket, 'Prices does not match'

       expected_value_of_products = '1'
       actual_value_of_products = self.browser.find_element(*BasketLocators.PRODUCT_QUANTITY).get_attribute('value')

       assert expected_value_of_products == actual_value_of_products, 'Value of products does not match'

    def should_not_be_success_message(self):
       add_to_basket_button = self.browser.find_element(*ProductPageLocators.ADD_TO_BASKET_BUTTON)
       add_to_basket_button.click()

       alert = self.browser.switch_to.alert
       alert.dismiss()
       alert.accept()

       assert self.is_not_element_present(*ProductPageLocators.MESSAGE_ADD), 'MESSAGE_ADD did not appear'
       assert self.is_not_element_present(*ProductPageLocators.MESSAGE_BASKET), 'MESSAGE_BASKET did not appear'
       assert self.is_not_element_present(*ProductPageLocators.MESSAGE_OFFER), 'MESSAGE_OFFER did not appear'

    def message_should_disappear(self):
       add_to_basket_button = self.browser.find_element(*ProductPageLocators.ADD_TO_BASKET_BUTTON)
       add_to_basket_button.click()
       self.solve_quiz_and_get_code()

       assert self.is_disappeared(*ProductPageLocators.MESSAGE_ADD), \
          'MESSAGE_ADD did not disappeared'
