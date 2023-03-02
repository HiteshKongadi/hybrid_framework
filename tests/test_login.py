import pytest
from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from assertpy import assert_that
from selenium.webdriver.common.by import By


class TestLoginUI:

    @pytest.fixture(scope="function" , autouse=True)
    def setup(self):
        # service = Service(executable_path==r"<filepath_of_chrome>")
        # driver = webdriver.Chrome(Service=service)
        self.driver = webdriver.Chrome()
        self.driver.maximize_window()
        self.driver.implicitly_wait(30)
        self.driver.get("https://opensource-demo.orangehrmlive.com/")
        yield
        self.driver.quit()

    def test_title(self):
        actual_title = self.driver.title
        assert "HRM" in actual_title == "OrangeHRM"
        assert_that("OrangeHRM").is_equal_to(actual_title)

    def test_header(self):
        # get the login header and assert it
        actual_header = self.driver.find_element(By.XPATH, "//h5[contains(@class,'login')]").text
        assert_that("Login").is_equal_to(actual_header)
