__author__ = 'Administrator'
from selenium.webdriver.common.by import By
from selenium.common.exceptions import NoSuchElementException
from common.common_fun import Common
from common.collector_log import my_log
from common.read_config import get_appPackage
import logging
class Exercise(Common):
    appPackage = get_appPackage()
    hb_exercise = (By.ID, appPackage+':id/rbtn_1')  # 合并行权
    wt_exercise = (By.ID, appPackage+':id/rbtn_2')  # 行权委托
    rengou_name = (By.ID, appPackage+':id/et_rengouhyname')  # 认购合约名称
    rengu_name = (By.ID, appPackage+':id/et_renguhyname')  # 认沽合约名称
    num_exercise = (By.ID, appPackage+':id/et_kxqnum')  # 行权数量
    ok_exercise = (By.ID, appPackage+':id/btn_ok')  # 行权确认
    hold = (By.XPATH, "//android.widget.RadioButton[@text='持仓']")  # 持仓
    mate_hold = (By.XPATH, "//android.widget.RadioButton[@text='可匹配行权持仓']")  # 可匹配行权持仓
    frist_contract = (By.XPATH, "//android.widget.ListView[@resource-id=appPackage+':id/lv_query']/android.widget.LinearLayout[1]")  # 第一个合约
    back = (By.ID, appPackage+':id/tv_back')
    def c_back(self):
        self.get_clickable_element(self.back,"返回")
    def exercise(self,contract_name):
        # 点击”合并行权“--”持仓“--”合约“--”可匹配行权持仓“--”合约“--”输入数量“--”行权确认“
        # // android.widget.TextView[ @ text = '50ETF购11月3000']
        xpath = "//android.widget.TextView[@text='%s']" %contract_name
        print(xpath)
        contract = (By.XPATH,xpath)  # 合约
        self.get_clickable_element(self.hb_exercise,"合并行权")
        self.get_clickable_element(self.hold,"持仓")
        try:
            # self.get_clickable_element(contract, "合约")
            self.swipe_ele(contract)
        except NoSuchElementException:
            my_log.error("合并行权没有持仓合约")
            self.error_save_screenshot("合并行权没有持仓合约")
        else:
            gou_text = self.get_element_text(self.rengou_name,"认购合约名称")
            gu_text = self.get_element_text(self.rengu_name, "认沽合约名称")
            if len(gou_text) == 0 and len(gu_text) == 0:
                my_log.error("合并行权没有持仓合约")
            else:
                try:
                    self.get_clickable_element(self.frist_contract, "合约")
                except NoSuchElementException:
                    my_log.error("合并行权没有可匹配持仓合约")
                    self.error_save_screenshot("合并行权没有可匹配持仓合约")
                    return False
                else:
                    self.clear_input(self.num_exercise, "清空行权数量输入框")
                    self.input_send_keys(self.num_exercise, 1, "输入行权数量")
                    self.get_clickable_element(self.ok_exercise, "行权确认")
                    self.confirm()
                    try:
                        self.toastok()
                    except:
                        print("没有toast确认弹窗")
                    return True



