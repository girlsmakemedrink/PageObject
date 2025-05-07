from PageObject.pages.base_page import BasePage
from .locators import BasketLocators

class BasketPage(BasePage):

    def guest_cant_see_product_in_basket(self):

        assert self.is_not_element_present(*BasketLocators.BASKET_ITEMS), 'basket items found'

        assert self.is_element_present(
            *BasketLocators.BASKET_IS_EMPTY_MESSAGE), 'message that basket is empty not found'

        empty_message = self.browser.find_element(*BasketLocators.BASKET_IS_EMPTY_MESSAGE).text
        assert empty_message == 'Your basket is empty. Continue shopping', 'Not correct basket message. Got "{}" '.format(
            empty_message)