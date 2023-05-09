from Page_Object import MainPage
import logging
import pytest


LOGGER = logging.getLogger(__name__)


def test_examples_ui(driver):
    LOGGER.info('Starting the driver')
    yandex_main_page = MainPage(driver)

    # Work with MainPage
    LOGGER.info('The Reqres main page opens')
    yandex_main_page.go_to_main_page()

    LOGGER.info('Get params')
    for params in yandex_main_page.get_test_parameters():
        web_elem, res_code_ui, res_content_ui, req_code_api, res_content_api = params

        LOGGER.info(f'\n{res_code_ui}\n{req_code_api}\n#\n#\n#')
        LOGGER.info(f'\n{res_content_ui}\n{res_content_api}\n#\n#\n#')

        # try:
        #     assert res_code_ui == req_code_api
        #     assert res_content_ui == res_content_api
        # except Exception as ex:
        #     LOGGER.info(f'Assertion error: {ex}')

    # //pre[@data-key='output-response' and @hidden='true']
    # //pre[@data-key='output-response']
