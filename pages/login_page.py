from selenium.webdriver.common.by import By


class LoginPage:
    def __init__(self, driver):
        self.d = driver

    def enter_username(self, username):
        self.d.find_element(By.NAME, "username").send_keys(username)

    def enter_password(self, password):
        self.d.find_element(By.NAME, "password").send_keys(password)
