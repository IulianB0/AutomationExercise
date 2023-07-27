import time

from selenium.webdriver.common.by import By

from utils.webdriver import WebDriver


class RegisterUser(WebDriver):

    def load_url(self, url):
        self.driver.get(f'{url}')
        time.sleep(1)

    def click(self, xpath_button):
        self.driver.find_element(By.XPATH, xpath_button).click()
        time.sleep(1)

    def get_text(self, text):
        self.driver.find_element(By.XPATH, f"//*[contains(text(), '{text}')]")
        self.driver.implicitly_wait(1)

    def fill_text(self, text, text_xpath):
        self.driver.find_element(By.XPATH, text_xpath).send_keys(text)
        self.driver.implicitly_wait(1)


