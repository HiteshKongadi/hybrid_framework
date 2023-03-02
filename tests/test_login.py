from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from assertpy import assert_that

class TestLoginUI:
    def test_title(self):
        #service = Service(executable_path==r"<filepath_of_chrome>")
        #driver = webdriver.Chrome(Service=service)
        driver = webdriver.Chrome()
        driver.maximize_window()
        driver.implicitly_wait(30)
        driver.get("https://opensource-demo.orangehrmlive.com/")
        actual_title = driver.title
        assert "HRM" in actual_title == "OrangeHRM"
        assert_that("OrangeHRM").is_equal_to(actual_title)
