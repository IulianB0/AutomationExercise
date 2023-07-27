from selenium import webdriver


class WebDriver:

    driver = webdriver.Chrome()
    driver.maximize_window()

    def pop(self):
        try:
            alert = self.driver.switch_to.alert
            alert.dismiss()
        except Exception:
            pass
    def quit(self):
        self.driver.quit()
