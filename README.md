# Incognito Login

A simple Python learning project that uses Selenium to open Chrome in incognito mode and submit the LinkedIn login form.

The goal is to practice browser automation: configuring a browser, finding elements by ID, entering text, and sending keyboard input.

## What it does

1. Opens a new incognito Chrome window.
2. Navigates to the LinkedIn login page.
3. Waits three seconds, then fills in the email and password fields.
4. Submits the form with the Enter key.
5. Waits five seconds, then closes the browser.

## Requirements

- Python 3 with pip
- Google Chrome
- An internet connection

Selenium can manage ChromeDriver automatically through [Selenium Manager](https://www.selenium.dev/documentation/selenium_manager/). The first run may need to download a compatible driver.

## Setup

Clone the repository and create a virtual environment:

```sh
git clone https://github.com/NimLordia/incognitologin.git
cd incognitologin
python -m venv .venv
```

Activate the environment on Windows (PowerShell):

```powershell
.\.venv\Scripts\Activate.ps1
```

Or on macOS / Linux:

```sh
source .venv/bin/activate
```

If your system uses `python3` instead of `python`, use `python3` when creating the environment.

Install the dependencies:

```sh
python -m pip install -r requirements.txt
```

## Usage

In `app.py`, replace the placeholder values with your own login details:

```python
username_field.send_keys("your_email@example.com")
password_field.send_keys("your_password")
```

Keep real credentials out of Git commits. Restore the placeholders before committing or sharing the file.

Run the script:

```sh
python app.py
```

## Current limitations

This is a small learning exercise. It uses fixed delays, does not verify whether login succeeded, and does not handle login errors, CAPTCHA, or two-factor authentication. Changes to LinkedIn's page may also require updating the script.

The browser closes automatically after the final delay, so the script does not leave an interactive logged-in session open. If an earlier step raises an exception, browser cleanup is not guaranteed.
