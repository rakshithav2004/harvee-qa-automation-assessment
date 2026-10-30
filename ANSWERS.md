# Harvee Technologies – QA Automation Tester Assessment

**Name:** Rakshitha Bai V  
**Role:** QA Automation Tester

# Section A – Test Design and Automation

## A1. Manual Test Cases

### Assumptions and Preconditions

I am using the SauceDemo website for testing. I assume the website is accessible, the test accounts are available, and the product inventory is loaded correctly.

- Use the standard user for successful login and shopping workflows.
- Use the locked-out user to validate login failure handling.
- Start each test from a known application state to avoid interference from previous tests.
- Use valid product details and checkout information where required.
- Verify both the displayed results and the application's actual behavior.

### Manual Test Cases

| ID | Test Scenario | Steps | Expected Result | Priority |
|---|---|---|---|---|
| TC01 | Standard user login | Enter valid standard-user credentials and click Login. | Login succeeds and the user is redirected to the Products page. | P1 |
| TC02 | Locked-out user login | Enter the locked-out user's credentials and click Login. | Login is denied and an appropriate error message is displayed. | P1 |
| TC03 | Invalid password | Enter a valid username with an incorrect password and click Login. | Login fails, and the user remains on the login page with an error message. | P1 |
| TC04 | Empty login fields | Leave both fields empty and click Login. | Login is prevented and the required-field validation message is displayed. | P1 |
| TC05 | Product details | Log in and inspect the product list. | Product names, images, prices, and action buttons are displayed correctly. | P1 |
| TC06 | Sort prices low to high | Select the price low-to-high option and inspect product prices. | Products are displayed in ascending order of price. | P1 |
| TC07 | Sort prices high to low | Select the price high-to-low option and inspect product prices. | Products are displayed in descending order of price. | P1 |
| TC08 | Sort product names alphabetically | Select the A-to-Z option and inspect product names. | Product names are displayed in alphabetical order. | P2 |
| TC09 | Add one product | Click Add to Cart for one product. | The cart badge displays one item, and the selected product is added to the cart. | P1 |
| TC10 | Add two products | Add two different products to the cart. | The cart badge displays two items, and both products are present in the cart. | P1 |
| TC11 | Remove a product | Add a product to the cart and click Remove. | The product is removed, and the cart badge updates accordingly. | P1 |
| TC12 | Remove an item from the cart | Add two products, open the cart, and remove one product. | The removed product disappears, and only the remaining product is displayed. | P1 |
| TC13 | Empty cart | Open the cart without adding any products. | The cart displays no products and does not show incorrect item details. | P2 |
| TC14 | Continue shopping | Open the cart and click Continue Shopping. | The user returns to the Products page, and the existing cart state is preserved. | P2 |
| TC15 | Checkout with valid details | Add a product, open the cart, click Checkout, enter valid customer details, and continue. | The user reaches the checkout overview page. | P1 |
| TC16 | Missing first name | Start checkout, leave the first-name field empty, and click Continue. | Checkout is blocked and a first-name validation message is displayed. | P1 |
| TC17 | Missing last name | Start checkout, leave the last-name field empty, and click Continue. | Checkout is blocked and a last-name validation message is displayed. | P1 |
| TC18 | Missing postal code | Start checkout, leave the postal-code field empty, and click Continue. | Checkout is blocked and a postal-code validation message is displayed. | P1 |
| TC19 | Verify order total | Add products, proceed to the overview page, and compare item prices, subtotal, tax, and total. | The subtotal matches the sum of item prices, and the total equals subtotal plus tax. | P1 |
| TC20 | Complete an order | Complete checkout using valid details and click Finish. | The order is completed, and the confirmation page displays the expected success message. | P1 |
| TC21 | Cart after checkout | Complete an order and return to the Products page. | The completed order's items are no longer present in the active cart. | P2 |
| TC22 | Access inventory after logout | Log in, log out, and attempt to open the inventory URL directly. | The protected page is not accessible without authentication, and the user is redirected appropriately. | P1 |
| TC23 | Responsive layout | Open the website at desktop and mobile-sized viewports. | Important content remains visible, and controls are usable without disruptive layout issues. | P2 |
| TC24 | Keyboard navigation | Navigate through the login page, product list, cart, and checkout using the keyboard. | Interactive controls are keyboard-accessible, focus is visible, and supported actions can be completed without a mouse. | P2 |
| TC25 | Session handling | Log in, log out, and attempt to revisit a protected page using browser navigation or a direct URL. | The application prevents access to protected content after logout and requires authentication again. | P1 |

**Priority guide:**
- **P1 – High:** Core functionality or a failure that could prevent users from logging in, shopping, or completing checkout.
- **P2 – Medium:** Important usability, navigation, or secondary functionality that should be tested but is generally less critical to the primary purchase flow.

*Note: These are proposed test priorities. Actual priority should also consider business impact and the severity of any defect discovered.*

### Exploratory Testing – 15 Minutes

**Objective:** Identify unexpected behavior that could affect a customer's ability to browse products, manage a cart, and complete checkout.

I would divide the exploratory session into three focused areas:

- **First 3 minutes – Product listing:** Inspect product details and change sorting options. Check for incorrect ordering, missing images, or inconsistent product information.
- **Next 4 minutes – Cart operations:** Add and remove products, navigate between the Products and Cart pages, and verify that the cart badge matches the actual cart contents.
- **Next 5 minutes – Checkout:** Complete the checkout flow, test missing required fields, and verify the subtotal, tax, and final total.
- **Final 3 minutes – Session and retesting:** Check access after logout, repeat suspicious behavior, and record reproducible issues.

I would focus on incorrect sorting, cart counts that do not update, missing validation messages, incorrect totals, and unauthorized access to protected pages.

For each issue identified, I would document the reproduction steps, expected result, actual result, and supporting screenshots or logs where useful. These are potential areas to investigate, not confirmed defects until the behavior has been reproduced and verified.

### Test Strategy

I would prioritize login, product sorting, cart operations, and checkout because failures in these areas can prevent customers from completing a purchase.

My approach would include:
1. **Positive testing:** Verify successful login, product selection, cart operations, and order completion.
2. **Negative testing:** Validate invalid login credentials, empty fields, and missing checkout information.
3. **Regression testing:** Re-run existing tests after changes to confirm that previously working functionality remains stable.
4. **Usability testing:** Manually inspect keyboard navigation and responsive behavior at different viewport sizes.
5. **Automation:** Use Python, Pytest, and Playwright to automate repeatable functional scenarios.
6. **Failure analysis:** Review assertions, error messages, screenshots, and execution reports before determining whether a failure is caused by the application, test data, or automation code.

I would use reusable page classes, independent test setup where practical, explicit assertions, and condition-based waits rather than fixed delays. This approach improves maintainability and helps reduce flaky tests.

### Automated Test Coverage

The following manual test scenarios have corresponding automated tests in my current suite:

| Manual Test Case | Automated Test |
|---|---|
| TC01 – Standard user login | `test_TC01_standard_user_login` |
| TC02 – Locked-out user login | `test_TC02_locked_user_login` |
| TC06 – Sort prices low to high | `test_TC03_sort_price_low_to_high` |
| TC07 – Sort prices high to low | `test_TC04_sort_price_high_to_low` |
| TC10–TC12 – Add and remove cart items | `test_TC05_add_two_products_remove_one` |
| TC16–TC18 – Required checkout fields | `test_TC06_checkout_required_fields` |
| TC19–TC21 – Checkout total and cart state | `test_TC07_checkout_total_and_cart_empty` |
| TC22 – Access inventory without authentication | `test_TC08_products_page_requires_login` |

The checkout validation test uses parameterization to cover the three missing-field scenarios: first name, last name, and postal code.

The remaining manual test cases can be automated incrementally as the suite grows. I would prioritize additional automation based on business risk, test repeatability, and regression value.

Automation coverage should be reported according to what each test actually verifies. For example, the automated checkout test should only be considered to cover order completion or post-checkout cart behavior if its assertions explicitly validate those outcomes.

---

# Section B – Test Analysis and Communication

## B1. Reviewing AI-Generated Test Code

I would not use AI-generated test code without reviewing it first. Even if a test runs successfully, it may not verify the complete requirement or detect important defects.

### Problems in the supplied test

1. **Hard-coded URL:** The application URL should come from environment variables or configuration so the test can run against different environments.
2. **Hard-coded credentials:** Usernames and passwords should be read from environment variables rather than embedded in the test.
3. **Generic Add to Cart selector:** A selector such as `text=Add to cart` may match the wrong product button. The test should identify the intended product card and its button.
4. **Fixed sleep:** A fixed delay makes tests slower and can still fail when the application responds slowly. Playwright should wait for the relevant element or page state.
5. **Incomplete sorting verification:** Checking only one price does not confirm that the entire product list is correctly sorted. The test should collect all prices and compare them in numeric order.
6. **Weak total assertion:** `expect(total).toBeTruthy()` only checks that a value exists. It does not verify that the total equals the subtotal plus tax.
7. **Incomplete checkout flow:** The test should continue through the Finish action if completing an order is part of the requirement.
8. **Missing confirmation check:** The test should verify that the order confirmation is displayed.
9. **Missing cart verification:** It should check the active cart after checkout if the expected behavior is that the cart becomes empty.
10. **Limited failure evidence:** Screenshots and test reports should help identify what failed.
11. **Test independence:** The test should establish its own starting state rather than depend on another test.
12. **Maintainability:** Reusable page objects or helper methods should be used for common interactions and locators.

### Corrected Playwright test

Since my assessment project uses Python, Pytest, and Playwright, I would implement the test in Python. The following example illustrates the verification logic for product sorting, checkout totals, and order completion.

import os
import re
from decimal import Decimal

from playwright.sync_api import Page, expect

def test_checkout_total_and_cart_empty(page: Page):
    base_url = os.environ["BASE_URL"]
    username = os.environ["STANDARD_USER"]
    password = os.environ["TEST_PASSWORD"]

    # Open the application and log in.
    page.goto(base_url)
    page.locator('[data-test="username"]').fill(username)
    page.locator('[data-test="password"]').fill(password)
    page.locator('[data-test="login-button"]').click()

    expect(page).to_have_url(re.compile(r".*/inventory\.html"))
    expect(page.locator(".inventory_item")).not_to_have_count(0)

    # Add two products using their individual product cards.
    product_cards = page.locator(".inventory_item")
    product_cards.nth(0).locator("button").click()
    product_cards.nth(1).locator("button").click()

    # Verify the cart badge and contents.
    expect(page.locator(".shopping_cart_badge")).to_have_text("2")
    page.locator(".shopping_cart_link").click()
    expect(page.locator(".cart_item")).to_have_count(2)

    # Start checkout.
    page.locator('[data-test="checkout"]').click()
    page.locator('[data-test="firstName"]').fill("Test")
    page.locator('[data-test="lastName"]').fill("User")
    page.locator('[data-test="postalCode"]').fill("560001")
    page.locator('[data-test="continue"]').click()

    # Verify the order overview.
    expect(page.locator(".summary_subtotal_label")).to_be_visible()
    expect(page.locator(".summary_tax_label")).to_be_visible()
    expect(page.locator(".summary_total_label")).to_be_visible()

    subtotal_text = page.locator(
        ".summary_subtotal_label"
    ).inner_text()
    tax_text = page.locator(
        ".summary_tax_label"
    ).inner_text()
    total_text = page.locator(
        ".summary_total_label"
    ).inner_text()

    subtotal = Decimal(subtotal_text.split("$")[-1])
    tax = Decimal(tax_text.split("$")[-1])
    total = Decimal(total_text.split("$")[-1])

    assert total == subtotal + tax, (
        f"Expected total {subtotal + tax}, "
        f"but found {total}"
    )

    # Complete checkout and verify confirmation.
    page.locator('[data-test="finish"]').click()
    expect(page.locator(".complete-header")).to_be_visible()
    expect(page.locator(".complete-header")).to_contain_text(
        "Thank you"
    )

    # Return to the products page and verify the active cart is empty.
    page.locator('[data-test="back-to-products"]').click()
    expect(page.locator(".shopping_cart_badge")).to_have_count(0)

### How I would validate the corrected test

I would run the test against the actual application and verify that the selectors match the page. I would confirm that the test fails if the total is incorrect, the order confirmation is missing, or the cart still contains items after checkout. I would also check the failure screenshot and execution report if an assertion fails.

This example demonstrates the intended checks; before using it in the submitted project, I would align the selectors, configuration, and page-object methods with the existing repository. I would also use the project's existing fixtures and page objects where available rather than duplicate their setup.

## B2. Evaluating an AI-Generated Test-Case Feature

I would evaluate an AI feature that generates test cases from a short requirement. Although it can save time, I would review the generated cases before using them.

| Check | How I would assess it | Scoring method |
|---|---|---|
| Requirement accuracy | Compare each test's expected result with the given requirement. | 0 = Incorrect, 1 = Partly correct, 2 = Correct |
| Coverage | Check for positive, negative, boundary, and relevant security scenarios. | 0 = Major gaps, 1 = Some gaps, 2 = Good coverage |
| Unsupported assumptions | Check whether the output invents rules that were not provided. | 0 = Major inventions, 1 = Minor assumptions, 2 = No unsupported rules |
| Usability and structure | Check whether the cases are clear, non-duplicated, and follow the required format. | 0 = Difficult to use, 1 = Needs edits, 2 = Ready for review |

**Scoring:** The maximum score is 8.

- **7–8:** Promising output, but human review is still required.
- **4–6:** Needs revision.
- **0–3:** Requires substantial rework.

I would test the feature using several requirements, including login validation, product sorting, and checkout. I would compare its output against manually reviewed test cases and record the scores. I would also check whether repeated runs produce consistent results. The score helps compare outputs, but it does not replace human review.

## B3. Bug Report — Product Price Sorting

**Bug ID:** BUG-003  
**Title:** Products are not sorted correctly by price, from low to high  
**Environment:** SauceDemo web application  
**Release:** 4.2.0  
**Severity:** Major  
**Priority:** P1  

### Preconditions
- The user can log in successfully.
- The products page displays multiple products with different prices.

### Steps to Reproduce
1. Open the SauceDemo application.
2. Log in using a valid account.
3. Navigate to the products page.
4. Select **Price (low to high)** from the sorting dropdown.
5. Observe the displayed product prices.

### Expected Result
Products should appear in ascending numerical order, with the lowest-priced product first and the highest-priced product last.

### Actual Result
The product priced at **$29.99** appears before the product priced at **$15.99**, violating ascending price order.

### Reproducibility
The issue occurs on every test run.

### Impact
Users may have difficulty finding the lowest-priced products, reducing confidence in the sorting feature.

### Evidence
Capture a screenshot of the products page after selecting **Price (low to high)**, showing the incorrect order.

### Recommendation
Investigate the sorting implementation and verify that prices are compared numerically rather than as strings. Retest ascending and descending sorting after the fix, including products with different prices.

## B4. Release Decision

I would recommend **holding the release until the sorting defect is assessed and the intermittent checkout failure is investigated**.

The sorting defect produces an incorrect order, which directly affects users trying to find the lowest-priced products. The checkout test also fails intermittently, so I would investigate whether this is a test stability issue or an actual application defect.

Before making the release decision, I would:

1. Reproduce the sorting issue and confirm its impact.
2. Investigate the checkout failure using logs, screenshots, and test reports.
3. Rerun the checkout test to identify whether the failure is caused by timing, test data, environment instability, or an application issue.
4. Run relevant regression tests after any fix.
5. Share the findings, risks, and test results with the QA lead and release manager.

If the sorting issue affects a core requirement and remains unresolved, I would recommend delaying the release. If the issue is understood, its impact is acceptable, and the authorized release stakeholders approve the risk, a release may proceed with documented risks and a follow-up plan.

I would not treat a passing rerun alone as proof that the checkout issue is resolved.

---

## Section C – Investigation and Experience

## C1. Checkout Failure Investigation

If checkout starts failing for some users, I would first assess the impact and investigate whether the issue is related to the application, test environment, or specific user data.

### Investigation Steps

1. **Confirm the issue:** Identify affected users, when the failures started, the frequency, and the exact checkout step where they occur.
2. **Reproduce the failure:** Test with affected and unaffected accounts using the same steps, browsers, and test data where possible.
3. **Collect evidence:** Review application logs, API responses, browser console errors, screenshots, and automated test reports.
4. **Check recent changes:** Investigate recent deployments, configuration changes, and database or API changes that could affect checkout.
5. **Isolate the cause:** Verify customer information validation, cart contents, price calculations, payment responses, and session handling.
6. **Verify the fix:** Once the suspected cause is addressed, rerun the failing test and relevant checkout regression tests.
7. **Communicate findings:** Share the impact, evidence, suspected root cause, and current status with the development and QA teams.

### Possible Root Causes

- Incorrect handling of customer information.
- API failures or unexpected responses.
- Session or authentication issues.
- Incorrect cart totals or tax calculations.
- Browser-specific problems or unstable test data.

### Conclusion

I would prioritize the issue based on its impact on real users and whether it blocks order completion. I would avoid assuming the failure is caused by flaky automation until the evidence supports that conclusion. After the fix, I would verify the affected scenarios and run regression tests before recommending closure.

## C2. A Real Issue I Worked On at Vonage

During my time as a Software Engineering Trainee at Vonage, I worked on Java and Spring Boot REST APIs used in telecom billing workflows. One issue I worked on involved inconsistent validation and error handling across API flows, which made some invalid requests harder to troubleshoot.

I reviewed the existing validation logic and helped improve the handling of common validation rules and error responses. I then tested valid requests alongside invalid inputs, including missing or inconsistent data, to check that errors were handled consistently without affecting valid requests.

I also reviewed the resulting errors and regression-test results to verify the changes. This work contributed to a reduction of approximately 10–15% in validation-related API failures. It also made errors easier to interpret and helped make debugging more consistent.

The main lesson I learned was to reproduce an issue, compare the expected and actual behavior, investigate the relevant logic, and verify the change with regression tests. I would apply the same structured approach to a production issue by first assessing its impact, reviewing logs and requests, identifying the cause, validating the fix, and communicating the results clearly.

---

## Test Execution Summary

During my local test run, Pytest reported 10 passed tests and one warning in approximately 18 seconds. This confirms that the tests passed in that particular run. It does not mean every manual test case has been executed or that the application is completely defect-free.