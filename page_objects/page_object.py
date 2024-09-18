from selenium.webdriver.common.by import By



class HomePage(object):

    def __init__(self, driver):
        self.driver = driver


    def fill_search_input(self, username: str):
        """

        :param driver:
        :param username:
        :return:
        """
        element = self.driver.find_element(By.CLASS_NAME, 'ytd-searchbox')
        element.send_keys(username)

