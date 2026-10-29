import os
from pathlib import Path

import pytest
from dotenv import load_dotenv
from playwright.sync_api import Page

load_dotenv()

BASE_URL = os.getenv(
    "BASE_URL",
    "https://www.saucedemo.com"
)


@pytest.fixture
def app_url():
    return BASE_URL.rstrip("/")


@pytest.fixture
def standard_user():
    return os.getenv("STANDARD_USER", "standard_user")


@pytest.fixture
def locked_user():
    return os.getenv("LOCKED_USER", "locked_out_user")


@pytest.fixture
def test_password():
    return os.getenv("TEST_PASSWORD", "secret_sauce")


@pytest.hookimpl(hookwrapper=True)
def pytest_runtest_makereport(item, call):
    outcome = yield
    report = outcome.get_result()

    if report.when == "call" and report.failed:
        page = item.funcargs.get("page")

        if page is not None and not page.is_closed():
            screenshot_dir = Path("reports/screenshots")
            screenshot_dir.mkdir(
                parents=True,
                exist_ok=True
            )

            safe_name = "".join(
                c if c.isalnum() or c in "-_" else "_"
                for c in item.nodeid
            )

            screenshot_path = (
                screenshot_dir / f"{safe_name}.png"
            )

            try:
                page.screenshot(
                    path=str(screenshot_path),
                    full_page=True
                )
                print(
                    f"\nFailure screenshot: {screenshot_path}"
                )
            except Exception as exc:
                print(
                    f"\nCould not save screenshot: {exc}"
                )