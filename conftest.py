from selenium import webdriver
import logging
import pytest


LOGGER = logging.getLogger(__name__)


@pytest.fixture(scope="class")
def driver():
    driver = webdriver.Chrome()

    LOGGER.info('Running autotests')
    yield driver

    LOGGER.info('Closing the browser')
    driver.quit()
