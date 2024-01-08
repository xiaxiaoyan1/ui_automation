import time
from appium.webdriver.common.mobileby import MobileBy
from common.collector_log import my_log
from common.common_fun import Common
from common.read_config import get_appPackage
#首页
class Gp(Common):
    appPackage = get_appPackage()
    # 股票首页
    gptilte = (MobileBy.ID, appPackage+":id/tv_stock")
    zzc = (MobileBy.ID, appPackage+":id/tv_zzc")
    buy = (MobileBy.ID, appPackage+":id/tv_trade_buy")
    sell = (MobileBy.ID, appPackage+":id/tv_trade_sell")
    position = (MobileBy.ID, appPackage+":id/tv_position")
    chedan = (MobileBy.ID, appPackage+":id/tv_chedan")
    query = (MobileBy.ID, appPackage+":id/tv_query")
    # 资金信息详情
    zjxq = (MobileBy.ID, appPackage+":id/tv_title")
    # 买入
    subbuy = (MobileBy.ID, appPackage+":id/btn_sub_mairu")
    contract = (MobileBy.ID, appPackage+":id/tv_contract")
    contract_item1 = (MobileBy.XPATH, "//android.widget.ListView[@resource-id='"+appPackage+":id/lv_code']/android.widget.LinearLayout[1]")
    price = (MobileBy.ID, appPackage+":id/tv_sub_ztdtjia")
    delprice = (MobileBy.ID, appPackage+":id/tv_sub_zttv")
    addprice = (MobileBy.ID, appPackage+":id/tv_sub_dttv")
    zt = (MobileBy.ID, appPackage+":id/tv_sub_zt")
    dt = (MobileBy.ID, appPackage+":id/tv_sub_dt")
    num = (MobileBy.ID, appPackage+":id/ed_sub_num")
    delnum = (MobileBy.ID, appPackage+":id/btn_sub_delete")
    addnum = (MobileBy.ID, appPackage+":id/btn_sub_add")
    submit = (MobileBy.ID, appPackage+":id/btn_sub_mr")
    fiveprice = (MobileBy.ID, appPackage+":id/tv_item_sub_num")
    hold = (MobileBy.XPATH, "//android.widget.RadioButton[@text='持仓']")
    hold_item = (MobileBy.XPATH, "//android.widget.ListView[@resource-id='"+appPackage+":id/lv_sub_grid']/android.widget.LinearLayout[1]")
    # 卖出
    subsell = (MobileBy.ID, appPackage+":id/btn_sub_maichu")

    # 点击股票
    def tipGp(self):
        self.get_clickable_element(self.gptilte,"切换股票")
    # 点击资金详情
    def tipzzc(self):
        self.get_clickable_element(self.zzc,"点击总资产")
        try:
            self.get_visible_element(self.zjxq,"资金详情title")
        except:
            my_log.error("进入资金详情页失败")
            return False
        else:
            text = self.get_element_text(self.zjxq,"资金详情title值")
            if text == "资金信息详情":
                my_log.info("进入资金详情页成功")
                return True
            else:
                print("此页面title:%s" %text)
                my_log.error("进入资金详情页失败")
                return False
    # 进入限价页
    def tipxj(self):
        self.get_clickable_element(self.buy, "限价")
        try:
            self.get_visible_element(self.subbuy, "限价-买入")
        except:
            my_log.error("进入股票限价页面失败")
            return False
        else:
            my_log.info("进入股票限价页面成功")
            return True
    # 进入市价页
    def tipsj(self):
        self.get_clickable_element(self.sell, "市价")
        try:
            self.get_visible_element(self.subbuy, "市价-买入")
        except:
            my_log.error("进入股票市价页面失败")
            return False
        else:
            my_log.info("进入股票市价页面成功")
            return True
    # 点击买入title
    def tipbuy(self):
        self.get_clickable_element(self.subbuy,"买入")
    # 点击卖出title
    def tipbuy(self):
        self.get_clickable_element(self.subsell, "卖出")
    # 输入合约代码并选择合约
    def input_contract(self,code="000001"):
        self.send_key(self.contract,code,"输入合约代码")
        self.get_clickable_element(self.contract_item1, "选择合约")
        text1 = self.get_element_text(self.contract, "合约代码")
        text2 = self.get_element_text(self.price, "委托价格")
        if text1 != "" and text2 != "":
            return True
        else:
            my_log.error("合约代码输入错误")
            return False
    # 加价格
    def add_price(self):
        # 获取加之前的价格
        text1 = self.get_element_text(self.price,"加之前价格")
        # 获取最小单位价格
        unit_price = self.get_element_text(self.addprice,"最小单位价格")
        # 点击“+”
        self.get_clickable_element(self.addprice,"点击加号")
        # 获取加之后价格
        text2 = self.get_element_text(self.price,"加之后价格")
        # 比较判断
        if float(text1)+float(unit_price) == float(text2):
            return True
        else:
            my_log.error("加价格操作失败")
            return False
    # 减价格
    def del_price(self):
        # 获取减之前的价格
        text1 = self.get_element_text(self.price,"减之前价格")
        # 获取最小单位价格
        unit_price = self.get_element_text(self.addprice,"最小单位价格")
        # 点击“-”
        self.get_clickable_element(self.delprice,"点击减号")
        # 获取减之后价格
        text2 = self.get_element_text(self.price,"减之后价格")
        # 比较判断
        if float(text1)-float(unit_price) == float(text2):
            return True
        else:
            my_log.error("减价格操作失败")
            return False
    # 带入涨停价
    def send_ztj(self):
        text1 = self.get_element_text(self.zt,"涨停价")
        # 点击涨停价
        self.get_clickable_element(self.zt,"点击涨停价")
        # 获取价格输入框价格
        text2 = self.get_element_text(self.price,"价格")
        if float(text1) == float(text2):
            return True
        else:
            my_log.error("带入涨停价操作失败")
            return False
    # 带入跌停价
    def send_dtj(self):
        text1 = self.get_element_text(self.dt, "跌停价")
        # 点击跌停价
        self.get_clickable_element(self.dt, "点击跌停价")
        # 获取价格输入框价格
        text2 = self.get_element_text(self.price, "价格")
        if float(text1) == float(text2):
            return True
        else:
            my_log.error("带入跌停价操作失败")
            return False
    # 带入买卖五档价
    def send_fiveprice(self):
        text1 = self.get_element_text(self.fiveprice, "买卖五档价")
        # 点击买卖五档价
        self.get_clickable_element(self.dt, "买卖五档")
        # 获取价格输入框价格
        text2 = self.get_element_text(self.price, "价格")
        if float(text1) == float(text2):
            return True
        else:
            my_log.error("带入跌停价操作失败")
            return False
    # 输入数量
    def input_num(self,count=100):
        self.send_key(self.num,count,"输入数量")
    # 加数量
    def add_num(self):
        # 获取加之前的数量
        text1 = self.get_element_text(self.num,"加之前数量")
        # 点击“+”
        self.get_clickable_element(self.addnum,"点击加号")
        # 获取加之后数量
        text2 = self.get_element_text(self.num,"加之后数量")
        # 比较判断
        if int(text1)+100 == int(text2):
            return True
        else:
            my_log.error("加数量操作失败")
            return False
    # 减数量
    def del_num(self):
        # 获取减之前的数量
        text1 = self.get_element_text(self.num,"减之前数量")
        # 点击“-”
        self.get_clickable_element(self.addnum,"点击减号")
        # 获取减之后数量
        text2 = self.get_element_text(self.num,"减之后数量")
        # 比较判断
        if int(text1)-100 == int(text2):
            return True
        else:
            my_log.error("减数量操作失败")
            return False
    # 买入
    def c_buy(self):
        self.get_clickable_element(self.subbuy)
        self.confirm()
    # 卖出
    def c_sell(self):
        self.get_clickable_element(self.subsell)
        self.confirm()
    # 持仓带入数据
    def c_hold(self):
        self.get_clickable_element(self.hold,"持仓")
        self.get_clickable_element(self.hold_item,"持仓item")
        text1 = self.get_element_text(self.contract, "合约代码")
        text2 = self.get_element_text(self.price, "委托价格")
        if text1 != "" and text2 != "":
            return True
        else:
            my_log.error("持仓带入数据错误")
            return False
