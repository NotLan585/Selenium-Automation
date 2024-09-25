from asyncio import timeout

from selenium.webdriver import Keys
from selenium.webdriver.common.by import By



class HomePage(object):

    def __init__(self, driver):
        self.driver = driver
        self.search_bar = (By.NAME, 'search_query')
        self.video_title = (By.ID, 'video-title')

    def fill_search_input(self, username: str):
        """

        :param driver:
        :param username:
        :return:
        """
        self.driver.find_element(*self.search_bar).send_keys(username)

    def hit_search_bar_enter(self):
        """

        :return:
        """
        self.driver.find_element(*self.search_bar).send_keys(Keys.ENTER)

    def click_clip_title(self, title: str):
        """

        :param title:
        :return:
        """
        self.driver.find_element(By.LINK_TEXT, f"{title}").click()
