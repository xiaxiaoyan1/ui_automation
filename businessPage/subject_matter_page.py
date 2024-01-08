import time,pytest
from appium.webdriver.common.mobileby import MobileBy
from selenium.webdriver.common.by import By

from common.collector_log import my_log
from common.common_fun import Common
from common.read_config import get_appPackage
class SubjectMatter(Common):
    appPackage = get_appPackage()
    index = (By.ID,appPackage+":id/tv_name")
    ETF = (By.ID,appPackage+":id/tv_listtitle")
    ETF_tok = (By.ID,appPackage+":id/rl_entry")
    capital = (By.XPATH,"//android.widget.TextView[@text='资金']")
    news = (By.XPATH, "//android.widget.TextView[@text='新闻']")
    up = (By.XPATH, "// android.widget.TextView[@text='上涨']")
    news_item = (By.XPATH, "//android.widget.ListView[@resource-id='news']/android.view.View[1]")
    t_price = (MobileBy.XPATH, "//android.widget.TextView[@text='期权']")
    implement_price = (MobileBy.ID, appPackage+":id/tv_content")
    # 获取第i个指数并点击
    def c_index(self,i):
        ele = self.get_visible_elements(self.index, "指数")
        print(ele)
        text = ele[i].text
        ele[i].click()
        return text
    def c_ETF(self,i):
        ele = self.get_visible_elements(self.ETF,"ETF")
        text = ele[i].text
        ele[i].click()
        self.get_clickable_element(self.ETF_tok,"ETF_tok")
        return text
    def Capital(self,text):
        self.swipeup(0.8, 0.2, 100)
        self.swipeup(0.8, 0.2, 100)
        self.get_clickable_element(self.capital, "%s的资金" %text)
        res = self.find_element(self.up, "上涨")
        pytest.assume(res == True)
    def News(self,text):
        self.swipeup(0.8, 0.2, 100)
        self.swipeup(0.8, 0.2, 100)
        self.get_clickable_element(self.news, "%s的新闻" %text)
        res = self.find_element(self.news_item, "news_item",30)
        pytest.assume(res == True)
    def option(self):
        # self.swipeup(0.8, 0.2, 100)
        # self.swipeup(0.8, 0.2, 100)
        # self.get_clickable_element(self.t_price, "期权")
        try:
            self.swipe_ele(self.t_price)
            text = self.get_element_text(self.implement_price, "执行价",15)
        except:
            self.swipe_ele(self.t_price)
            text = self.get_element_text(self.implement_price, "执行价",15)
        if text == "":
            my_log.error("未获取到期权中的执行价%s" % text)
            pytest.assume(1 == 0)
        else:
            pytest.assume(1 == 1)