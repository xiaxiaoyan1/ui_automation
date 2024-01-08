
from appium.webdriver.common.mobileby import MobileBy
import logging,time

from common.collector_log import my_log
from common.common_fun import Common
from common.read_config import get_appPackage
class TradeFirst(Common):
    appPackage = get_appPackage()
    tocap=(MobileBy.ID,appPackage+':id/ll_zjxq')
    CapTetail=(MobileBy.ID,appPackage+':id/tv_title')
    capBack=(MobileBy.ID,appPackage+':id/tv_back')
    position=(MobileBy.ID,appPackage+':id/tv_position')
    money_label1=(MobileBy.ID,appPackage+':id/tv_money_label1')
    clok=(MobileBy.ID,appPackage+':id/tv_lock')
    allancel=(MobileBy.ID,appPackage+':id/btn_all_chedan')
    btnclok=(MobileBy.ID,appPackage+':id/btn_perform')
    toexe=(MobileBy.XPATH,"//android.widget.TextView[@text='行权']")
    comb_report = (MobileBy.XPATH, "//android.widget.TextView[@text='组合申报']")
    merger_exe = (MobileBy.XPATH, "//android.widget.TextView[@text='合并行权']")
    style = (MobileBy.XPATH, "//android.widget.TextView[@text='委托风格']")
    password = (MobileBy.XPATH, "//android.widget.TextView[@text='修改交易密码']")
    password_zj = (MobileBy.XPATH, "//android.widget.TextView[@text='修改资金密码']")
    setup = (MobileBy.XPATH, "//android.widget.TextView[@text='委托设置']")
    tosearch=(MobileBy.ID,appPackage+':id/tv_query')
    order=(MobileBy.ID,appPackage+':id/tv_order')
    cancelorder = (MobileBy.ID, appPackage+':id/tv_cancelOrder')
    first_page = (MobileBy.XPATH, "//android.widget.RadioButton[@text='首页']")
    optional_page = (MobileBy.XPATH, "//android.widget.RadioButton[@text='自选']")
    hq_page = (MobileBy.XPATH, "//android.widget.RadioButton[@text='行情']")
    trade_page = (MobileBy.XPATH, "//android.widget.RadioButton[@text='交易']")
    setup_page = (MobileBy.XPATH, "//android.widget.RadioButton[@text='设置']")
    def to_first_page(self):
        self.get_clickable_element(self.first_page,"首页")
    def to_optional_page(self):
        self.get_clickable_element(self.optional_page,"自选")
    def to_hq_page(self):
        self.get_clickable_element(self.hq_page,"行情")
    def to_trade_page(self):
        self.get_clickable_element(self.trade_page,"交易")
    def to_setup_page(self):
        self.get_clickable_element(self.setup_page,"设置")
    def to_capital(self):
        # time.sleep(5)
        # self.driver.find_element_by_id(appPackage+':id/ll_zjxq').click()
        self.get_clickable_element(self.tocap,"资金详情")
        try:
            # self.driver.find_element(*self.CapTetail)
            self.get_visible_element(self.CapTetail,"资金详情页面标题")
        except Exception:
            my_log.error("进入资金详情页面失败")
            return False
        else:
            my_log.info("进入资金详情页面成功")
            return True

    def to_search(self):
        self.get_clickable_element(self.tosearch,"查询")
    def to_clok(self):
        self.get_clickable_element(self.clok,"进入锁定解锁页")
    def to_position(self):
        self.get_clickable_element(self.position,"持仓")
    def to_cancelOrder(self):
        self.get_clickable_element(self.cancelorder,"进入撤单页")
    def to_order(self):
        self.get_clickable_element(self.order,"下单")
    def to_comb_report(self):
        self.get_clickable_element(self.comb_report, "组合申报")
    def to_merger_exe(self):
        self.get_clickable_element(self.merger_exe, "合并行权")
    def to_style(self):
        self.get_clickable_element(self.style,"委托风格")
    def to_password(self):
        # 滑动到底部
        self.swipeup(0.7, 0.3)
        try:
            self.get_clickable_element(self.password,"修改交易密码")
        except:
            my_log.error("该券商不支持修改密码")
            assert True
    def to_password_zj(self):
        # 滑动到底部
        self.swipeup(0.7, 0.3)
        try:
            self.get_clickable_element(self.password_zj,"修改资金密码")
        except:
            my_log.error("该券商不支持修改资金密码")
            assert True
    def to_setup(self):
        # 滑动到底部
        self.swipeup(0.7,0.3)
        self.get_clickable_element(self.setup,"委托设置")
    def to_exercise(self):
        # self.driver.find_element(*self.toexe).click()
        self.get_clickable_element(self.toexe,"行权")



if __name__ == '__main__':
    tradehome = TradeFirst(self.driver)
    # tradehome.to_position()
    # print("点击下单按钮")
    tradehome.to_order()