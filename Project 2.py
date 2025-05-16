# Project2: Create a code to open instagram and login to it

from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.chrome.options import Options
import time

# Set up Chrome options
chrome_options = Options()
chrome_options.add_argument("--start-maximized")

# Set up the Chrome driver
driver = webdriver.Chrome(service=Service(), options=chrome_options)

# Open Instagram login page
driver.get("https://www.instagram.com/accounts/login/")
time.sleep(5)

# Enter credentials
username = driver.find_element(By.NAME, "username")
password = driver.find_element(By.NAME, "password")
username.send_keys("your_username")
password.send_keys("your_password")

# Click login
login_button = driver.find_element(By.XPATH, "//button[@type='submit']")
login_button.click()

time.sleep(10)
driver.quit()