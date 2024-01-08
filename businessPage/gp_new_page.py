import time
from appium.webdriver.common.mobileby import MobileBy
from common.collector_log import my_log
from common.common_fun import Common
from common.read_config import get_appPackage
from businessPage.trade_first_page import TradeFirst
from businessPage.optional_page import Optional
#首页
class Gp(Common):
    appPackage = get_appPackage()
    # 股票首页
    gptilte = (MobileBy.ID, appPackage+":id/tv_stock")
    qqtilte = (MobileBy.ID, appPackage+":id/tv_options")
    zzc = (MobileBy.ID, appPackage+":id/tv_zzc")
    zzc1 = (MobileBy.ID, appPackage + ":id/tv_zzc_1")
    buy = (MobileBy.ID, appPackage+":id/tv_trade_buy")
    sell = (MobileBy.ID, appPackage+":id/tv_trade_sell")
    position = (MobileBy.ID, appPackage+":id/tv_position")
    chedan = (MobileBy.ID, appPackage+":id/tv_chedan")
    query = (MobileBy.ID, appPackage+":id/tv_query")
    # 资金信息详情
    zjxq = (MobileBy.ID, appPackage+":id/tv_title")
    # 去标识化
    checkbox_pwd = (MobileBy.ID, appPackage + ":id/checkbox_pwd")
    # title
    title = (MobileBy.ID, appPackage+":id/tv_title")
    # 买入
    titlebuy = (MobileBy.XPATH, "//android.widget.RadioButton[@text='买入']")
    contract = (MobileBy.ID, appPackage+":id/tv_contract")
    contract_item1 = (MobileBy.XPATH, "//android.widget.ListView[@resource-id='"+appPackage+":id/lv_code']/android.widget.LinearLayout[1]")
    price = (MobileBy.ID, appPackage+":id/tv_sub_ztdtjia")
    delprice = (MobileBy.ID, appPackage+":id/tv_price_sub_unit")
    addprice = (MobileBy.ID, appPackage+":id/tv_price_add_unit")
    pricetype = (MobileBy.ID, appPackage + ":id/tv_price_type")
    pricetype_item2 = (MobileBy.XPATH, "//android.widget.FrameLayout[1]/android.widget.LinearLayout[1]/android.widget.FrameLayout[1]/android.widget.FrameLayout[1]/android.widget.FrameLayout[1]/android.widget.FrameLayout[1]/android.view.ViewGroup[1]/android.widget.FrameLayout[1]/android.widget.LinearLayout[1]/android.widget.RelativeLayout[2]/androidx.recyclerview.widget.RecyclerView[1]/android.widget.LinearLayout[2]/android.widget.TextView[1]")
    pricetype_item3 = (MobileBy.XPATH, "//android.widget.FrameLayout[1]/android.widget.LinearLayout[1]/android.widget.FrameLayout[1]/android.widget.FrameLayout[1]/android.widget.FrameLayout[1]/android.widget.FrameLayout[1]/android.view.ViewGroup[1]/android.widget.FrameLayout[1]/android.widget.LinearLayout[1]/android.widget.RelativeLayout[2]/androidx.recyclerview.widget.RecyclerView[1]/android.widget.LinearLayout[3]/android.widget.TextView[1]")
    btnCancel = (MobileBy.ID, appPackage + ":id/btnCancel")
    btnOk = (MobileBy.ID, appPackage + ":id/btnOk")
    zt = (MobileBy.ID, appPackage+":id/tv_sub_zt")
    dt = (MobileBy.ID, appPackage+":id/tv_sub_dt")
    num = (MobileBy.ID, appPackage+":id/ed_sub_num")
    delnum = (MobileBy.ID, appPackage+":id/tv_sub_num_nuit")
    addnum = (MobileBy.ID, appPackage+":id/tv_add_num_nuit")
    all = (MobileBy.ID, appPackage + ":id/tv_num1")
    half = (MobileBy.ID, appPackage + ":id/tv_num2")
    third = (MobileBy.ID, appPackage + ":id/tv_num3")
    quarter = (MobileBy.ID, appPackage + ":id/tv_num4")
    submit = (MobileBy.ID, appPackage+":id/btn_sub_mr")
    fiveprice = (MobileBy.ID, appPackage+":id/tv_item_sub_num")
    hold_item = (MobileBy.XPATH, "//android.widget.ListView[@resource-id='"+appPackage+":id/lv_sub_grid']/android.widget.LinearLayout[2]")
    # 加自选
    iv_zx = (MobileBy.ID, appPackage + ":id/iv_zx")
    iv_more = (MobileBy.ID, appPackage + ":id/iv_more")
    more_zx = (MobileBy.ID, appPackage + ":id/tv_name")
    Back = (MobileBy.ID, appPackage + ':id/tv_back')
    # 卖出
    titlesell = (MobileBy.XPATH, "//android.widget.RadioButton[@text='卖出']")
    cantrade = (MobileBy.ID, appPackage+":id/tv_tip_num")
    # 持仓
    titlehold = (MobileBy.XPATH, "//android.widget.RadioButton[@text='持仓']")
    hold = (MobileBy.XPATH, "//android.widget.RadioButton[@text='持仓']")
    hold_item1 = (MobileBy.XPATH, "//android.widget.ListView[@resource-id='"+appPackage+":id/lv_stock_grid']/android.widget.LinearLayout[1]")
    tv_stock_p_mr = (MobileBy.ID, appPackage+":id/tv_stock_p_mr")
    tv_stock_p_mc = (MobileBy.ID, appPackage + ":id/tv_stock_p_mc")
    tv_stock_p_hq = (MobileBy.ID, appPackage + ":id/tv_stock_p_hq")
    tvIndexName = (MobileBy.ID, appPackage + ":id/tvIndexName")
    # 撤单
    titlecancle = (MobileBy.XPATH, "//android.widget.RadioButton[@text='撤单']")
    cancle_item = (MobileBy.XPATH, "//android.widget.ListView[@resource-id='"+appPackage+":id/lv_stock_grid']/android.widget.LinearLayout[1]")
    # 查询
    titlequery = (MobileBy.XPATH, "//android.widget.RadioButton[@text='查询']")
    today_cj = (MobileBy.XPATH, "//android.widget.TextView[@resource-id='"+appPackage+":id/tv_label' and @text='当日成交']")
    today_wt = (MobileBy.XPATH, "//android.widget.TextView[@resource-id='"+appPackage+":id/tv_label' and @text='当日委托']")
    history_cj = (MobileBy.XPATH, "//android.widget.TextView[@resource-id='"+appPackage+":id/tv_label' and @text='历史成交']")
    # 返回
    def back(self):
        self.get_clickable_element(self.Back, "返回")
    # 获取title文字
    def title_text(self):
        text = self.get_element_text(self.title,"title文字")
        return text
    # 点击股票
    def tipGp(self):
        self.get_clickable_element(self.gptilte,"切换股票")
    # 点击期权
    def tipQq(self):
        self.get_clickable_element(self.qqtilte, "切换期权")
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
    # 点击去标识化
    def tipqbsh(self):
        el = self.get_clickable_element(self.checkbox_pwd,"去标识化")
        checked = el.get_attribute('checked')
        print("checked:%s"%checked)
        # 显示
        if checked == 'false':
            try:
                self.get_visible_element(self.zzc,"总资产")
                return True
            except:
                return False
        # 隐藏
        else:
            try:
                self.get_visible_element(self.zzc1,"隐藏总资产")
                return True
            except:
                return False
    # 进入买入页
    def tipxj(self):
        self.get_clickable_element(self.buy, "首页买入")
        try:
            self.get_visible_element(self.titlebuy, "title买入")
        except:
            my_log.error("进入股票买入页面失败")
            return False
        else:
            text = self.get_element_text(self.title,"title")
            if text == "股票买入":
                my_log.info("进入股票买入页面成功")
                return True
            else:
                my_log.error("进入股票买入页面失败")
                return False
    # 进入卖出页
    def tipsj(self):
        self.get_clickable_element(self.sell, "首页卖出")
        try:
            self.get_visible_element(self.titlesell, "title卖出")
        except:
            my_log.error("进入股票卖出页面失败")
            return False
        else:
            text = self.get_element_text(self.title, "title")
            if text == "股票卖出":
                my_log.info("进入股票卖出页面成功")
                return True
            else:
                my_log.error("进入股票卖出页面失败")
                return False
    # 进入持仓页
    def tipcc(self):
        self.get_clickable_element(self.position, "首页持仓")
        try:
            self.get_visible_element(self.titlehold, "title持仓")
        except:
            my_log.error("进入股票持仓页面失败")
            return False
        else:
            text = self.get_element_text(self.title, "title")
            if text == "股票持仓":
                my_log.info("进入股票持仓页面成功")
                return True
            else:
                my_log.error("进入股票持仓页面失败")
                return False
    # 进入撤单页
    def tipcd(self):
        self.get_clickable_element(self.chedan, "首页撤单")
        try:
            self.get_visible_element(self.titlecancle, "title撤单")
        except:
            my_log.error("进入股票撤单页面失败")
            return False
        else:
            text = self.get_element_text(self.title, "title")
            if text == "股票撤单":
                my_log.info("进入股票撤单页面成功")
                return True
            else:
                my_log.error("进入股票撤单页面失败")
                return False
    # 进入查询页
    def tipcx(self):
        self.get_clickable_element(self.query, "首页查询")
        try:
            self.get_visible_element(self.titlequery, "title查询")
        except:
            my_log.error("进入股票查询页面失败")
            return False
        else:
            text = self.get_element_text(self.title, "title")
            if text == "股票查询":
                my_log.info("进入股票查询页面成功")
                return True
            else:
                my_log.error("进入股票查询页面失败")
                return False
    # 点击买入title
    def tipbuy(self):
        self.get_clickable_element(self.titlebuy,"买入")
    # 点击卖出title
    def tipsell(self):
        self.get_clickable_element(self.titlesell, "卖出")
    # 点击持仓title
    def tiphold(self):
        self.get_clickable_element(self.titlehold, "持仓")
    # 点击撤单title
    def tipcancle(self):
        self.get_clickable_element(self.titlecancle, "撤单")
    # 点击查询title
    def tipquery(self):
        self.get_clickable_element(self.titlequery, "查询")
    # 输入合约代码并选择合约
    def input_contract(self,code="000001"):
        self.get_clickable_element(self.contract,"点击代码输入框")
        print(code)
        self.s_keyboard(code)
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
            my_log.error("加价格操作失败，加之前价格:%s，加之后价格:%s" % (text1,text2))
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
            my_log.error("减价格操作失败，减之前价格:%s，减之后价格:%s" % (text1,text2))
            return False
    # 带入涨停价
    def send_ztj(self):
        text = self.get_element_text(self.zt,"涨停价")
        text1 = text.split("：")[-1]
        # 点击涨停价
        self.get_clickable_element(self.zt,"点击涨停价")
        # 获取价格输入框价格
        text2 = self.get_element_text(self.price,"价格")
        if float(text1) == float(text2):
            return True
        else:
            my_log.error("带入涨停价操作失败，涨停价价格:%s，带入之后价格:%s" % (text1,text2))
            return False
    # 带入跌停价
    def send_dtj(self):
        text = self.get_element_text(self.dt, "跌停价")
        text1 = text.split("：")[-1]
        # 点击跌停价
        self.get_clickable_element(self.dt, "点击跌停价")
        # 获取价格输入框价格
        text2 = self.get_element_text(self.price, "价格")
        if float(text1) == float(text2):
            return True
        else:
            my_log.error("带入跌停价操作失败，跌停价价格:%s，带入之后价格:%s" % (text1,text2))
            return False
    # 带入买卖五档价
    def send_fiveprice(self):
        text1 = self.get_element_text(self.fiveprice, "买卖五档价")
        if text1 == "----" or text1 == "- - - -":
            my_log.info("行情没有数据")
            return True
        else:
            # 点击买卖五档价
            self.get_clickable_element(self.fiveprice, "买卖五档")
            # 获取价格输入框价格
            text2 = self.get_element_text(self.price, "价格")
            if float(text1) == float(text2):
                return True
            else:
                my_log.error("带入买卖五档价操作失败，买卖五档价格:%s，带入之后价格:%s" % (text1,text2))
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
            my_log.error("加数量操作失败，加之前:%s，加之后:%s" % (text1,text2))
            return False
    # 减数量
    def del_num(self):
        # 获取减之前的数量
        text1 = self.get_element_text(self.num,"减之前数量")
        # 点击“-”
        self.get_clickable_element(self.delnum,"点击减号")
        # 获取减之后数量
        text2 = self.get_element_text(self.num,"减之后数量")
        # 比较判断
        if int(text1)-100 == int(text2):
            return True
        else:
            my_log.error("减数量操作失败，减之前:%s，减之后:%s" % (text1,text2))
            return False
    # 买入
    def c_buy(self):
        text = self.get_element_text(self.cantrade, "可买数")
        num = text[2:-1]
        print("可买数：%s" % num)
        if int(num) == 0:
            my_log.error("该股票可买数为0")
        else:
            self.get_clickable_element(self.submit,"买入提交")
            self.confirm()
    # 卖出
    def c_sell(self):
        text = self.get_element_text(self.cantrade, "可卖数")
        num = text[2:-1]
        print("可卖数：%s" % num)
        if int(num) == 0:
            my_log.error("该股票可卖数为0")
        else:
            self.get_clickable_element(self.submit,"卖出提交")
            self.confirm()
    # 持仓带入数据
    def c_hold(self):
        self.get_clickable_element(self.hold_item,"持仓item")
        text1 = self.get_element_text(self.contract, "合约代码")
        text2 = self.get_element_text(self.price, "委托价格")
        if text1 != "" and text2 != "":
            return True
        else:
            my_log.error("持仓带入数据错误")
            self.error_save_screenshot("持仓带入数据错误")
            return False
    # 获取输入框中可买/卖数
    def trade_num(self):
        text = self.get_element_text(self.num,"输入框可买/卖数")
        num = text.split(':')[-1]
        print("输入框可买/卖数:%s"%num)
        return int(num)
    # 全仓
    def c_all(self):
        self.get_clickable_element(self.all,"全仓")
    # 半仓
    def c_half(self):
        self.get_clickable_element(self.half, "半仓")
    # 1/3仓
    def c_third(self):
        self.get_clickable_element(self.third, "1/3仓")
    # 1/4仓
    def c_quarter(self):
        self.get_clickable_element(self.quarter, "1/4仓")

    # 加自选
    def c_zx(self):
        self.get_clickable_element(self.iv_zx,"加自选")
    # more加自选
    def c_more_zx(self):
        self.get_clickable_element(self.iv_more,"更多")
        text = self.get_element_text(self.more_zx,"更多-加自选")
        self.get_clickable_element(self.more_zx,"更多-加自选")
        self.back()
        if text == "加入自选":
            my_log.info("执行加自选操作")
        elif text == "删除自选":
            my_log.info("执行删自选操作")
        else:
            my_log.error("更多-加自选,按钮名称为：%s" %text)
    # 查看是否已加自选，已加自选返回True，未加自选返回False
    def zx_state(self):
        self.get_clickable_element(self.iv_more,"更多")
        time.sleep(1)
        text = self.get_element_text(self.more_zx,"更多-加自选")
        if text == "加入自选":
            self.back()
            return False
        elif text == "删除自选":
            self.back()
            return True
        else:
            my_log.error("更多-加自选,按钮名称为：%s" %text)
            self.back()
            return text
    # # 从股票交易页进入自选页
    # def gp_to_zx(self):
    #     self.back()
    #     TradeFirst.to_optional_page(self)
    # # 根据股票名称查看自选页是否存在该股票
    # def have_Optional(self,name):
    #     res = Optional.have_zx(name)
    #     return res

    # 持仓-买入
    def hold_mr(self):
        self.get_clickable_element(self.hold_item1,"点击持仓")
        self.get_clickable_element(self.tv_stock_p_mr,"买入")
        text = self.get_element_text(self.submit,"提交")
        text1 = self.get_element_text(self.contract, "合约代码")
        text2 = self.get_element_text(self.price, "委托价格")
        if text1 != "" and text2 != "" and text == "买入":
            return True
        else:
            my_log.error("持仓带入数据错误")
            return False
    # 持仓-卖出
    def hold_mc(self):
        self.get_clickable_element(self.hold_item1, "点击持仓")
        self.get_clickable_element(self.tv_stock_p_mc, "卖出")
        text = self.get_element_text(self.submit, "提交")
        text1 = self.get_element_text(self.contract, "合约代码")
        text2 = self.get_element_text(self.price, "委托价格")
        if text1 != "" and text2 != "" and text == "卖出":
            return True
        else:
            my_log.error("持仓带入数据错误")
            return False
    # 持仓-行情
    def hold_hq(self):
        self.get_clickable_element(self.hold_item1, "点击持仓")
        self.get_clickable_element(self.tv_stock_p_hq, "行情")
        try:
            self.get_visible_element(self.tvIndexName,"指数")
        except:
            my_log.error("持仓跳转行情页失败")
            return False
        else:
            return True

    # 撤单
    def cancle(self):
        try:
            self.get_visible_element(self.cancle_item,"撤单数据")
        except:
            my_log.error("没有撤单数据")
            return False
        else:
            self.get_clickable_element(self.cancle_item,"撤单数据")
            self.toastok()
            return True

    # 查询-当日成交
    def cx_cj_today(self):
        self.get_clickable_element(self.today_cj,"当日成交")
        text = self.get_element_text(self.title,"当日成交title")
        if text == "当日成交":
            return True
        else:
            my_log.error("进入查询-当日成交页失败")
            return False
    # 查询-当日委托
    def cx_wt_today(self):
        self.get_clickable_element(self.today_wt, "当日委托")
        text = self.get_element_text(self.title, "当日委托title")
        if text == "当日委托":
            return True
        else:
            my_log.error("进入查询-当日委托页失败")
            return False
    # 查询-历史成交
    def cx_cj_history(self):
        self.get_clickable_element(self.history_cj, "历史成交")
        text = self.get_element_text(self.title, "历史成交title")
        if text == "历史成交":
            return True
        else:
            my_log.error("进入查询-历史成交页失败")
            return False

    # 获取价格类型数组
    def price_type_arr(self):
        self.get_clickable_element(self.pricetype,"点击价格类型")
        arr = []
        time.sleep(1)
        # 向下滑动
        self.swipeup(0.85,0.95,500)
        for i in range(10):
            text1 = self.get_element_text(self.pricetype_item2,"中间选中item")
            text2 = self.get_element_text(self.pricetype_item3,"底部item")
            print("arr加入元素：%s"%text1)
            arr.append(text1)
            # 如果滑到底了，就结束循环
            if text2 == "":
                break
            else:
                self.swipeup(0.95,0.88,500)
                time.sleep(1)
                text3 = self.get_element_text(self.pricetype_item2,"底部item")
                # 如果滑动没有改变数据，就是没有滑动成功，重新滑动
                while text1 == text3:
                    print("没有滑动成功，重新滑动")
                    self.swipeup(0.9, 0.81, 500)
                    text3 = self.get_element_text(self.pricetype_item2,"底部item")
                # 如果滑动幅度过大(之前底部item与现在中间item不一样)，则往上回滑
                text4 = self.get_element_text(self.pricetype_item2,"中间选中item")
                while text4 != text2:
                    print("滑动幅度过大,回滑")
                    self.swipeup(0.85, 0.9, 500)
                    text4 = self.get_element_text(self.pricetype_item2, "底部item")
        self.get_clickable_element(self.btnCancel,"取消")
        my_log.info(arr)
        return arr
