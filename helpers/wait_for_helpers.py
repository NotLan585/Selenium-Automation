import string

from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC


class WaitHelpers(object):

    def __init__(self, driver):
        self.driver = driver

    def wait_for_text(self, text: string, timeout=30):
        """
        Waits for the string element for the during of the passed in timeout(default 30 seconds)
        """
        WebDriverWait(self. driver, timeout).until(
            EC.presence_of_element_located((By.PARTIAL_LINK_TEXT, text))  # This is a dummy element
        )

    def wait_for_url(self, url: string, timeout=30):
        """
        Waits for the url to update
        """
        WebDriverWait(self. driver, timeout).until(
            EC.url_to_be(url)  # This is a dummy element
        )
