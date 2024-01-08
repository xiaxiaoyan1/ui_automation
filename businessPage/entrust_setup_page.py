__author__ = 'Administrator'
from common.collector_log import my_log
from selenium.webdriver.common.by import By
from selenium.common.exceptions import NoSuchElementException
from common.common_fun import Common
from common.read_config import get_appPackage
class Setup(Common):
    appPackage = get_appPackage()
    defaultPrice = (By.ID,appPackage+':id/rl_defaultPrice') # 默认价格
    opponentPrice = (By.XPATH, "//android.widget.TextView[@resource-id='"+appPackage+":id/tv_name' and @text='对手价']")  # 对手价
    orderPrice = (By.XPATH, "//android.widget.TextView[@resource-id='"+appPackage+":id/tv_name' and @text='挂单价']")  # 挂单价
    defaultNumber = (By.ID, appPackage+':id/tv_num')  # 默认开仓数
    defaultNumber_input = (By.ID, appPackage+':id/et_input')  # 默认开仓数输入框
    add_defaultNumber = (By.ID, appPackage+':id/rl_add_defaultNumber')  # 默认下单增加数量
    order_switch = (By.ID, appPackage+':id/order_switch')  # 下单确认开关
    risk_switch = (By.ID, appPackage+':id/risk_switch')  # 下单风险提示开关
    rl_defaultTime = (By.ID, appPackage+':id/tv_defaultTime')  # 拆单间隔时间
    xj_defaultDivide_switch = (By.ID, appPackage+':id/xj_defaultDivide_switch')  # 限价拆单开关
    rl_xj_defaultDivideNum = (By.ID, appPackage+':id/tv_xj_Dividenum')  # 限价每单拆单张数
    sj_defaultDivide_switch = (By.ID, appPackage+':id/sj_defaultDivide_switch')  # 市价拆单开关设置
    rl_sj_defaultDivideNum = (By.ID, appPackage+':id/tv_sj_defaultDividenum')  # 市价每单拆单张数
    rl_positionFilterConditions = (By.ID, appPackage+':id/tv_positionFilterConditions')  # 持仓过滤条件
    position_rbtn_1 = (By.ID, appPackage+':id/rbtn_1')  # 已平仓合约保留一天
    position_rbtn_2 = (By.ID, appPackage+':id/rbtn_2')  # 已平仓合约不保留
    rl_setting_login_time = (By.ID, appPackage+':id/tv_setting_time')  # 登录时长
    login_rbtn_1 = (By.ID, appPackage+':id/rbtn_1')  # 始终登录
    login_rbtn_2 = (By.ID, appPackage+':id/rbtn_2')  # 15分钟后自动退出
    login_rbtn_3 = (By.ID, appPackage+':id/rbtn_3')  # 30分钟后自动退出

    def setprice_dsj(self):
        self.get_clickable_element(self.defaultPrice,"默认价格")
        self.get_clickable_element(self.opponentPrice,"对手价")

    def setprice_gdj(self):
        self.get_clickable_element(self.defaultPrice, "默认价格")
        self.get_clickable_element(self.orderPrice, "挂单价")
    def setDefaultNumber(self,num=1):
        self.get_clickable_element(self.defaultNumber, "默认开仓数")
        self.input_send_keys(self.defaultNumber_input,num,"默认开仓数输入框")
        self.confirm()
        defaultNumber_text = self.get_element_text(self.defaultNumber, "默认开仓数")
        assert int(defaultNumber_text) == int(num)
    def setadd_defaultNumber(self,num=1):
        self.get_clickable_element(self.add_defaultNumber, "默认下单增加数量")
        self.input_send_keys(self.defaultNumber_input, num, "默认下单增加数量输入框")
        self.confirm()
    def setorder_switch(self):
        self.get_clickable_element(self.order_switch, "下单确认开关")
    def setrisk_switch(self):
        self.get_clickable_element(self.risk_switch,"下单风险提示开关")
    def setrl_defaultTime(self,num=400):
        self.get_clickable_element(self.rl_defaultTime, "拆单间隔时间")
        self.input_send_keys(self.defaultNumber_input, num, "拆单间隔时间输入框")
        self.confirm()
    def setxj_defaultDivide_switch(self):
        self.swipeup(0.7,0.1)
        self.get_clickable_element(self.xj_defaultDivide_switch, "限价拆单开关")
    def setrl_xj_defaultDivideNum(self,num=50):
        self.swipeup(0.7, 0.1)
        self.get_clickable_element(self.rl_xj_defaultDivideNum, "限价每单拆单张数")
        self.input_send_keys(self.defaultNumber_input, num, "限价每单拆单张数输入框")
        self.confirm()
    def setsj_defaultDivide_switch(self):
        self.swipeup(0.7, 0.1)
        self.get_clickable_element(self.sj_defaultDivide_switch, "市价拆单开关")
    def setrl_sj_defaultDivideNum(self,num=10):
        self.swipeup(0.7, 0.1)
        self.get_clickable_element(self.rl_sj_defaultDivideNum, "市价每单拆单张数")
        self.input_send_keys(self.defaultNumber_input, num, "市价每单拆单张数输入框")
        self.confirm()
    def setposition_save(self):
        self.swipeup(0.7, 0.1)
        text = self.get_element_text(self.rl_positionFilterConditions,"持仓过滤条件text")
        self.get_clickable_element(self.rl_positionFilterConditions, "持仓过滤条件")
        if text == "已平仓合约保留一天":
            self.get_clickable_element(self.position_rbtn_2, "已平仓合约不显示")
            return "已平仓合约不显示"
        else:
            self.get_clickable_element(self.position_rbtn_1,"已平仓合约保留一天")
            return "已平仓合约保留一天"

    # def setposition_notsave(self):
    #     self.swipeup(0.7, 0.1)
    #     self.get_clickable_element(self.rl_positionFilterConditions, "持仓过滤条件")
    #     self.get_clickable_element(self.position_rbtn_2, "已平仓合约不保留")

    def setlogin_always(self):
        self.swipeup(0.8, 0.1)
        self.get_clickable_element(self.rl_setting_login_time, "登录时长")
        self.get_clickable_element(self.login_rbtn_1, "始终登录")
        # try:
        #     self.get_visible_element(self.login_rbtn_1, "始终登录")
        # except NoSuchElementException:
        #     my_log.info("改变登录时长条件成功")
        #     return True
        # else:
        #     my_log.info("登录时长已是始终登录")
        #     self.driver.tap(100, 100)
        #     return False
    def setlogin_15(self):
        self.swipeup(0.8, 0.1)
        self.get_clickable_element(self.rl_setting_login_time, "登录时长")
        self.get_clickable_element(self.login_rbtn_2, "15分钟后自动退出")
        # try:
        #     self.get_visible_element(self.login_rbtn_2, "15分钟后自动退出")
        # except NoSuchElementException:
        #     my_log.info("改变登录时长条件成功")
        #     return True
        # else:
        #     my_log.info("登录时长已是15分钟后自动退出")
        #     self.driver.tap(100, 100)
        #     return False
    def setlogin_30(self):
        self.swipeup(0.8, 0.1)
        self.get_clickable_element(self.rl_setting_login_time, "登录时长")
        self.get_clickable_element(self.login_rbtn_3, "30分钟后自动退出")
        # try:
        #     self.get_visible_element(self.login_rbtn_3, "30分钟后自动退出")
        # except NoSuchElementException:
        #     my_log.info("改变登录时长条件成功")
        #     return True
        # else:
        #     my_log.info("登录时长已是30分钟后自动退出")
        #     self.driver.tap(100, 100)
        #     return False
    def page_back(self):
        self.back()
    def el_text(self,loc,desc =None):
        text = self.get_element_text(loc,desc)
        return text