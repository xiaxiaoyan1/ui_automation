__author__ = 'Administrator'
from appium.webdriver.common.mobileby import MobileBy
from selenium.common.exceptions import NoSuchElementException
from common.common_fun import Common
import logging
from common.read_config import get_appPackage
class OrderSearch(Common):
    appPackage = get_appPackage()
    stock=(MobileBy.ID,appPackage+':id/tv_stock')
    btnok=(MobileBy.ID,appPackage+':id/btnOk')
    btncancel=(MobileBy.ID,appPackage+':id/btnCancel')


#标的选择-确认
    def choice_stock(self):
        self.driver.find_element(*self.stock).click()
        com=Common(self.driver)
        com.swipeup()
        self.driver.find_element(*self.btnok).click()

#标的选择-取消
    def cancel_stock(self):
        self.driver.find_element(*self.stock).click()
        com=Common(self.driver)
        com.swipeup()
        self.driver.find_element(*self.btncancel).click()




