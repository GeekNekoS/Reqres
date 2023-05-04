from locators import *
from Base_Page import BaseClass


class MainPage(BaseClass):
    # exsample
    def find_smth(self):
        return self.find_element(LoginLocators.SMTH, time=self.time)
