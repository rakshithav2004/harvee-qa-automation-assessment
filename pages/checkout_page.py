from playwright.sync_api import Page, expect

class CheckoutPage:
    def __init__(self, page: Page):
        self.page = page

        self.first_name = page.locator(
            '[data-test="firstName"]'
        )
        self.last_name = page.locator(
            '[data-test="lastName"]'
        )
        self.postal_code = page.locator(
            '[data-test="postalCode"]'
        )
        self.continue_button = page.locator(
            '[data-test="continue"]'
        )
        self.cancel_button = page.locator(
            '[data-test="cancel"]'
        )
        self.error_message = page.locator(
            '[data-test="error"]'
        )

        self.item_total = page.locator(
            '[data-test="subtotal-label"]'
        )
        self.tax = page.locator(
            '[data-test="tax-label"]'
        )
        self.total = page.locator(
            '[data-test="total-label"]'
        )
        self.finish_button = page.locator(
            '[data-test="finish"]'
        )
        self.complete_header = page.locator(
            '[data-test="complete-header"]'
        )
        self.back_home_button = page.locator(
            '[data-test="back-to-products"]'
        )

    def enter_customer_details(
        self,
        first_name: str,
        last_name: str,
        postal_code: str
    ):
        self.first_name.fill(first_name)
        self.last_name.fill(last_name)
        self.postal_code.fill(postal_code)

    def continue_checkout(self):
        self.continue_button.click()

    def expect_error(self, message: str):
        expect(self.error_message).to_contain_text(message)

    def get_money_value(self, locator) -> float:
        text = locator.inner_text()
        return float(text.split("$")[-1])

    def get_item_total(self) -> float:
        return self.get_money_value(self.item_total)

    def get_tax(self) -> float:
        return self.get_money_value(self.tax)

    def get_total(self) -> float:
        return self.get_money_value(self.total)

    def finish_order(self):
        self.finish_button.click()

    def expect_order_complete(self):
        expect(self.complete_header).to_have_text(
            "Thank you for your order!"
        )

    def return_to_products(self):
        self.back_home_button.click()