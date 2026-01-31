# IE7374_MLOps
# Lab Assignment 1 – MLOps (IE7374)

## Overview
This repository contains the implementation for **Lab Assignment 1** of the MLOps course at Northeastern University.  
The objective of this lab is to demonstrate Python project structuring, unit testing, and continuous integration using GitHub Actions.

The lab focuses on building a simple Python module, validating it using multiple testing frameworks, and automating test execution through CI pipelines.

---

## Project Structure

IE7374_MLOps/
├── src/
│ ├── init.py
│ └── calculator.py
├── test/
│ ├── init.py
│ ├── test_pytest.py
│ └── test_unittest.py
├── .github/
│ └── workflows/
│ ├── pytest_action.yml
│ └── unittest_action.yml
├── requirements.txt
├── .gitignore
└── README.md


---

## Calculator Module
The `calculator.py` module implements basic arithmetic operations:
- Addition
- Subtraction
- Multiplication
- Combined calculation using intermediate results

Input validation is included to ensure only numeric values are processed.

---

## Testing Implementation

### Pytest
- Implemented in `test_pytest.py`
- Uses assertions and parameterized tests
- Generates a JUnit XML report during CI execution

Run locally:
```bash
pytest -v


Unittest

Implemented in test_unittest.py

Uses Python’s built-in unittest framework

Scoped to avoid dependency conflicts with Pytest tests

Run locally:

python -m unittest test.test_unittest


CI/CD with GitHub Actions

This project uses GitHub Actions to automatically validate code changes.

Pytest CI Workflow

Runs Pytest on every push and pull request to main

Uploads test reports as CI artifacts

Uses Python 3.10 and updated GitHub Actions

Unittest CI Workflow

Runs only Unittest-based test cases

Avoids Pytest dependency conflicts

Configures PYTHONPATH explicitly for CI compatibility

Both workflows must pass to ensure code stability.


Modifications from Reference Repository

To comply with lab requirements, the following customizations were made compared to the reference repository:

Updated Python version to 3.10

Separated Pytest and Unittest into independent CI pipelines

Scoped Unittest execution to avoid Pytest imports

Fixed CI issues related to module resolution

Updated deprecated GitHub Actions to supported versions

Enhanced CI triggers with pull request validation


### How to Run Locally

Create and activate a virtual environment

Install dependencies:

Run tests:

pytest
python -m unittest test.test_unittest

### Conclusion

This lab demonstrates core MLOps practices such as automated testing, CI pipeline configuration, and debugging real-world CI failures. It highlights the importance of reliable testing and automation in production-ready ML and Python systems.

### Repository Link
https://github.com/NagashreeBK98/IE7374_MLOps

