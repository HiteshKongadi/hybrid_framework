import time

import pytest
from selenium import webdriver
# from selenium.webdriver.chrome.service import Service
from assertpy import assert_that
from selenium.webdriver.common.by import By
from base.webdriver_listener import WebDriverWrapper
from utilities import data_source

# @pytest.fixture(scope="class", autouse=True)
# def scope_class():
# print("class triggered")
# yield
# print("class end")


class TestLogin(WebDriverWrapper):

    def test_valid_login(self):
        self.driver.find_element(By.NAME, "username").send_keys("Admin")
        self.driver.find_element(By.NAME, "password").send_keys("admin123")
        self.driver.find_element(By.XPATH, "//button[@type='submit']").click()

        actual_dashboard = self.driver.find_element(By.XPATH, "//h6").text
        assert_that("Dashboard").is_equal_to(actual_dashboard)
        # time.sleep(10)

        # print("valid login")

    @pytest.mark.parametrize("username,password,expected_error", data_source.test_invalid_login_data)
    def test_invalid_login(self, username, password, expected_error):
        self.driver.find_element(By.NAME, "username").send_keys(username)
        self.driver.find_element(By.NAME, "password").send_keys(password)
        self.driver.find_element(By.XPATH, "//button[@type='submit']").click()
        actual_error = self.driver.find_element(By.XPATH, "//p[contains(@class ,'oxd-alert-content-text')]").text
        assert_that(expected_error).is_equal_to(actual_error)
        assert_that(actual_error).contains('Invalid')


# //p[contains(normalize-space(),'Invalid credentials')]

class TestLoginUI(WebDriverWrapper):

    def test_title(self):
        actual_title = self.driver.title
        assert "HRM" in actual_title == "OrangeHRM"
        assert_that("OrangeHRM").is_equal_to(actual_title)

    def test_header(self):
        # get the login header and assert it
        actual_header = self.driver.find_element(By.XPATH, "//h5[contains(@class,'login')]").text
        assert_that("Login").is_equal_to(actual_header)

    def test_login_placeholders(self):
        actual_username_placeholder = self.driver.find_element(By.NAME, "username").get_attribute("placeholder")
        actual_password_placeholder = self.driver.find_element(By.NAME, "password").get_attribute("placeholder")
        assert_that("Username").is_equal_to(actual_username_placeholder)
        assert_that("Password").is_equal_to(actual_password_placeholder)
