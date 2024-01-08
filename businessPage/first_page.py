import time
from appium.webdriver.common.mobileby import MobileBy

from common.collector_log import my_log
from common.common_fun import Common
from common.read_config import get_appPackage
#首页
class First(Common):
    appPackage = get_appPackage()
    quotation = (MobileBy.XPATH, '//*[@class="android.widget.RadioButton"and @index="2"]')
    trade = (MobileBy.XPATH, '//*[@class="android.widget.RadioButton"and @index="3"]')
    hq = (MobileBy.XPATH,"//android.widget.TextView[@text='行情报价']")
    contract_screen = (MobileBy.XPATH, "//android.widget.TextView[@text='合约筛选']")
    strategy = (MobileBy.XPATH, "//android.widget.TextView[@text='策略交易']")
    contract_trade = (MobileBy.XPATH, "//android.widget.TextView[@text='期权交易']")
    notice = (MobileBy.XPATH, "//android.widget.TextView[@text='重要通告']")
    optional = (MobileBy.XPATH, "//android.widget.TextView[@text='自选商品']")
    statistics = (MobileBy.XPATH, "//android.widget.TextView[@text='市场统计']")
    wave_index = (MobileBy.XPATH, "//android.widget.TextView[@text='波动指数']")
    history_hq = (MobileBy.XPATH, "//android.widget.TextView[@text='历史行情']")
    news_more = (MobileBy.ID, appPackage+":id/tv_news_more")
    video_more = (MobileBy.ID, appPackage+":id/tv_video_more")
    title = (MobileBy.ID, appPackage+":id/tv_title")
    # 策略交易
    strategy_hight = (MobileBy.XPATH, "//android.widget.Button[@text='大涨']")
    strategy_order = (MobileBy.ID, appPackage+":id/btn_order")
    # 市场统计
    gou_count = (MobileBy.XPATH, "//android.widget.FrameLayout[1]/android.widget.LinearLayout[1]/android.widget.FrameLayout[1]/android.widget.LinearLayout[1]/android.widget.RelativeLayout[3]/android.widget.ListView[1]/android.widget.LinearLayout[2]/android.widget.LinearLayout[1]/android.widget.TextView[2]")
    calendar = (MobileBy.ID, appPackage+":id/iv_click_calendar")
    # 波动指数
    ETF50 = (MobileBy.XPATH, "//android.widget.TextView[@text='沪50ETF波指']")
    bz_title = (MobileBy.ID, appPackage+":id/tv_zqmc")
    # 期权
    qq_title = (MobileBy.ID, appPackage+":id/tv_options")

    def to_quotation(self):
        self.click_element(self.quotation, "行情")
    def to_login(self):
        time.sleep(3)
        self.get_clickable_element(self.trade, "交易")
    def to_hq(self):
        self.get_clickable_element(self.hq,"行情报价")
        res = self.assert_element_text(self.title,"期权标的")
        return res
    def to_contract_screen(self):
        self.get_clickable_element(self.contract_screen, "合约筛选")
        res = self.assert_element_text(self.title, "合约筛选")
        return res
    def to_strategy(self):
        self.get_clickable_element(self.strategy,"策略交易")
        self.get_clickable_element(self.strategy_hight,"大涨")
        self.get_clickable_element(self.strategy_order, "下单")
        self.confirm()
        text = self.toastok_text()
        if "闭市" in text:
            self.toastok()
            my_log.error("现在已闭市,系统禁止委托")
            self.error_save_screenshot("现在已闭市,系统禁止委托")
            return False
        elif "提示" in text:
            self.toastok()
            return True
        else:
            self.pop_click(3, "确认")
            my_log.error("委托失败")
            self.error_save_screenshot("委托失败")
            return False
        # res = self.assert_element_text(self.title, "策略选择")
        # return res
    def to_trade(self):
        self.get_clickable_element(self.contract_trade,"期权交易")
        res = self.assert_element_text(self.qq_title, "期权")
        return res
    def to_notice(self):
        self.get_clickable_element(self.notice,"重要通告")
        res = self.assert_element_text(self.title, "通告")
        return res
    def to_optional(self):
        self.get_clickable_element(self.optional,"自选商品")
        res = self.assert_element_text(self.title, "自选")
        return res
    def to_statistics(self):
        self.get_clickable_element(self.statistics,"市场统计")
        text1 = self.get_element_text(self.gou_count,"认购总成交量")
        self.get_clickable_element(self.calendar,"日历")
        self.get_clickable_element((MobileBy.XPATH,"//android.widget.CheckedTextView[@class='android.widget.CheckedTextView']"),"DAY")
        # day = self.driver.find_elements_by_xpath("//android.widget.CheckedTextView[@class='android.widget.CheckedTextView']")
        # print(day)
        # for i in day:
        #     print(i.checked)
        #     if i.checked == "true":
        #         print("checked")
        #         i.click()
        #         break
        text2 = self.get_element_text(self.gou_count,"认购总成交量")
        return int(text1),int(text2)
    def to_wave_index(self):
        self.get_clickable_element(self.wave_index,"波动指数")
        self.get_clickable_element(self.ETF50,"沪50ETF波指")
        res = self.assert_element_text(self.bz_title, "沪50ETF波指")
        return res
    # def to_history_hq(self):
    #     self.get_clickable_element(self.history_hq,"历史行情")
    #     res = self.assert_element_text(self.title, "历史行情")
    #     return res
    # def to_news_more(self):
    #     self.get_clickable_element(self.news_more,"更多新闻")
    #     res = self.assert_element_text(self.title, "更多新闻")
    #     return res
    # def to_video_more(self):
    #     self.get_clickable_element(self.video_more,"更多视频")
    #     res = self.assert_element_text(self.title, "更多视频")
    #     return res

