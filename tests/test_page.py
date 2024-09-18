import unittest

from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.chrome.options import Options
import time
from page_objects.page_object import HomePage

# Setup Chrome WebDriver options
chrome_options = Options()
chrome_options.add_argument("--start-maximized")

# Initialize WebDriver (ensure you have the correct path to chromedriver)
service = Service("path_to_chromedriver")

class TestHomePage(unittest.TestCase):

    def setUp(self):
        self.driver = webdriver.Chrome()

    def test_home_page(self):
        """

        :return:
        """
        driver = self.driver
        driver.get("https://www.youtube.com/")
        home_page = HomePage(driver)
        home_page.fill_search_input("Test")
        # Locate username and password fields and log in button
        username_input = driver.find_element(By.ID, "username")
        password_input = driver.find_element(By.ID, "password")
        login_button = driver.find_element(By.ID, "loginButton")

        # Enter login credentials
        username_input.send_keys("your_username")
        password_input.send_keys("your_password")

        # Submit the form
        login_button.click()

        # Wait for the page to load and check if login is successful
        time.sleep(5)

        # Check for login success by finding a logout button or a specific element on the landing page
        logout_button = driver.find_element(By.ID, "logoutButton")
