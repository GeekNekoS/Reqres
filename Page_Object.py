from locators import *
from Base_Page import BaseClass
from tests_api.test_examples_api import *  #
import json
import time

import logging  #


LOGGER = logging.getLogger(__name__)  #


class MainPage(BaseClass):
    def get_test_parameters(self):
        api_tests = {
            0: test_get_list_users,
            1: test_get_single_user,
            2: test_get_single_user_not_found,
            3: test_get_list_resource,
            4: test_get_single_resource,
            5: test_get_single_resource_not_found,
            6: test_post_create,
            7: test_put_update,
            8: test_patch_update,
            9: test_delete_delete,
            10: test_post_register_successful,
            11: test_post_register_unsuccessful,
            12: test_post_login_successful,
            13: test_post_login_unsuccessful,
            14: test_get_delayed_response
        }

        all_tests = self.find_elements(MainPageLocators.TESTS_EXAMPLES, time=self.time)

        parameters = []
        for i in range(len(api_tests)):
            all_tests[i].click()
            time.sleep(0.5)

            row = ()

            response_code_ui = int(self.find_element(MainPageLocators.RESPONSE_CODE, time=self.time).text)
            try:
                response_output_ui = json.loads(self.find_element(MainPageLocators.RESPONSE_OUTPUT, time=self.time).text)
                LOGGER.info(f'{i}: {response_output_ui}')  #
            except:
                response_output_ui = self.find_element(MainPageLocators.RESPONSE_OUTPUT, time=self.time).text  # ''
                LOGGER.info(f'{i}: {response_output_ui}')  #

            response_code_api, response_content_api = api_tests[i]()
            row += (response_code_ui, response_output_ui, response_code_api, response_content_api)

            parameters.append(row)

        return parameters
