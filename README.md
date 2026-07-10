<h1><span style ="color:#007ACC;">SauceDemo POM Automation</span></h1>
This project is a UI automation framework for the **SauceDemo** website built using **Python**, **Selenium**, **Pytest**, and the **Page Object Model (POM)** design pattern.

The framework automates the main user flow of the application, including login, inventory, cart, and checkout.

---

## Website Under Test

https://www.saucedemo.com/

---

## Tech Stack

- Python
- Selenium WebDriver
- Pytest
- Page Object Model (POM)
- uv
- Git & GitHub

---

## Project Structure

```text
saucedemo_pom/
│
├── docs/
│   ├── bugreport_saucedemo.pdf
│   ├── sauceDemo_Test_Plan.pdf
│   └── test_case_saucedemo.xlsx
│
├── pages/
│   ├── base_page.py
│   ├── login_page.py
│   ├── inventory_page.py
│   ├── cart_page.py
│   ├── checkout_step_one_page.py
│   ├── checkout_step_two_page.py
│   └── checkout_complete_page.py
│
├── tests/
│   ├── test_login.py
│   ├── test_inventory.py
│   ├── test_cart.py
│   ├── test_checkout_step_one.py
│   ├── test_checkout_step_two.py
│   └── test_checkout_complete.py
│
├── conftest.py
├── pyproject.toml
├── uv.lock
└── README.md
```

---

## Getting Started

### 1. Clone the repository

```bash
git clone https://github.com/Nirju33/saucedemo_pom
```

Go to the project folder.

```bash
cd saucedemo_pom
```

---

### 2. Create a virtual environment

```bash
uv venv
```

---

### 3. Activate the virtual environment

**Windows**

```powershell
.venv\Scripts\activate
```

**macOS/Linux**

```bash
source .venv/bin/activate
```

---

### 4. Install dependencies

```bash
uv sync
```

---

## Running the Tests

Run all tests:

```bash
pytest
```

Run tests with detailed output:

```bash
pytest -v
```

Run a specific test file:

```bash
pytest tests/test_inventory.py
```

Run a specific test:

```bash
pytest tests/test_inventory.py -k test_price_sorting
```

Generate an HTML report:

```bash
pytest --html=report.html
```

---
 
