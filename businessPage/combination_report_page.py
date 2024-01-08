__author__ = 'Administrator'
from common.collector_log import my_log
from selenium.webdriver.common.by import By
from common.common_fun import Common
from common.read_config import get_appPackage
class CombinationReport(Common):
    appPackage = get_appPackage()
    comb_apply = (By.ID, appPackage+':id/rbtn_1')
    comb_hold = (By.ID, appPackage+':id/rbtn_2')
    comb_relieve = (By.ID, appPackage+':id/rbtn_3')
    rgnsjc = (By.XPATH, "//android.widget.GridView[@resource-id='"+appPackage+":id/lv_type']/android.widget.LinearLayout[1]/android.widget.TextView[1]")
    apply_item = (By.XPATH,"//android.widget.ListView[@resource-id='"+appPackage+":id/lv_group']/android.widget.LinearLayout[1]")
    hold_item = (By.XPATH,"//android.widget.ListView[@resource-id='"+appPackage+":id/lv_query']/android.widget.LinearLayout[1]")
    hold_items = appPackage+":id/ll_root"
    hold_relieve = (By.ID, appPackage+':id/btn_separatecombination')
    hold_singleping = (By.ID, appPackage+':id/btn_singleping')
    relieve_item = (By.XPATH,"//android.widget.ListView[@resource-id=appPackage+':id/lv_query']/android.widget.LinearLayout[1]")
    market = (By.ID, appPackage+':id/tv_market')
    sh = (By.ID, appPackage+':id/tv_market_shanghai')
    sz = (By.ID, appPackage+':id/tv_market_shegnzheng')
    def apply(self):
        self.get_clickable_element(self.comb_apply,"组合申报")
        self.get_clickable_element(self.rgnsjc,"认购牛市价差")
        try:
            self.get_clickable_element(self.apply_item,"认购牛市价差组合")
        except Exception:
            my_log.error("没有认购牛市价差组合")
            self.error_save_screenshot("没有认购牛市价差组合")
            return False
        else:
            self.confirm()
            self.toastok()
            return True


    # 无法定位列表最后一个元素
    # def holdRelieve(self):
    #     self.get_clickable_element(self.comb_hold, "组合持仓")
    #     self.get_visible_element(self.hold_item,"持仓组合")
    #     list1 = self.driver.find_elements_by_id(self.hold_items)
    #     count = len(list1)
    #     item = (By.XPATH,"//android.widget.ListView[@resource-id=appPackage+':id/lv_query']/android.widget.LinearLayout["+str(count)+"]")
    #     print(item)
    #     self.swipe_ele(item)
    #     self.get_clickable_element(self.hold_relieve,"组合持仓--解除组合")
    #     self.confirm()
    #     self.toastok()

    def relieveComb(self):
        self.get_clickable_element(self.comb_relieve, "解除组合")
        try:
            self.get_clickable_element(self.relieve_item, "可解除组合")
        except Exception:
            return False
        else:
            self.confirm()
            self.toastok()
            return True

    def shMarket(self):
        self.get_clickable_element(self.market,"切换市场")
        self.get_clickable_element(self.sh,"切换上海市场")
    def szMarket(self):
        self.get_clickable_element(self.market,"切换市场")
        self.get_clickable_element(self.sz,"切换深圳市场")