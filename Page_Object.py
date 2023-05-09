from locators import *
from Base_Page import BaseClass
import requests
import time

import logging  #


LOGGER = logging.getLogger(__name__)  #


class MainPage(BaseClass):
    def get_test_parameters(self):
        all_tests = self.find_elements(MainPageLocators.TESTS_EXAMPLES, time=self.time)

        parameters = []
        for web_elem in all_tests:
            web_elem.click()
            time.sleep(0.5)

            row = ()

            response_code_ui = int(self.find_element(MainPageLocators.RESPONSE_CODE, time=self.time).text)
            try:
                response_output_ui = self.find_element(MainPageLocators.RESPONSE_OUTPUT, time=self.time).json
            except AttributeError:
                response_output_ui = self.find_element(MainPageLocators.RESPONSE_OUTPUT, time=self.time).text

            response_url = self.find_element(MainPageLocators.RESPONSE_URL, time=self.time).text
            response = requests.get("https://reqres.in" + response_url)
            response_code_api = response.status_code
            try:
                response_output_api = response.json()
            except AttributeError:
                response_output_api = response.content

            row += (web_elem, response_code_ui, response_output_ui, response_code_api, response_output_api)

            parameters.append(row)
            LOGGER.info(f'{row}')

        return parameters
