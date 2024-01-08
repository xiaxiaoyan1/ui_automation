__author__ = 'Administrator'
from selenium.webdriver.common.by import By
from selenium.common.exceptions import NoSuchElementException
from common.common_fun import Common
import logging,time
from common.read_config import get_appPackage
from common.collector_log import my_log
class Exercise(Common):
    appPackage = get_appPackage()
    xq = (By.ID, appPackage+':id/rbtn_1')  # 顶部行权
    tv_name = (By.ID, appPackage+':id/tv_name')  # 行权合约名称
    tv_hyName = (By.ID, appPackage+':id/tv_name')  # 协议行权合约名称
    exenum=(By.ID,appPackage+':id/et_num')   # 行权量
    exebtn=(By.ID,appPackage+':id/btn_ok') # 行权按钮
    hold = (By.XPATH, "//android.widget.RadioButton[@text='持仓']")  # 行权持仓
    contract = (By.XPATH, "//android.widget.ListView[@resource-id='"+appPackage+":id/lv_query']/android.widget.LinearLayout[1]")  # 合约
    assign = (By.XPATH, "//android.widget.RadioButton[@text='被指派']")  # 被指派
    sfsl = (By.XPATH, "//android.widget.TextView[@text='收付数量']")  # 收付数量
    changeagree=(By.ID,appPackage+':id/rbtn_2') #协议行权
    policy_value = (By.ID,appPackage+':id/et_clValue') #策略值
    agree_num = (By.ID,appPackage+':id/et_num') #协议数量
    agree_btn = (By.ID,appPackage+':id/btn_submit') #协议行权确认
    entrust=(By.ID,appPackage+':id/rbtn_3') #行权委托
    entrust_time=(By.XPATH,"//android.widget.TextView[@text='委托时间']") #委托时间
    change = (By.XPATH, "//android.widget.RadioButton[@text='修改']")  # 修改
    entrustdata=(By.XPATH,'//*[@text=当日成交]')
    entrustitem = (By.XPATH, "//android.widget.ListView[@resource-id='"+appPackage+":id/lv_query']/android.widget.LinearLayout[1]")
    cancle = (By.ID, appPackage + ':id/iv_right')  # 撤单
#行权确认
    def exercise(self,num=1):
        self.get_clickable_element(self.xq,"顶部行权")
        for i in range(5):
            text = self.get_element_text(self.tv_name, "行权合约名称")
            if len(text) == 0:
                time.sleep(2)
            else:
                break
        try:
            self.get_visible_element(self.contract,"合约")
        except Exception:
            my_log.error("没有合约")
            self.error_save_screenshot("没有合约")
            return False
        else:
            self.input_send_keys(self.exenum,num,"行权量")
            self.get_clickable_element(self.exebtn,"行权")
            try:
                self.toastok()
            except:
                print("没有虚值toast确认弹窗")
            return True
            self.confirm()
            try:
                self.toastok()
            except:
                print("没有toast确认弹窗")
            return True
#被指派
    def ass(self):
        self.get_clickable_element(self.xq,"顶部行权")
        self.get_clickable_element(self.assign, "被指派")
        try:
            self.get_visible_element(self.sfsl,"收付数量")
        except Exception:
            my_log.error("进入被指派页面失败")
            self.error_save_screenshot("进入被指派页面失败")
            return False
        else:
            return True

#协议行权
    def agree_exercise(self,num=1):
        self.get_clickable_element(self.changeagree,"协议行权")
        for i in range(5):
            text = self.get_element_text(self.tv_hyName, "协议行权合约名称")
            if len(text) == 0:
                time.sleep(2)
            else:
                break
        try:
            self.get_visible_element(self.contract, "合约")
        except Exception:
            my_log.error("没有合约")
            self.error_save_screenshot("没有合约")
            return False
        else:
            self.input_send_keys(self.policy_value,num,"策略值")
            self.get_clickable_element(self.agree_btn,"协议行权确认")
            self.confirm()
            return True
# 协议行权修改
    def change_exercise(self,num=1):
        self.get_clickable_element(self.changeagree, "协议行权")
        self.get_clickable_element(self.change,"修改")
        for i in range(10):
            text = self.get_element_text(self.policy_value, "策略值")
            if len(text) == 0:
                time.sleep(2)
            else:
                break
        try:
            self.get_visible_element(self.contract, "合约")
        except Exception:
            my_log.error("没有合约")
            self.error_save_screenshot("没有合约")
            return False
        else:
            self.input_send_keys(self.agree_num,num,"协议行权数量")
            self.get_clickable_element(self.agree_btn,"协议行权确认")
            self.confirm()
            return True
# 行权委托-撤单
    def entrust_exercise(self):
        self.get_clickable_element(self.entrust,"行权委托")
        try:
            self.get_visible_element(self.entrust_time,"委托时间")
        except Exception:
            my_log.error("进入行权委托页面失败")
            self.error_save_screenshot("进入行权委托页面失败")
            return False
        else:
            self.get_clickable_element(self.entrustitem,"行权委托记录")
            self.get_clickable_element(self.cancle,"撤单按钮")
            self.confirm()
            self.toastok()
            return True


