# OrangeHRM Automation Framework

A Selenium-based UI Automation Framework developed using Python, Pytest, and the Page Object Model (POM) design pattern.

This project automates critical functionalities of the OrangeHRM application, including Login and PIM (Personnel Information Management) module operations. The framework is designed for scalability, maintainability, and reusability by following industry-standard automation practices.

---

## Tech Stack

- Python
- Selenium WebDriver
- Pytest
- Page Object Model (POM)
- Pytest HTML Reports
- OpenPyXL (Excel Data Handling)
- Logging
- Git & GitHub

---

## Framework Features

✔ Page Object Model (POM)

✔ Data Driven Testing (DDT)

✔ Pytest Fixtures

✔ Parameterization

✔ Explicit Waits

✔ Screenshot Capture on Failure

✔ Custom Logging

✔ Configuration File Management

✔ HTML Test Reports

✔ Reusable Utility Classes

---

## Application Under Test

**OrangeHRM**

Modules Automated:

- Login Module
- PIM Module
- Employee Search Functionality
- Add Employee Functionality

---

## Project Structure

```text
Automation-Tests
│
├── Configurations
│   └── Configuration files and environment settings
│
├── Logs
│   └── Execution logs
│
├── Reports
│   └── Pytest HTML Reports
│
├── pageObjects
│   ├── LoginPage.py
│   ├── AddPIMPage.py
│   └── PIM_search.py
│
├── testCases
│   ├── conftest.py
│   ├── test_login.py
│   ├── test_login_ddt.py
│   ├── test_addPim.py
│   ├── test_SearchByPim.py
│   ├── test_SearchPIMById.py
│   └── test_SearchPimByName.py
│
├── utilities
│   ├── XLUtils.py
│   ├── customLogger.py
│   └── readProperties.py
│
└── README.md
```

---

## Automated Test Scenarios

### Login Functionality

- Valid Login Verification
- Invalid Login Verification
- Data-Driven Login Testing using Excel Data

### PIM Module

- Add New Employee
- Search Employee by Employee ID
- Search Employee by Employee Name
- Validate Search Results

---

## Design Pattern

### Page Object Model (POM)

The framework follows the Page Object Model design pattern where:

- Web elements are maintained separately from test scripts
- Page actions are encapsulated within page classes
- Test scripts remain clean and maintainable

Benefits:

- Better code reusability
- Easier maintenance
- Reduced code duplication
- Improved scalability

---

## Utilities Implemented

### XLUtils.py

Used for Data Driven Testing.

Functions include:

- Reading Excel data
- Writing test results
- Managing test datasets

### customLogger.py

Provides centralized logging support for:

- Test execution tracking
- Failure analysis
- Debugging

### readProperties.py

Used for:

- Reading application URLs
- Managing credentials
- Environment configuration

---

## Reporting

Pytest HTML Reports are generated after execution.

Sample command:

```bash
pytest --html=Reports/report.html
```

Reports include:

- Execution Summary
- Pass/Fail Statistics
- Execution Duration
- Failure Details

---

## Logging

Execution logs are generated inside:

```text
Logs/
```

Logs help identify:

- Test execution flow
- Errors
- Failures
- Debugging information

---

## Data Driven Testing

The framework supports Data Driven Testing using Excel files.

Implemented in:

```text
test_login_ddt.py
```

Test data is read dynamically using:

```text
utilities/XLUtils.py
```

---

## Installation

### Clone Repository

```bash
git clone https://github.com/Manas1853/Automation-Tests.git
```

### Navigate to Project Directory

```bash
cd Automation-Tests
```

### Install Dependencies

```bash
pip install -r requirements.txt
```

---

## Running Tests

Run all tests:

```bash
pytest -v
```

Generate HTML Report:

```bash
pytest -v --html=Reports/report.html
```

Run a specific test:

```bash
pytest testCases/test_login.py -v
```

---

## Skills Demonstrated

- Selenium WebDriver
- Python Automation
- Pytest Framework
- Page Object Model
- Data Driven Testing
- Logging and Reporting
- Test Framework Design
- UI Automation Testing
- Git Version Control

---

## Future Enhancements

- Parallel Test Execution using pytest-xdist
- Cross Browser Testing
- Docker Integration
- GitHub Actions CI/CD Pipeline
- Allure Reporting

---

## Author

**Manas Pal**

Aspiring QA Automation Engineer

GitHub: https://github.com/Manas1853
