from playwright.sync_api import expect

from pages.login_page import LoginPage
from pages.products_page import ProductsPage


def test_TC01_standard_user_login(
    page, app_url, standard_user, test_password
):
    login = LoginPage(page, app_url)
    login.open()
    login.login(standard_user, test_password)

    products = ProductsPage(page)
    products.expect_products_page()


def test_TC02_locked_user_login(
    page, app_url, locked_user, test_password
):
    login = LoginPage(page, app_url)
    login.open()
    login.login(locked_user, test_password)

    login.expect_login_error(
        "Sorry, this user has been locked out."
    )