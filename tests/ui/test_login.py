import pytest

from pages.login_page import LoginPage
from utils.driver_factory import get_driver
from data.test_data import VALID_USERNAME, VALID_PASSWORD


def test_login_success():

    driver = get_driver()

    login_page = LoginPage(driver)
    login_page.open()
    login_page.login(VALID_USERNAME, VALID_PASSWORD)

    assert "inventory" in driver.current_url

    driver.quit()