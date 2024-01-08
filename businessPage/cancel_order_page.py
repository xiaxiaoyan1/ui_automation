__author__ = 'Administrator'
# from appium.webdriver.common.mobileby import MobileBy
# from selenium.common.exceptions import NoSuchElementException
from common.collector_log import my_log
from selenium.webdriver.common.by import By
from common.common_fun import Common
from common.read_config import get_appPackage
import time,pytest
class CancelOrder(Common):
    appPackage = get_appPackage()
    all_cancel = (By.ID,appPackage+":id/btn_all_chedan") # 全部撤单
    confirm_cancel = (By.ID,appPackage+":id/btn_confirm_chedan") # 批量撤单
    checkbox_cancel = (By.ID,appPackage+":id/checkbox")  # 撤单单选框
    item = (By.XPATH,"//android.widget.ListView[@resource-id='"+appPackage+":id/lv_query']/android.widget.LinearLayout[1]") # 可撤的单
    item_name = (By.XPATH,"//android.widget.FrameLayout[1]/android.widget.LinearLayout[1]/android.widget.FrameLayout[1]/android.widget.LinearLayout[1]/android.widget.FrameLayout[1]/android.widget.LinearLayout[1]/android.widget.ListView[1]/android.widget.LinearLayout[1]/android.widget.LinearLayout[1]/android.widget.LinearLayout[1]/android.widget.TextView[1]")  # 可撤单的合约名称
    cancel = (By.ID, appPackage+':id/action_revoke') # 撤单
    cancel_sell = (By.ID, appPackage+':id/action_alter') # 撤单后再买入/卖出/平仓
    cancel_type = (By.XPATH, "//android.widget.FrameLayout[1]/android.widget.LinearLayout[1]/android.widget.FrameLayout[1]/android.widget.LinearLayout[1]/android.widget.FrameLayout[1]/android.widget.LinearLayout[1]/android.widget.ListView[1]/android.widget.LinearLayout[1]/android.widget.LinearLayout[1]/android.widget.HorizontalScrollView[1]/android.widget.LinearLayout[1]/android.widget.TextView[2]")  # 买入/卖出/平仓

    title = (By.ID, appPackage+':id/tv_title') # 交易页面title
    hand = (By.ID, appPackage + ":id/et_hand")  # 交易页面数量输入框

    def c_checkbox_cancel(self):
        self.get_clickable_element(self.checkbox_cancel,"撤单单选框")

    def c_all_cancel(self):
        try:
            self.get_visible_element(self.item,"可撤的单")
        except Exception:
            my_log.error("没有可撤单")
            self.error_save_screenshot("没有可撤单")
            self.toastok()
            return False
        else:
            self.get_clickable_element(self.all_cancel, "全部撤单")
            self.toastok()
            self.toastok()
            return True

    def c_confirm_cancel(self):
        time.sleep(3)
        self.get_clickable_element(self.confirm_cancel, "批量撤单")
        try:
            text = self.get_element_text(self.confirm_cancel, "确定撤单")
            self.get_clickable_element(self.checkbox_cancel, "撤单单选框")
        except Exception:
            my_log.error("没有可撤单")
            self.error_save_screenshot("没有可撤单")
            return False
        else:
            pytest.assume(text == "确定撤单")
            my_log.info("有可撤单")
            self.get_clickable_element(self.confirm_cancel, "确定撤单")
            self.toastok()
            return True
    def c_cancel(self):
        try:
            self.get_clickable_element(self.item, "可撤的单")
        except Exception:
            my_log.error("没有可撤单")
            self.error_save_screenshot("没有可撤单")
            return False
        else:
            my_log.info("有可撤单")
            self.get_clickable_element(self.cancel, "撤单")
            self.confirm()
            self.toastok()
            return True
    def c_cancel_sell(self):
        try:
            self.get_clickable_element(self.item, "可撤的单")
        except Exception:
            my_log.error("没有可撤单")
            self.error_save_screenshot("没有可撤单")
            return False
        else:
            my_log.info("有可撤单")
            item_name = self.get_element_text(self.item_name,"可撤单name")
            text = self.get_element_text(self.cancel_type,"业务类型")
            print(text)
            el_text = self.get_element_text(self.cancel_sell,"撤单后买入/卖出/平仓")
            self.get_clickable_element(self.cancel_sell, "撤单后买入/卖出/平仓")
            print(el_text)
            if "买入开仓" in text:
                pytest.assume(el_text == "撤单后再买入")
            elif "卖出开仓" in text:
                pytest.assume(el_text == "撤单后再卖出")
            elif "平仓" in text:
                pytest.assume(el_text == "撤单后再平仓")
            # 获取撤单合约名称、张数
            el1 = self.get_textContains_ele("合约名称")
            el2 = self.get_textContains_ele("委托数量")
            # name、num为数组，需取数组中第二个元素
            name = el1.text.split("：")
            num = el2.text.split("：")
            print(name,num,item_name)
            pytest.assume(name[1].replace(" ", "") == item_name.replace(" ", ""))
            # 提交，跳转至交易页
            self.confirm()
            title = self.get_element_text(self.title,"交易页面title")
            trade_count = self.get_element_text(self.hand,"数量输入框")
            print(title,trade_count)
            pytest.assume(name[1].replace(" ", "") == title.replace(" ", "") and num[1] == trade_count)
            return True
    # def one_cancel(self):
    #     self.driver.find_element(*self.clickline)
    #     com=Common(self.driver)
    #     com.confirm_frame()
    #     try:
    #         self.driver.find_element(*self.toast)
    #         self.driver.find_element(*self.toasttext)
    #     except NoSuchElementException:
    #         logging.error('cancel order fail')
    #         getsreen=Common(self.driver)
    #         getsreen.getScreenShot('cancel order fail')
    #         return False
    #     else:
    #         self.driver.find_element(*self.toast0k).click()
    #         return True








