import pytest

from pages.login_page import LoginPage
from pages.products_page import ProductsPage
from pages.cart_page import CartPage
from pages.checkout_page import CheckoutPage


@pytest.mark.parametrize(
    "first_name,last_name,postal_code,error",
    [
        (
            "",
            "Bai",
            "560001",
            "Error: First Name is required"
        ),
        (
            "Rakshitha",
            "",
            "560001",
            "Error: Last Name is required"
        ),
        (
            "Rakshitha",
            "Bai",
            "",
            "Error: Postal Code is required"
        ),
    ],
    ids=[
        "missing-first-name",
        "missing-last-name",
        "missing-postal-code",
    ],
)
def test_TC06_checkout_required_fields(
    page,
    app_url,
    standard_user,
    test_password,
    first_name,
    last_name,
    postal_code,
    error,
):
    login = LoginPage(page, app_url)
    login.open()
    login.login(standard_user, test_password)

    products = ProductsPage(page)
    products.add_product_to_cart(
        "Sauce Labs Backpack"
    )
    products.open_cart()

    cart = CartPage(page)
    cart.checkout()

    checkout = CheckoutPage(page)
    checkout.enter_customer_details(
        first_name, last_name, postal_code
    )
    checkout.continue_checkout()
    checkout.expect_error(error)


def test_TC07_checkout_total_and_cart_empty(
    page, app_url, standard_user, test_password
):
    login = LoginPage(page, app_url)
    login.open()
    login.login(standard_user, test_password)

    products = ProductsPage(page)
    products.add_product_to_cart(
        "Sauce Labs Backpack"
    )
    products.add_product_to_cart(
        "Sauce Labs Bike Light"
    )
    products.open_cart()

    cart = CartPage(page)
    cart.expect_item_count(2)
    cart.checkout()

    checkout = CheckoutPage(page)
    checkout.enter_customer_details(
        "Rakshitha", "Bai", "560001"
    )
    checkout.continue_checkout()

    item_total = checkout.get_item_total()
    tax = checkout.get_tax()
    total = checkout.get_total()

    assert round(item_total + tax, 2) == total, (
        f"Incorrect checkout total: "
        f"subtotal={item_total}, tax={tax}, total={total}"
    )

    checkout.finish_order()
    checkout.expect_order_complete()

    checkout.return_to_products()
    products.open_cart()

    cart = CartPage(page)
    cart.expect_item_count(0)