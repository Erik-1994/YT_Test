import pytest
from selenium import webdriver
from lib2to3.pgen2 import driver


@pytest.fixture()
def test_setup():
    global driver

    driver = webdriver.Chrome(
        executable_path="C:\\Users\\Lenovo Legion\\Desktop\\chromedriver.exe")

    driver.implicitly_wait(10)
    driver.maximize_window()
    yield
    driver.quit()


def test_validYtT(test_setup):
    driver.get("https://www.youtube.com/")

    search = driver.find_element_by_name("search_query")
    search.send_keys("test")

    button = driver.find_element_by_id("search-icon-legacy")
    button.submit()

    assert "test" in driver.current_url

