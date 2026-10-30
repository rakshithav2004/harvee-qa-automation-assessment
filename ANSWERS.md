# Harvee Technologies – QA Automation Tester Assessment

**Name:** Rakshitha Bai V  
**Role:** QA Automation Tester

# Section A – Test Design and Automation

## A1. Manual Test Cases

### Assumptions

I am using the SauceDemo website for testing. I assume the website is available, the test accounts are working as expected, and the product inventory contains the required products. I will use the standard user for normal testing and the locked-out user to check login failure scenarios.

### Manual Test Cases

| ID | Test scenario | Steps | Expected result |
|---|---|---|---|
| TC01 | Standard user login | Enter valid username and password and click Login. | The user should reach the Products page. |
| TC02 | Locked-out user login | Enter the locked-out user's credentials. | Login should fail and display an error message. |
| TC03 | Invalid password | Enter a valid username with an incorrect password. | The user should not be able to log in. |
| TC04 | Empty login fields | Click Login without entering any details. | The application should show an appropriate validation message. |
| TC05 | Check product details | Log in and look at the product list. | Product names, images, prices, and buttons should be displayed correctly. |
| TC06 | Sort price low to high | Select the low-to-high price option. | Products should appear from the lowest price to the highest. |
| TC07 | Sort price high to low | Select the high-to-low price option. | Products should appear from the highest price to the lowest. |
| TC08 | Sort names alphabetically | Select the A-to-Z sorting option. | Product names should appear in alphabetical order. |
| TC09 | Add one product | Add a product to the cart. | The cart badge should show one item. |
| TC10 | Add two products | Add two different products to the cart. | The cart badge should show two items. |
| TC11 | Remove a product | Add a product and then remove it. | The cart badge should update correctly. |
| TC12 | Remove an item from the cart | Add two products, open the cart, and remove one. | Only the remaining product should be displayed. |
| TC13 | Check an empty cart | Open the cart without adding any products. | The cart should be empty, with no incorrect product details. |
| TC14 | Continue shopping | Open the cart and click Continue Shopping. | The user should return to the Products page. |
| TC15 | Checkout with valid details | Add a product, open the cart, enter all required details, and continue. | The user should reach the order overview page. |
| TC16 | Missing first name | Leave the first-name field empty and continue. | Checkout should show a first-name validation message. |
| TC17 | Missing last name | Leave the last-name field empty and continue. | Checkout should show a last-name validation message. |
| TC18 | Missing postal code | Leave the postal-code field empty and continue. | Checkout should show a postal-code validation message. |
| TC19 | Check order total | Compare the subtotal, tax, and total on the overview page. | The total should equal the subtotal plus tax. |
| TC20 | Complete an order | Complete checkout using valid details. | The application should show an order confirmation. |
| TC21 | Check cart after checkout | Complete an order and return to the Products page. | The completed order's items should no longer be in the active cart. |
| TC22 | Access inventory after logout | Log in, log out, and directly open the inventory URL. | The user should not be able to access the protected page without logging in again. |
| TC23 | Check different screen sizes | Open the website at desktop and mobile-sized viewports. | Important content and controls should remain usable. |
| TC24 | Keyboard navigation | Use the keyboard to navigate the login page, product list, and checkout. | Interactive controls should be reachable and usable with the keyboard. |
| TC25 | Check session handling | Log out and try to open a protected page again. | The application should redirect the user to login or otherwise prevent access. |

### Exploratory Testing – 15 Minutes

**Objective:** I want to check whether users can shop and complete checkout without running into unexpected problems.

I would spend the first three minutes exploring the product list and changing the sorting options. Next, I would spend four minutes adding and removing products and checking whether the cart badge matches the actual cart contents. I would then spend five minutes testing checkout, including missing fields and the calculation of the order total. I would use the final three minutes to repeat any suspicious behavior and record the results.

I would pay particular attention to incorrect product sorting, cart counts that do not update, missing validation messages, incorrect totals, and access to the inventory after logout.

For any issue I find, I would record the steps to reproduce it, the expected and actual results, and a screenshot if it helps explain the problem. These are areas I would investigate, not defects I would report without verifying them.

### Test Strategy

I would start with the features that could prevent a customer from buying a product, such as login, sorting, cart operations, and checkout. I would cover both successful and unsuccessful scenarios, including missing form fields and invalid login details. I would use manual testing for exploratory checks, keyboard navigation, and different screen sizes. For repetitive scenarios, I would use Python, Pytest, and Playwright to automate the main workflows. I would keep the tests independent, use reusable page classes, and rely on actual page conditions instead of fixed delays. When a test fails, I would review the error, screenshot, and execution report before deciding whether it is an application defect or a problem with the test itself.

### Automated Test Coverage

I have automated the following main scenarios:

| Manual test case | Automated test |
|---|---|
| TC01 – Standard user login | `test_TC01_standard_user_login` |
| TC02 – Locked-out user login | `test_TC02_locked_user_login` |
| TC06 – Sort prices low to high | `test_TC03_sort_price_low_to_high` |
| TC07 – Sort prices high to low | `test_TC04_sort_price_high_to_low` |
| TC10–TC12 – Add and remove cart items | `test_TC05_add_two_products_remove_one` |
| TC16–TC18 – Required checkout fields | `test_TC06_checkout_required_fields` |
| TC19–TC21 – Checkout total and empty cart | `test_TC07_checkout_total_and_cart_empty` |
| TC22 – Access after logout | `test_TC08_products_page_requires_login` |

The checkout validation test uses parameterization to check three missing-field scenarios. The remaining manual test cases can be tested manually or automated later as the suite grows.

---

# Section B – Test Analysis and Communication

## B1. Reviewing AI-Generated Test Code

I would not use AI-generated test code without checking whether it actually tests the required behavior. A test can look correct but still miss a defect if it checks only one product, uses an incorrect selector, or does not verify the complete result.

For a price-sorting test, I would log in, select the required sorting option, collect all the displayed prices, convert them to numbers, and compare the complete list with the expected order.

For example, the following assertion checks that the prices are in ascending order:

```python
actual_prices = products.get_product_prices()

assert len(actual_prices) > 1
assert actual_prices == sorted(actual_prices), (
    f"Prices are not ascending: {actual_prices}"
)
```

I would run the test against the actual application to confirm that the selector works and the assertion catches incorrect ordering. I would also check that the test does not rely on fixed sleeps and can run independently of other tests.

## B2. Evaluating an AI Testing Feature

I would choose AI-generated test cases as the feature to evaluate. It can save time when creating test scenarios, but I would still check the results before using them.

I would evaluate it using these four checks:

| Check | What I would look for | Score |
|---|---|---|
| Accuracy | Does the generated test match the actual application behavior? | 0–2 |
| Coverage | Does it include positive, negative, and boundary scenarios? | 0–2 |
| Correctness | Are the selectors, test data, and expected results correct? | 0–2 |
| Maintainability | Is the test easy to read, update, and reuse? | 0–2 |

For each check, I would give 0 for poor results, 1 for partially correct results, and 2 for good results. The maximum score would be 8. A score of 7–8 would mean the output looks promising but still needs human review; 4–6 would mean it needs improvements, and 0–3 would mean substantial rework is needed.

## B3. Bug Report – Incorrect Price Sorting

**Title:** Products are not sorted correctly by price in release 4.2.0

**Environment:** Release 4.2.0. The browser, operating system, and build details should be recorded during testing.

**Steps to reproduce:**
1. Log in using a valid account.
2. Open the Products page.
3. Select the price low-to-high option.
4. Check the order of the displayed products.
5. Repeat the test to confirm whether the issue occurs again.

**Expected result:** Products should be displayed from the lowest price to the highest price.

**Actual result:** The reported behavior is that the $29.99 product appears before the $15.99 product.

**Severity:** I would initially consider this a major functional issue because users cannot rely on the selected sorting option. The final priority would depend on the team's release criteria and the impact on users.

**Evidence:** I would attach a screenshot showing the selected sorting option and the incorrect product order, along with the test result and environment details.

I would reproduce the issue before closing the bug and update the report with the confirmed results.

## B4. Release Recommendation

I would recommend investigating the sorting defect before approving the release. If the application consistently places the $29.99 product before the $15.99 product when low-to-high sorting is selected, that is a functional problem that should be assessed before release.

I would also investigate the checkout test that fails in one out of ten runs. I would review the screenshot, logs, and failing step to determine whether the problem comes from the application, test code, or environment. I would not assume it is just a flaky test without evidence.

My recommendation would be to hold release approval until the sorting issue has been assessed and the checkout failure has been investigated. If the release cannot be delayed, the team should document the risk and make an explicit release decision. After any fix, I would rerun the affected tests and the relevant regression suite.

---

## Section C – Investigation and Experience

## C1. Investigating a Checkout Failure

If a checkout test failed, I would first review the test report, screenshot, and error message to identify the exact step where it failed. I would rerun the test to check whether the issue was consistent or intermittent.

Next, I would verify the test setup, including the login status, cart contents, customer details, and page state. I would also check whether the application had loaded correctly before the test interacted with it.

If the issue continued, I would inspect the application behavior and available logs to determine whether the cause was an application defect, test data, an incorrect selector, or a timing issue. If I confirmed a genuine defect, I would document the reproduction steps, expected and actual results, and supporting evidence. If the problem was in the test itself, I would correct the test setup or synchronization and rerun the affected tests to verify the result.

## C2. A Real Issue I Worked On at Vonage

During my time as a Software Engineering Trainee at Vonage, I worked on Java and Spring Boot REST APIs used in telecom billing workflows. One issue I worked on involved inconsistent validation and error handling across API flows, which made some invalid requests harder to troubleshoot.

I reviewed the existing validation logic and helped improve the handling of common validation rules and error responses. I then tested valid requests alongside invalid inputs, including missing or inconsistent data, to check that errors were handled consistently without affecting valid requests.

I also reviewed the resulting errors and regression-test results to verify the changes. This work contributed to a reduction of approximately 10–15% in validation-related API failures. It also made errors easier to interpret and helped make debugging more consistent.

The main lesson I learned was to reproduce an issue, compare the expected and actual behavior, investigate the relevant logic, and verify the change with regression tests. I would apply the same structured approach to a production issue by first assessing its impact, reviewing logs and requests, identifying the cause, validating the fix, and communicating the results clearly.

---

## Test Execution Summary

During my local test run, Pytest reported 10 passed tests and one warning in approximately 18 seconds. This confirms that the tests passed in that particular run. It does not mean every manual test case has been executed or that the application is completely defect-free.