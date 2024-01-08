__author__ = 'Administrator'
from appium.webdriver.common.mobileby import MobileBy
import time
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.common.exceptions import NoSuchElementException
from common.common_fun import Common
from common.collector_log import my_log
from common.read_config import get_appPackage
class Position(Common):
    appPackage = get_appPackage()
    tip=(MobileBy.ID,appPackage+':id/tv_filed1')
    order=(MobileBy.ID,appPackage+':id/tv_order')
    hq=(MobileBy.ID,appPackage+':id/tv_hq')
    detail=(MobileBy.ID,appPackage+':id/tv_detail')
    pc=(MobileBy.ID,appPackage+':id/tv_qp')
    bond=(MobileBy.XPATH,'//android.widget.TextView[@text="保证金"]')
    hqcode=(MobileBy.ID,appPackage+':id/tv_zqmc')
    price=(MobileBy.ID,appPackage+':id/tv_price')
    buy=(MobileBy.ID,appPackage+':id/tv_price')
    p_price = (MobileBy.ID,appPackage+':id/tv_cPrice')  # 平仓价格
    sort = (MobileBy.ID,appPackage+':id/iv_sort')  # 排序图标

    def tipline(self):
        self.get_clickable_element(self.tip,"点击持仓行")
        
    def tiporder(self):
        # self.driver.find_element(*self.order).click()
        self.get_clickable_element(self.order,"下单")
        try:
            #self.driver.find_element(*self.price)
            self.get_visible_element(self.price,"持仓-下单")
        except NoSuchElementException:
            my_log.error("持仓进入下单页面失败")
            return False
        else:
            my_log.info("持仓进入下单页面成功")
            return True
    def sort_icon(self):
        try:
            self.find_element_noterror(self.sort,"排序图标")
            return True
        except:
            my_log.info("没有排序图标")
            return False
    # 判断二级菜单是否展开
    def secondary_menu(self):
        try:
            self.find_element_noterror(self.order,"二级菜单")
            return True
        except:
            my_log.error("没有展开二级菜单")
            return False

#持仓二级菜单进入行情
    def tiphq(self):
        #self.driver.find_element(*self.hq).click()
        self.get_clickable_element(self.hq,"行情")
        try:
            #self.driver.find_element(*self.hqcode)
            self.get_visible_element(self.hqcode,"持仓-行情")
        except NoSuchElementException:
            my_log.error("持仓进入行情页面失败")
            return False
        else:
            my_log.info("持仓进入行情页面成功")
            return True

#持仓二级菜单进入详情
    def tipdetail(self):
        #self.driver.find_element(*self.detail).click()
        self.get_clickable_element(self.detail,"详情")
        try:
            # self.driver.find_element(*self.bond)
            self.get_visible_element(self.bond,"持仓-详情")
        except NoSuchElementException:
            my_log.error("持仓进入详情页面失败")
            return False
        else:
            my_log.info("持仓进入详情页面成功")
            return True
#持仓二级菜单进入平仓
    def tippc(self):
        #self.driver.find_element(*self.pc).click()
        self.get_clickable_element(self.pc,"平仓")
        try:
            #self.driver.find_element(*self.buy).click()
            self.get_visible_element(self.p_price,"持仓-平仓价格")
        except NoSuchElementException:
            my_log.info("持仓进入平仓页面失败")
            return False
        else:
            my_log.info("持仓进入平仓页面成功")
            return True


