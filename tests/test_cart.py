from pages.login_page import LoginPage
from pages.products_page import ProductsPage
from pages.cart_page import CartPage


def test_TC05_add_two_products_remove_one(
    page, app_url, standard_user, test_password
):
    login = LoginPage(page, app_url)
    login.open()
    login.login(standard_user, test_password)

    products = ProductsPage(page)
    products.expect_products_page()

    products.add_product_to_cart(
        "Sauce Labs Backpack"
    )
    products.add_product_to_cart(
        "Sauce Labs Bike Light"
    )

    products.expect_cart_badge(2)

    products.remove_product_from_cart(
        "Sauce Labs Bike Light"
    )

    products.expect_cart_badge(1)
    products.open_cart()

    cart = CartPage(page)
    cart.expect_item_count(1)

    assert cart.cart_items.locator(
        '[data-test="inventory-item-name"]'
    ).all_text_contents() == [
        "Sauce Labs Backpack"
    ]