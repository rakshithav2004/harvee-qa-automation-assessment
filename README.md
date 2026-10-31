# Harvee QA Automation Assessment

This repository contains my QA automation assessment project using Python, Pytest, and Playwright. I automated important e-commerce workflows on SauceDemo, including login, product sorting, cart operations, checkout validation, and access after logout.

## Technologies Used

- Python
- Pytest
- Playwright
- pytest-html
- python-dotenv

## Project Structure

```text
harvee-qa-automation-assessment/
├── pages/
│   ├── login_page.py
│   ├── products_page.py
│   ├── cart_page.py
│   └── checkout_page.py
├── tests/
│   ├── conftest.py
│   ├── test_login.py
│   ├── test_sorting.py
│   ├── test_cart.py
│   ├── test_checkout.py
│   └── test_security.py
├── reports/
├── .env
├── .gitignore
├── pytest.ini
├── requirements.txt
├── ANSWERS.md
├── AI_USAGE.md
└── README.md
```

## Setup

### 1. Clone the repository

```bash
git clone https://github.com/rakshithav2004/harvee-qa-automation-assessment.git
cd harvee-qa-automation-assessment
```

### 2. Create and activate a virtual environment

On Windows PowerShell:

```powershell
python -m venv .venv
.\.venv\Scripts\Activate.ps1
```

### 3. Install dependencies

```powershell
python -m pip install -r requirements.txt
python -m playwright install chromium
```

### 4. Configure environment variables

Create a local `.env` file in the project root:

```env
BASE_URL=https://www.saucedemo.com
STANDARD_USER=standard_user
LOCKED_USER=locked_out_user
TEST_PASSWORD=secret_sauce
```

Do not commit `.env` to GitHub.

## Running the Tests

Run the complete suite:

```powershell
python -m pytest -v
```

Generate an HTML report:

```powershell
python -m pytest -v --html=reports/report.html --self-contained-html
```

Open `reports/report.html` in a browser to review the results.

## Automated Test Coverage

| Test ID | Scenario |
|---|---|
| TC01 | Standard user login |
| TC02 | Locked-out user login |
| TC03 | Sort prices from low to high |
| TC04 | Sort prices from high to low |
| TC05 | Add two products and remove one |
| TC06 | Validate missing checkout fields |
| TC07 | Verify checkout total and empty cart after completion |
| TC08 | Attempt to access inventory after logout |

The checkout validation test uses parameterization to check missing first name, last name, and postal code.

Other manual test scenarios, including keyboard accessibility and responsive layout checks, are documented in `ANSWERS.md`.

## Design Approach

I used a simple Page Object Model to keep page locators and interactions separate from the tests. The tests use explicit assertions to verify application behavior. Configuration values are loaded from environment variables, and failure screenshots are captured where possible.

## Test Results

One local execution reported 10 passed tests and one warning in approximately 18 seconds. Results can vary depending on the application and test environment.

## Scaling the Suite

If the suite grows to around 200 tests, I would organize tests by feature, keep shared behavior in reusable page objects and fixtures, and use clear test IDs. I would separate smoke tests from the full regression suite, add browser coverage where required, and use CI to run tests automatically. I would also monitor flaky tests, review reports, and avoid unnecessary duplication.

## Assessment Answers

See `ANSWERS.md` for the manual test cases, exploratory testing charter, test strategy, code review, AI evaluation approach, bug report, release recommendation, and investigation responses.
