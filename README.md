
# Senior Automation Framework (Playwright + Pytest-BDD)

## Stack
- Playwright (Python)
- Pytest
- Pytest-BDD
- Allure Reports
- Parallel Execution (pytest-xdist)
- Page Object Model
- Environment configuration
- Utilities & reusable components

## Project Structure

features/              -> BDD feature files
features/steps/        -> Step definitions
pages/                 -> Page Object Models
tests/                 -> Fixtures
utils/                 -> Helper utilities
config/                -> Environment configuration
data/                  -> Test data
reports/               -> Allure results & screenshots

## Setup

Install dependencies

pip install -r requirements.txt

Install browsers

playwright install

## Run Tests

pytest

## Generate Allure Report

allure serve reports/allure-results

## Features

- BDD with 40 scenarios
- Parallel execution
- Page Object Model
- Environment configs (.env)
- Test data support
- Screenshot utilities
- Allure reporting
