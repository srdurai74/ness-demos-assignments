import time

import pytest
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.relative_locator import locate_with

from BaseConfig import BaseConfig
from DataConfig import DataConfig
from LoginPage import LoginPage
from DashboardPage import DashboardPage
from Util import Util

driver = webdriver.Chrome()


def test_login():

    global driver
    driver.get(BaseConfig.BASE_URL)
    driver.implicitly_wait(BaseConfig.DEFAULT_TIMEOUT)
    driver.maximize_window()
    util = Util()
    util.time_delay(3)

    loginpo = LoginPage(driver)
    util.time_delay(3)
    # dashboardpo = DashboardPage(driver)
    dashboardpo = loginpo.check_valid_login(DataConfig.VALID_USER_NAME,DataConfig.VALID_PASSWORD)
    util.time_delay(3)
    print('here :'+ dashboardpo.get_dashboard_msg())
    assert dashboardpo.get_dashboard_msg() == 'Dashboard'

    util.time_delay(5)

    driver.quit()
