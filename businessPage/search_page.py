__author__ = 'Administrator'
from appium.webdriver.common.mobileby import MobileBy
from selenium.common.exceptions import NoSuchElementException
from common.common_fun import Common
from common.collector_log import my_log
from common.read_config import get_appPackage
class Search(Common):
    appPackage = get_appPackage()
    #查询页面设计涉及元素
    daytrade=(MobileBy.XPATH,'//android.widget.TextView[@text="当日成交"]')
    tradetime=(MobileBy.XPATH,'//android.widget.TextView[@text="成交时间"]')
    dayentrust=(MobileBy.XPATH,'//android.widget.TextView[@text="当日委托"]')
    dayPrice=(MobileBy.XPATH,'//android.widget.TextView[@text="委托价"]')
    histrade=(MobileBy.XPATH,'//android.widget.TextView[@text="历史成交"]')
    tradedate=(MobileBy.XPATH,'//android.widget.TextView[@text="成交日期"]')
    dayexe=(MobileBy.XPATH,'//android.widget.TextView[@text="当日行权被指派"]')
    exeprice=(MobileBy.XPATH,'//android.widget.TextView[@text="行权价格"]')
    hisexe=(MobileBy.XPATH,'//android.widget.TextView[@text="历史行权指派"]')
    histime=(MobileBy.ID,appPackage+':id/tv_start')
    hiscapflow=(MobileBy.XPATH,'//android.widget.TextView[@text="历史资金流水"]')
    flowdata=(MobileBy.ID,appPackage+':id/tv_start')
    clok=(MobileBy.XPATH,'//android.widget.TextView[@text="锁定解锁查询"]')
    target=(MobileBy.XPATH,'//android.widget.TextView[@text="标的代码"]')
    dayexetru=(MobileBy.XPATH,'//android.widget.TextView[@text="当日行权委托查询"]')
    dayexeprice=(MobileBy.XPATH,'//android.widget.TextView[@text="委托数量"]')
    grouPosition=(MobileBy.XPATH,'//android.widget.TextView[@text="组合策略持仓查询"]')
    availAmount=(MobileBy.XPATH,'//android.widget.TextView[@text="可用数量"]')
    groupinfor=(MobileBy.XPATH,'//android.widget.TextView[@text="组合策略信息查询"]')
    groupcode=(MobileBy.XPATH,'//android.widget.TextView[@text="组合策略编码"]')
    groupflow=(MobileBy.XPATH,'//android.widget.TextView[@text="组合委托流水查询"]')
    groupdata=(MobileBy.XPATH,'//android.widget.TextView[@text="委托日期"]')
    hisflow=(MobileBy.XPATH,'//android.widget.TextView[@text="历史组合委托流水查询"]')
    hisdata=(MobileBy.XPATH,'//android.widget.TextView[@text="委托日期"]')

#查询当日成交
    def search_day_transaction(self):
        # self.driver.find_element(*self.daytrad).click()
        # self.get_clickable_element(self.daytrad,"查询当日成交").click()
        self.get_clickable_element(self.daytrade,"查询当日成交")
        try:
            # self.driver.find_element(*self.tradteail)
            self.get_visible_element(self.tradetime,"当日成交详情")
        except NoSuchElementException:
            my_log.error("进入当日成交页面失败")
            return False
        else:
            my_log.info("进入当日成交页面成功")
            return True
#查询当日委托
    def search_day_entrust(self):
        # self.driver.find_element(*self.dayentrust).click()
        self.get_clickable_element(self.dayentrust,"当日委托")
        try:
            # self.driver.find_element(*self.dayPrice)
            self.get_presence_element(self.dayPrice)
        except NoSuchElementException:
            my_log.error("进入当日委托页面失败")
            return False
        else:
            my_log.info("进入当日委托页面成功")
            return True
#查询历史成交
    def search_history_transaction(self):
        # self.driver.find_element(*self.histrade).click()
        self.get_clickable_element(self.histrade,"历史成交")
        try:
            self.toastok()
        except:
            pass
        try:
            self.get_visible_element(self.tradedate,"成交日期")
        except NoSuchElementException:
            my_log.error("进入历史成交页面失败")
            return False
        else:
            my_log.info('进入历史成交页面成功')
            return True
#查询当日行权被指派
    def search_day_exercise(self):
        # self.driver.find_element(*self.dayexe).click()
        self.get_clickable_element(self.dayexe,"当日行权被指派")
        try:
            self.get_visible_element(self.exeprice,"当日行权被指派")
            # self.driver.find_element(*self.exeprice)
        except NoSuchElementException:
            my_log.error("进入当日行权被指派失败")
            return False
        else:
            my_log.info("进入当日行权被指派成功")
            return True
#查询历史行权指派
    def search_history_exercise(self):
        self.get_clickable_element(self.hisexe,"历史行权指派")
        try:
            self.toastok()
        except:
            pass
        try:
            self.get_visible_element(self. histime,"历史行权指派")
        except NoSuchElementException:
            my_log.error("进入历史行权指派页面失败")
            return False
        else:
            my_log.info("进入历史行权指派页面成功")
            return True
#历史资金流水
    def search_hiscapitalflow(self):
        # self.driver.find_element(*self.hiscapflow).click()
        self.get_clickable_element(self.hiscapflow,"历史资金流水")
        try:
            self.get_visible_element(self. flowdata,"历史资金流水")
            # self.driver.find_element(*self.flowdata)
        except NoSuchElementException:
            my_log.error("进入历史资金流水页面失败")

            return False
        else:
            my_log.info("进入历史资金流水页面成功")

            return True
#查询锁定解锁
    def search_clok_unclok(self):
        self.get_clickable_element(self.clok,"锁定解锁查询")
        try:
            self.get_visible_element(self.target,"锁定解锁查询")
            # self.driver.find_element(*self.target)
        except NoSuchElementException:
            my_log.error("锁定解锁查询失败")

            return False
        else:
            my_log.info("锁定解锁查询成功")

            return True
#查询当日行权委托查询
    def search_day_exentrust(self):
        # self.driver.find_element(*self.dayexetru).click()
        self.get_clickable_element(self.dayexetru,"当日行权委托查询")
        try:
            # self.driver.find_element(*self.dayexeprice)
            self.get_visible_element(self.dayexeprice,"当日行权委托查询")
        except NoSuchElementException:
            my_log.error("当日行权委托查询失败")

            return False
        else:
            my_log.info("当日行权委托查询成功")

            return True

# #当日风险通知查询
#     def search_risk(self):
#         self.driver.find_element_MobileBy_xpth('//*[@text=当日风险通知]').click()

#组合策略持仓查询
    def search_group_Position(self):
        #self.driver.find_element(*self.grouPosition).click()
        self.get_clickable_element(self.grouPosition,"组合策略持仓查询")
        try:
            # self.driver.find_element(*self.availAmount)
            self.get_visible_element(self.availAmount,"组合策略持仓查询")
        except NoSuchElementException:
            my_log.error("组合策略持仓查询失败")

            return False
        else:
            my_log.info("组合策略持仓查询成功")

            return True
#组合策略信息查询
    def search_group_message(self):
        #self.driver.find_element_MobileBy_xpth(*self.groupinfor).click()
        self.get_clickable_element(self.groupinfor,"组合策略信息查询")
        try:
            #self.driver.find_element(*self.groupcode)
            self.get_visible_element(self.groupcode,"组合策略信息查询")
        except NoSuchElementException:
            my_log.error("组合策略信息查询失败")

            return False
        else:
            my_log.info("组合策略信息查询成功")

            return True
#组合委托流水查询

    def search_stream(self):
        #self.driver.find_element(*self.groupflow).click()
        self.get_clickable_element(self.groupflow,"组合委托流水查询")
        try:
            #self.driver.find_element(*self.groupdata)
            self.get_visible_element(self.groupdata,"组合委托流水查询")
        except NoSuchElementException:
            my_log.error("组合委托流水查询失败")

            return False
        else:
            my_log.info("组合委托流水查询成功")

            return True
#历史组合委托流水查询
    def search_history_stream(self):
        #self.driver.find_element(*self.hisflow).click()
        self.get_clickable_element(self.hisflow,"组合委托流水查询")
        try:
            self.toastok()
        except:
            pass
        try:
            #self.driver.find_element(*self.hisdata)
            self.get_visible_element(self.hisdata,"组合委托流水查询")
        except NoSuchElementException:
            my_log.error("组合委托流水查询失败")
            return False
        else:
            my_log.info("组合委托流水查询成功")
            return True
