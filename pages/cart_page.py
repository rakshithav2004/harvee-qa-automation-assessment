from playwright.sync_api import Page, expect

class CartPage:
    def __init__(self, page: Page):
        self.page = page

        self.cart_items = page.locator(
            '[data-test="inventory-item"]'
        )
        self.checkout_button = page.locator(
            '[data-test="checkout"]'
        )
        self.continue_shopping_button = page.locator(
            '[data-test="continue-shopping"]'
        )

    def expect_item_count(self, count: int):
        expect(self.cart_items).to_have_count(count)

    def checkout(self):
        self.checkout_button.click()

    def continue_shopping(self):
        self.continue_shopping_button.click()