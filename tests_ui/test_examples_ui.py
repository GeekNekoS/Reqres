from Page_Object import MainPage
import logging


LOGGER = logging.getLogger(__name__)


def test_examples_ui(driver):
    LOGGER.info('Starting the driver')
    yandex_main_page = MainPage(driver)

    # Work with MainPage
    LOGGER.info('The Reqres main page opens')
    yandex_main_page.go_to_main_page()

    LOGGER.info('Get params')
    for params in yandex_main_page.get_test_parameters():
        response_code_ui, response_output_ui, response_code_api, response_content_api = params
        try:
            assert response_code_ui == response_code_api
            assert response_output_ui == response_content_api
        except Exception as ex:
            LOGGER.info(f'Assertion error: {ex}')
