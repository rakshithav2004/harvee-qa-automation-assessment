from playwright.sync_api import Page, expect

class LoginPage:
    def __init__(self, page: Page, base_url: str):
        self.page = page
        self.base_url = base_url

        self.username_input = page.locator("#user-name")
        self.password_input = page.locator("#password")
        self.login_button = page.locator("#login-button")
        self.error_message = page.locator(
            '[data-test="error"]'
        )

    def open(self):
        self.page.goto(self.base_url)

    def login(self, username: str, password: str):
        self.username_input.fill(username)
        self.password_input.fill(password)
        self.login_button.click()

    def expect_login_error(self, message: str):
        expect(self.error_message).to_contain_text(message)

    def expect_login_form(self):
        expect(self.username_input).to_be_visible()
        expect(self.password_input).to_be_visible()    