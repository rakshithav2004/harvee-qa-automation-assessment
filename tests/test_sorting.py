from pages.login_page import LoginPage
from pages.products_page import ProductsPage


def test_TC03_sort_price_low_to_high(
    page, app_url, standard_user, test_password
):
    login = LoginPage(page, app_url)
    login.open()
    login.login(standard_user, test_password)

    products = ProductsPage(page)
    products.expect_products_page()
    products.sort_by("lohi")

    actual_prices = products.get_product_prices()

    assert len(actual_prices) > 1
    assert actual_prices == sorted(actual_prices), (
        f"Prices are not ascending: {actual_prices}"
    )


def test_TC04_sort_price_high_to_low(
    page, app_url, standard_user, test_password
):
    login = LoginPage(page, app_url)
    login.open()
    login.login(standard_user, test_password)

    products = ProductsPage(page)
    products.expect_products_page()
    products.sort_by("hilo")

    actual_prices = products.get_product_prices()

    assert len(actual_prices) > 1
    assert actual_prices == sorted(
        actual_prices, reverse=True
    ), f"Prices are not descending: {actual_prices}"