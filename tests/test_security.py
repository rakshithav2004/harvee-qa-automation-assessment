from playwright.sync_api import expect

from pages.login_page import LoginPage
from pages.products_page import ProductsPage


def test_TC08_products_page_requires_login(
    page, app_url, standard_user, test_password
):
    login = LoginPage(page, app_url)
    login.open()
    login.login(standard_user, test_password)

    products = ProductsPage(page)
    products.expect_products_page()
    products.logout()

    login.expect_login_form()

    page.goto(f"{app_url}/inventory.html")

    login.expect_login_form()