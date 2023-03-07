import time

import pytest
from selenium import webdriver
# from selenium.webdriver.chrome.service import Service
from assertpy import assert_that
from selenium.webdriver.common.by import By
from base.webdriver_listener import WebDriverWrapper


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

    def test_invalid_login(self):
        self.driver.find_element(By.NAME, "username").send_keys("Admin123")
        self.driver.find_element(By.NAME, "password").send_keys("admin12893")
        self.driver.find_element(By.XPATH, "//button[@type='submit']").click()
        actual_error = self.driver.find_element(By.XPATH, "//p[contains(@class ,'oxd-alert-content-text')]").text
        assert_that("Invalid credentials").is_equal_to(actual_error)
        assert_that (actual_error).contains('Invalid')


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
