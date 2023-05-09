from Page_Object import MainPage
import logging


LOGGER = logging.getLogger(__name__)


def test_examples_api(driver):
    LOGGER.info('smth')
    yandex_main_page = MainPage(driver)

    # Work with MainPage
    LOGGER.info('The yandex disk page opens')
    yandex_main_page.go_to_main_page()

    LOGGER.info('Finding smth')
    yandex_main_page.find_smth()
