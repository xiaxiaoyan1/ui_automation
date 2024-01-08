__author__ = 'Administrator'
#from common.desired_caps import App_Start
import time
import pytest
# from base.baseview import BaseView
# from appium import webdriver
# com=App_Start()
# driver=com.app_desired()
# com.pricay_agree()
from selenium.webdriver.common.by import By
from common.desired_caps import app_desired
from common.common_fun import Common
from common.read_config import get_appPackage
driver=app_desired()
class Toffer(Common):
    appPackage = get_appPackage()
    que_details = (By.ID, appPackage + ':id/ll_group')
    target_details = (By.ID, appPackage + ':id/rl_entry')
    def to_que_details(self):
        test=driver.find_elements_by_id(appPackage+":id/ll_group")
        test[1].click()
    def to_target_details(self):
        self.get_clickable_element(self.target_details,"xxx")

