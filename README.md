# E-commerce QA Automation Project

## Description

This project aims to automate the QA of an e-commerce website https://www.automationexercise.com/. It includes a few automated tests that cover various functionalities and scenarios of the site.
This is ongoing project and additional tests will be added.

## Testing Approach and Design Patterns
- Page Object Model (POM) for UI Tests
- Request-Response Model for API Tests - In progress

---

#### 1. Local Machine:

##### Start new test run:

    pytest -vs --alluredir=allure-reports

##### Check allure results:

    allure serve allure-reports

##### CLI Arguments:

1. `--headless` - run tests without loading the browser's UI.
2. `--use_local_driver` - use local driver without downloading it by `webdriver-manager` if added.
3. `--driver-path` - path to the driver (`external_files/drivers/chromedriver.exe` by default).



##### requirements for setup:

1. python3
2. allure
3. pip3 - should be installed as part of python3
4. pytest
5. faker
6. panda
