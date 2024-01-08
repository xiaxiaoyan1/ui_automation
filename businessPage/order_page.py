__author__ = 'Administrator'

import time,math

from common.collector_log import my_log
from selenium.webdriver.common.by import By

from common.read_config import get_appPackage
from common.common_fun import Common
class Order(Common):
    appPackage = get_appPackage()
    title = (By.ID,appPackage+":id/tv_title") #title
    iv_right = (By.ID, appPackage + ":id/iv_right")  # 切换合约
    add_optional=(By.ID,appPackage+":id/iv_zx") #加/减自选按钮
    more=(By.ID,appPackage+":id/iv_more")  #更多按钮
    entrust_style=(By.XPATH,"//android.widget.TextView[@text='委托风格']")  #委托风格
    contract=(By.ID,appPackage+":id/tv_contract")  #合约代码输入框
    search=(By.ID,appPackage+":id/tbt_search") #合约搜索按钮
    del_price=(By.ID,appPackage+": id / tv_del_unit") #减价格按钮
    add_price=(By.ID,appPackage+":id/tv_add_unit") #加价格按钮
    price=(By.ID,appPackage+":id/tv_price") # 价格输入框
    price_dsj=(By.ID,appPackage+":id/btn_dsj") # 价格输入框-对手价
    price_gdj = (By.ID, appPackage+":id/btn_gdj")  # 价格输入框-挂单价
    price_ztj = (By.ID, appPackage+":id/btn_ztj")  # 价格输入框-涨停价
    price_dtj = (By.ID, appPackage+":id/btn_dtj")  # 价格输入框-跌停价
    price_sjzx = (By.ID, appPackage+":id/btn_sjzx")  # 价格输入框-市价转限
    price_sjfok = (By.ID, appPackage+":id/btn_sjfok")  # 价格输入框-市价FOK
    price_sjioc = (By.ID, appPackage+":id/btn_sjioc")  # 价格输入框-市价IOC
    dismiss = (By.ID, appPackage+":id/iv_dismiss")  # 价格输入框-收起键盘
    del_hand = (By.ID, appPackage+":id/tv_hand_del")  # 减数量按钮
    add_hand = (By.ID, appPackage+":id/tv_hand_add")  #加数量按钮
    hand = (By.ID, appPackage+":id/et_hand") #数量输入框
    FOK = (By.ID, appPackage+":id/cb_fok") #FOK
    covered = (By.ID, appPackage+":id/cb_covered") #备兑
    clock = (By.ID, appPackage+":id/tv_cName1") #锁定解锁
    covered_sell = (By.ID, appPackage + ":id/tv_cName2")  # 备兑开仓
    price_now = (By.ID, appPackage+":id/tv_price_now") #最新价
    ztj_price = (By.ID, appPackage+":id/tv_price_up") #涨停价
    dtj_price = (By.ID, appPackage+":id/tv_price_down") #涨停价
    fristsell_price = (By.XPATH, "//android.widget.FrameLayout[1]/android.widget.LinearLayout[1]/android.widget.FrameLayout[1]/androidx.drawerlayout.widget.DrawerLayout[1]/android.widget.RelativeLayout[1]/android.widget.FrameLayout[1]/android.widget.LinearLayout[1]/android.widget.LinearLayout[1]/android.widget.LinearLayout[2]/android.widget.LinearLayout[2]/android.widget.ListView[1]/android.widget.LinearLayout[5]/android.widget.LinearLayout[1]/android.widget.TextView[2]") #卖一价
    orderbuy = (By.ID, appPackage+':id/ll_order1') # 买开按钮
    ordersell = (By.ID, appPackage+':id/ll_order2') # 卖开按钮
    orderflat = (By.ID, appPackage+':id/ll_order3') # 平仓按钮
    btn_kc = (By.ID, appPackage+':id/btn_kc') # 传统开仓
    btn_pc = (By.ID, appPackage+':id/btn_pc')  # 传统平仓
    traditional_buy = (By.ID, appPackage+':id/btn_traditional_buy')  # 传统买入开仓/平仓
    traditional_sell = (By.ID, appPackage+':id/btn_traditional_sell')  # 传统卖出开仓/平仓
    flat_price = (By.ID, appPackage+':id/tv_cPrice') # 平仓价格
    btn_cancel = (By.ID, appPackage+':id/btn_cancel') # 取消下单

    hold = (By.XPATH,"//android.widget.RadioButton[@text='持仓']") # 持仓
    hold_num_name = (By.XPATH,"//android.widget.TextView[@text='持仓/可用']") # 持仓/可用
    hold_count = (By.XPATH,"//android.widget.ListView[@resource-id='"+appPackage+":id/listview']/android.widget.LinearLayout[1]/android.widget.LinearLayout[2]/android.widget.TextView[2]") # 第一条持仓可用数量
    hold_counts = (By.ID, appPackage+':id/tv_filed2') # 所有持仓数量
    hold_nowprices = (By.ID, appPackage+':id/tv_filed4') # 所有持仓成本
    hold_yk = (By.XPATH,"//android.widget.TextView[@text='盈亏']") # 盈亏
    hold_yks = (By.ID, appPackage+':id/tv_filed6') # 所有持仓盈亏
    hold_num = (By.XPATH,"//android.widget.ListView[@resource-id='"+appPackage+":id/listview']/android.widget.LinearLayout[1]/android.widget.LinearLayout[2]/android.widget.TextView[1]") # 持仓数量
    hold_name = (By.XPATH,"//android.widget.ListView[@resource-id='"+appPackage+":id/listview']/android.widget.LinearLayout[1]/android.widget.LinearLayout[1]/android.widget.TextView[2]") # 持仓名称
    hold_type = (By.XPATH,"//android.widget.ListView[@resource-id='"+appPackage+":id/listview']/android.widget.LinearLayout[1]/android.widget.LinearLayout[1]/android.widget.TextView[1]") # 权力/义务
    hold_more = (By.XPATH, "//android.widget.ListView[@resource-id='"+appPackage+":id/listview']/android.widget.LinearLayout[1]/android.widget.ImageView[1]")  # 持仓更多
    all_flat = (By.XPATH, "//*[@text='全部平仓']")  # 全部平仓
    quick_back = (By.XPATH, "//*[@text='快捷反手']")  # 快捷反手
    cancel = (By.XPATH, "//android.widget.RadioButton[@text='撤单']")  # 撤单
    all_cancel = (By.ID, appPackage+':id/btn_all_chedan')  # 全部撤单
    confirm_cancel = (By.ID, appPackage+':id/btn_confirm_chedan')  # 确定撤单
    checkbox_cancel = (By.ID,appPackage+":id/checkbox")  # 撤单单选框
    entrust = (By.XPATH, "//android.widget.RadioButton[@text='委托']")  # 委托
    state = (By.XPATH, "//android.widget.TextView[@text='状态']")  # 状态
    deal = (By.XPATH, "//android.widget.RadioButton[@text='成交']")  # 成交
    deal_time = (By.XPATH, "//android.widget.TextView[@text='成交时间']")  # 成交时间
    trend = (By.XPATH, "//android.widget.RadioButton[@text='走势']")  # 走势
    trend_img = (By.XPATH, "//android.widget.FrameLayout[@resource-id='"+appPackage+":id/trendView']/android.view.View[1]")  # 走势图
    optional = (By.XPATH, "//android.widget.RadioButton[@text='自选']")  # 自选
    optional_item = (By.XPATH, "//android.widget.FrameLayout[1]/android.widget.LinearLayout[1]/android.widget.FrameLayout[1]/androidx.drawerlayout.widget.DrawerLayout[1]/android.widget.RelativeLayout[1]/android.widget.FrameLayout[1]/android.widget.LinearLayout[1]/android.widget.FrameLayout[2]/android.widget.LinearLayout[1]/android.widget.ListView[1]/android.widget.LinearLayout[1]/android.widget.TextView[1]")  # 自选item
    optional_new = (By.XPATH, "//android.widget.TextView[@text='最新']")  # 最新
    optional_rise = (By.XPATH, "//android.widget.TextView[@text='涨跌']")  # 涨跌
    optional_count = (By.XPATH, "//android.widget.TextView[@text='总量']")  # 总量
    btnok = (By.ID, appPackage+':id/btn_confirm')

    # 行情页
    hq_name = (By.ID, appPackage+':id/tv_zqmc') # 行情title

    # 判定传统下单买入开仓按钮是否存在
    def find_traditional_buy(self):
        try:
            self.get_visible_element(self.traditional_buy, "传统下单--买入开仓")
        except Exception:
            my_log.error("委托风格不是传统下单")
            return False
        else:
            my_log.info("委托风格是传统下单")
            return True
    # 判定三键下单买入开仓按钮是否存在
    def find_three_buy(self):
        try:
            self.get_visible_element(self.orderbuy, "三键下单--买入开仓")
        except Exception:
            my_log.error("委托风格不是三键下单")
            return False
        else:
            my_log.info("委托风格是三键下单")
            return True
    # 切换传统/三键下单
    def change_style(self,style="三键"):
        self.get_clickable_element(self.more,"更多")
        self.get_clickable_element(self.entrust_style,"委托风格")
        el = self.get_textContains_ele(style)
        el.click()
        self.back()
        if style == "三键":
            try:
                self.get_visible_element(self.orderbuy,"三键买开")
            except:
                my_log.error("切换三键下单失败")
                return False
            else:
                return True
        elif style == "传统":
            try:
                self.get_visible_element(self.btn_kc, "传统买入")
            except:
                my_log.error("切换传统下单失败")
                return False
            else:
                return True
        else:
            my_log.error("order_page中change_style传参：%s错误"%style)
            return False

    # 点击加自选，返回自选名称
    def c_add_optional(self):
        self.get_clickable_element(self.add_optional,"加自选")
        return self.get_element_text(self.title,"期权下单页顶部title")
    def c_iv_right(self):
        self.get_clickable_element(self.iv_right,"切换合约")
    def c_more(self):
        self.get_clickable_element(self.more,"更多")
    def c_contract(self):
        self.get_clickable_element(self.contract,"合约代码输入框")
    def c_search(self):
        self.get_clickable_element(self.search,"合约搜索")
    def c_del_price(self):
        self.get_clickable_element(self.del_price,"减价格按钮")
    def c_add_price(self):
        self.get_clickable_element(self.add_price,"加价格按钮")
    def c_price(self):
        self.get_clickable_element(self.price,"价格输入框")
    # def el_price(self):
    #     el = self.get_visible_element(self.price,"价格")
    #     return el
    # def el_add_hand(self):
    #     el = self.get_visible_element(self.add_hand,"加数量按钮")
    #     return el
    def el_text(self,loc,desc =None):
        text = self.get_element_text(loc,desc)
        return text
    def c_price_dsj(self):
        self.get_clickable_element(self.price, "价格输入框")
        self.get_clickable_element(self.price_dsj,"对手价")
        self.get_clickable_element(self.dismiss, "收起键盘")
    def c_price_gdj(self):
        self.get_clickable_element(self.price, "价格输入框")
        self.get_clickable_element(self.price_gdj,"挂单价")
        self.get_clickable_element(self.dismiss, "收起键盘")
    def c_price_ztj(self):
        self.get_clickable_element(self.price, "价格输入框")
        self.get_clickable_element(self.price_ztj,"涨停价")
        self.get_clickable_element(self.dismiss, "收起键盘")
    def c_price_dtj(self):
        self.get_clickable_element(self.price, "价格输入框")
        self.get_clickable_element(self.price_dtj,"跌停价")
        self.get_clickable_element(self.dismiss, "收起键盘")
    def c_price_sjzx(self):
        self.get_clickable_element(self.price, "价格输入框")
        self.get_clickable_element(self.price_sjzx, "市价转限")
        self.get_clickable_element(self.dismiss, "收起键盘")
    def c_price_sjfok(self):
        self.get_clickable_element(self.price, "价格输入框")
        self.get_clickable_element(self.price_sjfok,"市价FOK")
        self.get_clickable_element(self.dismiss, "收起键盘")
    def c_price_sjioc(self):
        self.get_clickable_element(self.price, "价格输入框")
        self.get_clickable_element(self.price_sjioc,"市价IOC")
        self.get_clickable_element(self.dismiss, "收起键盘")
    def c_dismiss(self):
        self.get_clickable_element(self.dismiss,"收起键盘")
    def c_del_hand(self):
        self.get_clickable_element(self.del_hand,"减数量")
    def c_add_hand(self):
        self.get_clickable_element(self.price_ztj,"加数量")
    def c_hand(self,num=1):
        el = self.get_visible_element(self.hand,"数量输入框")
        time.sleep(1)
        el.send_keys(num)
    def c_FOK(self):
        text1 = self.get_element_text(self.price,"价格输入框")
        self.get_clickable_element(self.FOK,"FOK")
        text2 = self.get_element_text(self.price, "价格输入框")
        if text1 != text2:
            return True
        else:
            return False
    # 三键下单勾选备兑
    def c_covered(self):
        self.get_clickable_element(self.covered,"备兑")
        try:
            text1 = self.get_element_text(self.clock,"锁定解锁")
            text2 = self.get_element_text(self.covered_sell,"备兑开仓")
            text1 == "锁定解锁"
            text2 == "备兑开仓"
        except:
            my_log.error("备兑未勾选上")
            self.error_save_screenshot("备兑未勾选上")
            return False
        else:
            return True
    # 传统下单勾选备兑
    def c_traditional_covered(self):
        self.get_clickable_element(self.covered,"备兑")
    # 备兑开仓
    def c_covered_sell(self):
        self.get_clickable_element(self.covered_sell, "买开")
        self.remind()
        self.confirm()
        return self.entrust_submit()
    # 跳转锁定解锁
    def c_clock(self):
        self.get_clickable_element(self.clock, "锁定解锁")
        try:
            text = self.get_element_text(self.title,"锁定解锁title")
            text == "锁定解锁"
        except:
            my_log.error("未进入锁定解锁页")
            self.error_save_screenshot("未进入锁定解锁页")
            return False
        else:
            return True
    def c_orderbuy(self):
        self.get_clickable_element(self.orderbuy,"买开")
        self.remind()
        self.confirm()
        return self.entrust_submit()
    def c_traditional_buy(self):
        self.get_clickable_element(self.btn_kc,"开仓")
        self.get_clickable_element(self.traditional_buy, "传统买入")
        self.remind()
        self.confirm()
        return self.entrust_submit()
    def c_traditional_buy_flat(self):
        self.get_clickable_element(self.btn_pc, "平仓")
        self.get_clickable_element(self.traditional_buy, "传统买入平仓")
        self.remind()
        try:
            self.confirm()
            return self.entrust_submit()
        except:
            return False
    # 判断是否有下单确认，有就返回True，否则返回False
    def c_orderbuy_no_ture(self):
        self.get_clickable_element(self.orderbuy, "买开")
        # 是否有风险提示弹窗
        try:
            self.get_textContains_ele("提醒")
            self.toastok()
        except:
            my_log.info("没有风险提示")
        finally:
            try:
                self.get_clickable_element(self.btn_cancel,"取消下单",3)
            except:
                self.toastok()
                return False
            else:
                return True
    def c_ordersell(self):
        self.get_clickable_element(self.ordersell,"卖开")
        self.remind()
        self.confirm()
        return self.entrust_submit()
    def c_traditional_sell(self):
        self.get_clickable_element(self.btn_kc, "开仓")
        self.get_clickable_element(self.traditional_sell, "传统卖出")
        self.remind()
        self.confirm()
        return self.entrust_submit()
    def c_traditional_sell_flat(self):
        self.get_clickable_element(self.btn_pc, "平仓")
        self.get_clickable_element(self.traditional_sell, "传统卖出平仓")
        self.remind()
        try:
            self.confirm()
            return self.entrust_submit()
        except:
            return False
    def c_orderflat(self):
        price_text = self.get_element_text(self.flat_price,"持仓价格")
        if price_text == "没有找到元素":
            print("没有找到元素持仓价格")
        elif price_text == "无仓位":
            my_log.error("平仓的合约可用数量为0")
            self.error_save_screenshot("平仓的合约可用数量为0")
            self.get_clickable_element(self.orderflat, "平仓")
            self.toastok()
            return False
        else:
            self.get_clickable_element(self.orderflat, "平仓")
            self.confirm()
            return self.entrust_submit()
    def c_hold(self):
        self.get_clickable_element(self.hold,"持仓")
    # 点击持仓item，返回权力仓或义务仓
    def get_hold_type(self):
        try:
            self.get_clickable_element(self.hold,"持仓")
            self.get_clickable_element(self.hold_type,"持仓item")
        except:
            my_log.error("没有期权持仓")
            self.error_save_screenshot("没有期权持仓")
            return False
        else:
            type = self.get_element_text(self.hold_type,"持仓类型")
            return type
    # 点击持仓item,判断是否带入持仓信息
    def c_hold_item(self):
        try:
            self.get_clickable_element(self.hold_name,"持仓item")
        except:
            my_log.error("没有期权持仓")
            self.error_save_screenshot("没有期权持仓")
        else:
            hold_num = self.get_element_text(self.hold_num,"期权持仓数量")
            hold_name = self.get_element_text(self.hold_name,"期权持仓名字")
            num = self.get_element_text(self.hand,"数量输入框数量")
            title = self.get_element_text(self.title,"title")
            print(hold_num,hold_name,num,title)
            if hold_name == title and hold_num == num:
                return True
            else:
                my_log.error("带入持仓数据失败")
                self.error_save_screenshot("带入持仓数据失败")
                return False
    # 点击第一条持仓的持仓更多
    def c_hold_more(self):
        self.get_clickable_element(self.hold_more,"持仓更多")
        # self.get_clickable_element(self.hold_more, "持仓更多")
    def c_all_flat(self):
        self.driver.tap([(726,1920)])
        self.remind()
        self.confirm()
        return self.find_toast_text()
    def c_quick_back(self):
        self.driver.tap([(726, 2131)])
        self.remind()
        self.confirm()
        return self.find_toast_text()
    def c_cancel(self):
        self.get_clickable_element(self.cancel,"撤单")
    def c_all_cancel(self):
        self.get_clickable_element(self.all_cancel,"全部撤单")
        self.toastok()
        return self.entrust_submit()
    def c_confirm_cancel(self):
        self.get_clickable_element(self.confirm_cancel, "批量撤单")
        try:
            self.get_visible_element(self.checkbox_cancel,"撤单单选框")
        except Exception as e:
            my_log.error("没有可撤单")
            my_log.exception(e)
            self.error_save_screenshot("没有可撤单")
            return False
        else:
            my_log.info("有可撤单")
            self.get_clickable_element(self.checkbox_cancel, "撤单单选框")
            self.get_clickable_element(self.confirm_cancel, "批量撤单")
            return self.entrust_submit()

    def c_checkbox_cancle(self):
        self.get_clickable_element(self.checkbox_cancel,"撤单单选框")
    def c_entrust(self):
        self.get_clickable_element(self.entrust,"委托")
        try:
            self.get_visible_element(self.state,"状态")
        except Exception:
            my_log.error("进入委托页失败")
            self.error_save_screenshot("进入委托页失败")
            return False
        else:
            return True
    def c_deal(self):
        self.get_clickable_element(self.deal,"成交")
        try:
            self.get_visible_element(self.deal_time,"成交时间")
        except Exception:
            my_log.error("进入成交页失败")
            self.error_save_screenshot("进入成交页失败")
            return False
        else:
            return True
    def c_trend(self):
        self.get_clickable_element(self.trend, "走势")
        try:
            self.get_visible_element(self.trend_img,"走势图")
        except Exception:
            my_log.error("进入走势页失败")
            self.error_save_screenshot("进入走势页失败")
            return False
        else:
            return True
    # 双击走势跳转行情
    def double_c_trend(self):
        # 记录title合约名称
        name = self.get_element_text(self.title,"合约名称")
        width = self.driver.get_window_size()['width']
        height = self.driver.get_window_size()['height']
        print("%d,%d"%(width / 2,height * 0.7))
        self.driver.tap([(width / 2,height * 0.7)])
        self.driver.tap([(width / 2,height * 0.7)])
        try:
            hq_name = self.get_element_text(self.hq_name,"行情title")
        except:
            self.driver.tap([(width / 2, height * 0.7)])
            self.driver.tap([(width / 2, height * 0.7)])
            hq_name = self.get_element_text(self.hq_name, "行情title")
        assert name == hq_name
    def c_optional(self):
        self.get_clickable_element(self.optional, "自选")
        try:
            self.get_visible_element(self.optional_new,"最新")
        except Exception:
            my_log.error("进入自选页失败")
            self.error_save_screenshot("进入自选页失败")
            return False
        else:
            return True
    def c_optional_item(self):
        try:
            self.get_clickable_element(self.optional_item,"自选item")
        except:
            my_log.error("没有自选")
            self.error_save_screenshot("没有自选")
        else:
            optional_name = self.get_element_text(self.optional_item,"自选名字")
            title = self.get_element_text(self.title,"title")
            if optional_name == title:
                return True
            else:
                return False

    def order_page_back(self):
        self.back()
    # 点击最新价带入价格
    def c_now_price(self):
        self.get_clickable_element(self.price_now,"最新价")
        now_price = self.get_element_text(self.price_now,"最新价")
        price = self.get_element_text(self.price,"委托价")
        if float(now_price) == float(price):
            return True
        else:
            my_log.error("带入最新价操作失败，最新价价格:%s，带入之后价格:%s" % (now_price,price))
            return False
    # 点击涨停价带入价格
    def c_ztj_price(self):
        text = self.get_element_text(self.ztj_price, "涨停价")
        text1 = text.split(" ")[-1]
        # 点击涨停价
        self.get_clickable_element(self.ztj_price, "点击涨停价")
        # 获取价格输入框价格
        text2 = self.get_element_text(self.price, "价格")
        if float(text1) == float(text2):
            return True
        else:
            my_log.error("带入涨停价操作失败，涨停价价格:%s，带入之后价格:%s" % (text1, text2))
            return False
    # 点击跌停价带入价格
    def c_dtj_price(self):
        text = self.get_element_text(self.dtj_price, "跌停价")
        text1 = text.split(" ")[-1]
        # 点击跌停价
        self.get_clickable_element(self.dtj_price, "点击跌停价")
        # 获取价格输入框价格
        text2 = self.get_element_text(self.price, "价格")
        if float(text1) == float(text2):
            return True
        else:
            my_log.error("带入跌停价操作失败，跌停价价格:%s，带入之后价格:%s" % (text1, text2))
            return False
    # 点击卖一价带入价格
    def c_firstsell_price(self):
        text1 = self.get_element_text(self.fristsell_price, "卖一价")
        if text1 == "----":
            my_log.info("行情没有数据")
            return True
        else:
            # 点击买卖五档价
            self.get_clickable_element(self.fristsell_price, "卖一价")
            # 获取价格输入框价格
            text2 = self.get_element_text(self.price, "价格")
            # 行情中价格在不断变化，这里允许两次取的价格有一个较小的差距
            if math.fabs(float(text1)-float(text2)) < 0.0005:
                return True
            else:
                my_log.error("带入卖一价操作失败，卖一价格:%s，带入之后价格:%s" % (text1, text2))
                return False
    # 获取N列的数据(N大于等于2),适用于持仓排序
    def get_num(self,N):
        arr = []
        if N == 2:
            ele = self.get_visible_elements(self.hold_counts,"所有持仓可用数")
        elif N == 3:
            ele = self.get_visible_elements(self.hold_nowprices, "所有持仓成本")
        elif N == 4:
            ele = self.get_visible_elements(self.hold_yks, "所有盈亏")
        else:
            my_log.error("get_num参数需在2到4之间")
        # 由于获取到的列表第一个值可能是列头，所以从第二个值开始取值
        for i in range(1,len(ele)):
            arr.append(float(ele[i].text))
        return arr
    # 获取M+1行N列的数据,如M传0，则是第1行,适用于自选排序
    def get_num1(self, M, N):
        item_path = "//android.widget.FrameLayout[1]/android.widget.LinearLayout[1]/android.widget.FrameLayout[1]/androidx.drawerlayout.widget.DrawerLayout[1]/android.widget.RelativeLayout[1]/android.widget.FrameLayout[1]/android.widget.LinearLayout[1]/android.widget.FrameLayout[2]/android.widget.LinearLayout[1]/android.widget.ListView[1]/android.widget.LinearLayout[%s]/android.widget.HorizontalScrollView[1]/android.widget.LinearLayout[1]/android.widget.TextView[%s]" % (M+1, N-1)
        item = (By.XPATH, item_path)
        num = self.get_element_text(item, "%s行%s列的数据" % (M, N))
        try:
            float(num)
        except:
            my_log.error("%s行%s列没有数据,为：%s"% (M, N, num))
        return float(num)
    # 现价
    def c_hold_now_price(self):
        ele = self.get_textContains_ele("成本")
        ele.click()
    # 盈亏
    def c_hold_yk(self):
        ele = self.get_textContains_ele("盈亏",1)
        ele.click()
    # 持仓可用
    def c_hold_num(self):
        self.get_clickable_element(self.hold_num_name, "持仓可用")
    # 获取持仓可用数
    def get_hold_count(self):
        return int(self.get_element_text(self.hold_count,"可用数量"))
    # 最新
    def c_new_price(self):
        self.get_clickable_element(self.optional_new, "最新")
    # 涨跌
    def c_rise(self):
        self.get_clickable_element(self.optional_rise, "涨跌")
    # 总量
    def c_count(self):
        self.get_clickable_element(self.optional_count, "总量")
    # 降序判断,第N列数据，N>=0
    def desc(self, N):
        time.sleep(3)
        arr = []
        res = False
        arr = self.get_num(N)
        for i in range(len(arr)-2):
            if arr[i] >= arr[i + 1]:
                res = True
            else:
                my_log.error("此顺序非降序")
                self.error_save_screenshot("此顺序非降序")
                res = False
                break
        print(arr)
        return res
    # 升序判断，第N列数据，N>=0
    def asc(self, N):
        time.sleep(10)
        arr = []
        res = False
        arr = self.get_num(N)
        for i in range(len(arr) - 2):
            if arr[i] <= arr[i + 1]:
                res = True
            else:
                my_log.error("此顺序非升序")
                self.error_save_screenshot("此顺序非升序")
                res = False
                break
        print(arr)
        return res
    # 降序判断,第N列数据，N>=0
    def desc1(self, N):
        time.sleep(3)
        arr = []
        res = False
        for i in range(3):
            arr.append(self.get_num1(i, N))
        for i in range(2):
            if arr[i] >= arr[i + 1]:
                res = True
            else:
                my_log.error("此顺序非降序")
                self.error_save_screenshot("此顺序非降序")
                res = False
                break
        print(arr)
        return res

    # 升序判断，第N列数据，N>=0
    def asc1(self, N):
        time.sleep(10)
        arr = []
        res = False
        for i in range(3):
            arr.append(self.get_num1(i, N))
        for i in range(2):
            if arr[i] <= arr[i + 1]:
                res = True
            else:
                my_log.error("此顺序非升序")
                self.error_save_screenshot("此顺序非升序")
                res = False
                break
        print(arr)
        return res

    # 买
    def buy(self,num=1):
        self.c_hand(self,num)
        self.driver.find_element(*self.handnum).send_keys(num)
        self.driver.find_element(*self.orderbuy).click()
        self.driver.find_element(*self.btnok).click()
        self.toastok()
    # 卖
    def sell(self,num=1):
        self.driver.find_element(*self.handnum).send_keys(num)
        self.driver.find_element(*self.ordersell).click()
        self.driver.find_element(*self.btnok).click()
        self.toastok()
    # 平
    def flat(self,num=1):
        self.driver.find_element(*self.handnum).send_keys(num)
        self.driver.find_element(*self.orderflat).click()
        try:
            self.driver.find_element(*self.btnok).click()
            self.toastok()
        except:
            logging.error('该平仓的合约可用数量为0')
            getsreen=Common(self.driver)
            getsreen.getScreenShot('The number of closed positions is 0')
            return False
        else:
            return True

    # 选择涨停价格
    def high_price(self):
        self.driver.find_element(*self.price).click()
        self.driver.find_element(*self.highprice).click()
        self.driver.find_element(*self.close).click()