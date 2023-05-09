from selenium.webdriver.common.by import By


class MainPageLocators:
    TESTS_EXAMPLES = (By.XPATH, "//div[@class='endpoints']/ul/li")
    RESPONSE_URL = (By.XPATH, "//span[@class='url']")
    RESPONSE_CODE = (By.XPATH, "//span[@data-key='response-code']")
    RESPONSE_OUTPUT = (By.XPATH, "//pre[@data-key='output-response']")
