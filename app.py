from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
import time

# Configure Chrome to open in incognito mode
chrome_options = Options()
chrome_options.add_argument("--incognito")

# Create a new Chrome session (ensure chromedriver is in your PATH or specify its location)
driver = webdriver.Chrome(options=chrome_options)

# Open LinkedIn login page
driver.get("https://www.linkedin.com/login")

# Allow the page to load
time.sleep(3)

# Locate the username and password fields
username_field = driver.find_element(By.ID, "username")
password_field = driver.find_element(By.ID, "password")

# Input your credentials (replace with your email and password)
username_field.send_keys("your_email@example.com")
password_field.send_keys("your_password")

# Submit the login form by simulating the ENTER key
password_field.send_keys(Keys.RETURN)

# Wait for login to complete (adjust time if needed)
time.sleep(5)

# Your bot is now logged in to LinkedIn!
# You can now add further steps to interact with the site.

# Optionally, close the browser when done
driver.quit()
