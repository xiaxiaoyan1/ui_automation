import time,pytest
from appium.webdriver.common.mobileby import MobileBy

from common.collector_log import my_log
from common.common_fun import Common
from common.read_config import get_appPackage
class Contract(Common):
    appPackage = get_appPackage()
    # 合约页
    arrow_left = (MobileBy.ID,appPackage+":id/iv_arrow_left")
    arrow_right = (MobileBy.ID, appPackage+":id/iv_arrow_right")
    title = (MobileBy.ID, appPackage+":id/tv_zqmc")
    more_page = (MobileBy.ID, appPackage+":id/iv_more")
    min = (MobileBy.ID, appPackage+":id/radiobtn_1")
    day = (MobileBy.ID, appPackage+":id/radiobtn_2")
    week = (MobileBy.ID, appPackage+":id/radiobtn_3")
    month = (MobileBy.ID, appPackage+":id/radiobtn_4")
    year = (MobileBy.ID, appPackage+":id/radiobtn_5")
    time_more = (MobileBy.ID, appPackage+":id/radiobtn_6")
    k_line = (MobileBy.XPATH, "//android.widget.FrameLayout[1]/android.widget.LinearLayout[1]/android.widget.FrameLayout[1]/androidx.drawerlayout.widget.DrawerLayout[1]/android.widget.RelativeLayout[1]/android.widget.FrameLayout[1]/android.widget.FrameLayout[1]/android.widget.LinearLayout[1]/android.widget.LinearLayout[1]/android.widget.LinearLayout[1]/android.widget.FrameLayout[1]/android.widget.TextView[1]")
    comboBox = (MobileBy.XPATH, "//android.widget.FrameLayout[1]/android.widget.LinearLayout[1]/android.widget.FrameLayout[1]/androidx.drawerlayout.widget.DrawerLayout[1]/android.widget.RelativeLayout[1]/android.widget.FrameLayout[1]/android.widget.FrameLayout[1]/android.widget.LinearLayout[1]/android.widget.LinearLayout[1]/android.widget.LinearLayout[1]/android.widget.FrameLayout[1]/android.widget.TextView[6]")
    VOLUME = (MobileBy.XPATH, "//android.widget.TextView[@text='VOLUME']")
    MACD = (MobileBy.XPATH, "//android.widget.TextView[@text='MACD']")
    KDJ = (MobileBy.XPATH, "//android.widget.TextView[@text='KDJ']")
    RSI = (MobileBy.XPATH, "//android.widget.TextView[@text='RSI']")
    setup = (MobileBy.ID, appPackage+":id/radiobtn_7")
    sub_num = (MobileBy.ID, appPackage+":id/ll_bs")
    t_price = (MobileBy.XPATH, "//android.widget.TextView[@text='T型报价']")
    implement_price = (MobileBy.ID, appPackage+":id/tv_content")
    handicap = (MobileBy.XPATH, "//android.widget.TextView[@text='盘口']")
    handicap_price = (MobileBy.XPATH, "//android.widget.TextView[@text='内在价值']")
    detailed = (MobileBy.XPATH, "//android.widget.TextView[@text='明细']")
    detailed_item = (MobileBy.XPATH, "//android.widget.ListView[@resource-id='"+appPackage+":id/lv_detail']/android.widget.LinearLayout[2]")
    indexName = (MobileBy.ID, appPackage+":id/tvIndexName")
    indexName_item = (MobileBy.ID, appPackage+":id/tv_name")
    indexName_hu = (MobileBy.ID, appPackage+":id/btn_hu")
    indexName_shen = (MobileBy.ID, appPackage+":id/btn_shen")
    indexName_300 = (MobileBy.ID, appPackage+":id/btn_chuang")
    indexName_chuang = (MobileBy.ID, appPackage+":id/btn_bd")
    indexName_close = (MobileBy.ID, appPackage+":id/tv_colse")
    fast_buy = (MobileBy.ID, appPackage+":id/btn_fast_buy")
    fast_sell = (MobileBy.ID, appPackage+":id/btn_fast_sell")
    del_unit = (MobileBy.ID, appPackage+":id/tv_del_unit")
    add_unit = (MobileBy.ID, appPackage+":id/tv_add_unit")
    order_price = (MobileBy.ID, appPackage+":id/tv_price")
    hand_del_unit = (MobileBy.ID, appPackage+":id/tv_hand_del_unit")
    hand_add_unit = (MobileBy.ID, appPackage+":id/tv_hand_add_unit")
    hand = (MobileBy.ID, appPackage+":id/et_hand")
    btn_buy = (MobileBy.ID, appPackage+":id/btn_buy")
    btn_sell = (MobileBy.ID, appPackage+":id/btn_sell")
    order = (MobileBy.ID, appPackage+":id/tv_order")
    add_self = (MobileBy.ID, appPackage+":id/addSelf")
    sub_self = (MobileBy.ID, appPackage+":id/subSelf")


    def arrow(self,direction):
        title = self.get_element_text(self.title,"title")
        new_title = ""
        if direction == "left":
            self.get_clickable_element(self.arrow_left,"左切换")
            time.sleep(2)
            new_title = self.get_element_text(self.title,"new_title")
        elif direction == "right":
            self.get_clickable_element(self.arrow_right, "右切换")
            time.sleep(2)
            new_title = self.get_element_text(self.title, "new_title")
        else:
            my_log.error("arrow方法传参只接受left/right,实际传参值为%s"%direction)
        print("切换前合约名称：%s，切换后合约名称：%s"%(title,new_title))
        return title,new_title
    # data = 日/周/月/年/分时/5分钟/15分钟/30分钟/60分钟
    def cycle(self,data):
        if data == "日":
            self.get_clickable_element(self.day,"日K")
            time.sleep(1)
            res = self.get_element_text(self.k_line,"K线类型日K")
            pytest.assume(res == "日K")
        elif data == "周":
            self.get_clickable_element(self.week, "周K")
            time.sleep(1)
            res = self.get_element_text(self.k_line, "K线类型周K")
            pytest.assume(res == "周K")
        elif data == "月":
            self.get_clickable_element(self.month, "月K")
            time.sleep(1)
            res = self.get_element_text(self.k_line, "K线类型月K")
            pytest.assume(res == "月K")
        elif data == "年":
            self.get_clickable_element(self.year, "年K")
            time.sleep(1)
            res = self.get_element_text(self.k_line, "K线类型年K")
            pytest.assume(res == "年K")
        elif data == "分时":
            self.get_clickable_element(self.min, "分时")
            time.sleep(1)
            res = self.find_element(self.sub_num, "买卖5档")
            pytest.assume(res == True)
        else:
            # self.get_clickable_element(self.time_more, "下拉框")
            # xpath = "//*[@text='5分钟']"
            # xpath.replace("5分钟",data)
            # print(xpath)
            # self.get_clickable_element((MobileBy.XPATH,xpath),"下拉列表item")
            # time.sleep(1)
            # res = self.get_element_text(self.k_line, "K线类型")
            # pytest.assume(res == data)
            my_log.error("传参（%s）错误！"%data)
    # type = MACD/KDJ/RSI/VOLUME
    def amount(self,type):
        self.get_clickable_element(self.comboBox,"选择弹窗")
        if type == "MACD":
            self.get_clickable_element(self.MACD,"MACD")
            text = self.get_element_text(self.comboBox,"选择弹窗text")
            pytest.assume(text == type)
        elif type == "KDJ":
            self.get_clickable_element(self.KDJ, "KDJ")
            text = self.get_element_text(self.comboBox, "选择弹窗text")
            pytest.assume(text == type)
        elif type == "RSI":
            self.get_clickable_element(self.RSI, "RSI")
            text = self.get_element_text(self.comboBox, "选择弹窗text")
            pytest.assume(text == type)
        elif type == "VOLUME":
            self.get_clickable_element(self.VOLUME, "VOLUME")
            text = self.get_element_text(self.comboBox, "选择弹窗text")
            pytest.assume(text == type)
        else:
            my_log.error("参数值%s不存在"%type)
    def tPrice(self):
        self.swipeup(0.8, 0.2, 100)
        self.swipeup(0.8,0.2,100)
        self.get_clickable_element(self.t_price,"T型报价")
        time.sleep(5)
        text = self.get_element_text(self.implement_price,"执行价")
        if text == "":
            my_log.error("未获取到T型报价中的执行价%s" % text)
            pytest.assume(1 == 0)
        else:
            pytest.assume(float(text) > 0)
    def Handicap(self):
        self.swipeup(0.8, 0.2, 100)
        self.swipeup(0.8, 0.2, 100)
        self.get_clickable_element(self.handicap, "盘口")
        res = self.find_element(self.handicap_price,"内在价值")
        pytest.assume(res == True)
    def Detailed(self):
        self.swipeup(0.8, 0.2, 100)
        self.swipeup(0.8, 0.2, 100)
        self.get_clickable_element(self.detailed, "明细")
        res = self.find_element(self.detailed_item, "明细item")
        pytest.assume(res == True)
    def index(self):
        self.get_clickable_element(self.indexName,"指数")
        self.get_clickable_element(self.indexName_hu,"上证指数")
        text = self.get_element_text(self.indexName_item,"指数名称")
        pytest.assume(text == "上证指数")
        self.get_clickable_element(self.indexName_shen, "深圳成指")
        text = self.get_element_text(self.indexName_item, "指数名称")
        pytest.assume(text == "深证成指")
        self.get_clickable_element(self.indexName_300, "沪深300")
        text = self.get_element_text(self.indexName_item, "指数名称")
        pytest.assume(text == "沪深300")
        self.get_clickable_element(self.indexName_chuang, "创业板指")
        text = self.get_element_text(self.indexName_item, "指数名称")
        pytest.assume(text == "创业板指")
        self.get_clickable_element(self.indexName_close,"关闭指数弹窗")
    def fastBuy(self):
        self.get_clickable_element(self.fast_buy,"快买")
        self.get_clickable_element(self.btn_buy,"快买按钮")
        time.sleep(2)
        self.remind()
        self.confirm()
        return self.entrust_submit()
    def fastSell(self):
        self.get_clickable_element(self.fast_sell,"快卖")
        self.get_clickable_element(self.btn_sell, "快卖按钮")
        time.sleep(2)
        self.remind()
        self.confirm()
        return self.entrust_submit()
    def to_order(self):
        self.get_clickable_element(self.order,"交易")
    def addSelf(self):
        try:
            text = self.get_element_text(self.add_self,"加自选text")
            self.get_clickable_element(self.add_self, text)
        except:
            text = self.get_element_text(self.sub_self, "减自选text")
            self.get_clickable_element(self.sub_self, text)
        return text




