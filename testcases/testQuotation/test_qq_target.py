# __author__ = 'Administrator'
# import pytest
# # from common.parivay import Pricay
# from page_object.first_page import first
# from page_object.qq_target_page import qq_target
# from common.desired_caps import app_desired
# from appium import webdriver
# import time
# # @pytest.fixture()
# # def my_fixture():
#
# class Test_target():
#     def test_qqtarget(self):
#         driver=app_desired()
#         self.driver=driver
#         T_offer=first(driver)
#         T_offer.to_quotation()
#         T_target=qq_target(driver)
#         T_target.to_Toffer()
#         self.driver.get_screenshot_as_file('../screenshots/T型报价.png')
#         Type_Quo=self.driver.find_element_by_xpath('//*[@resource-id="com.fzzq.qqb.fz:id/tv_title"]')
#         assert Type_Quo.get_attribute('text') == '上证50ETF'
#