import unittest
from asyncio import timeout

from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.chrome.options import Options
import time

from helpers.wait_for_helpers import WaitHelpers
from page_objects.page_object import HomePage

# Setup Chrome WebDriver options
chrome_options = Options()
chrome_options.add_argument("--start-maximized")

# Initialize WebDriver (ensure you have the correct path to chromedriver)
service = Service("path_to_chromedriver")

class TestHomePage(unittest.TestCase):

    def setUp(self):
        self.driver = webdriver.Chrome()

    def test_home_page_search(self):
        """
        Goes to the page
        Fills in the search input
        Clicks the search button
        Waits for the specific text
        Clicks the title of the clip passed in
        Waits for the url
        Verifies the element is visible
        :return:
        """
        driver = self.driver
        driver.get("https://www.youtube.com/")
        home_page = HomePage(driver)
        home_page.fill_search_input("Crab Rave")
        home_page.hit_search_bar_enter()
        helper = WaitHelpers(self.driver)
        helper.wait_for_text(text='Noisestorm - Crab Rave [Monstercat Release]', timeout=10)
        home_page.click_clip_title('Noisestorm - Crab Rave [Monstercat Release]')
        helper.wait_for_url(url='https://www.youtube.com/watch?v=LDU_Txk06tM', timeout=10)
        assert driver.find_element(By.PARTIAL_LINK_TEXT, 'Noisestorm - Crab Rave [Monstercat Release]').is_displayed()