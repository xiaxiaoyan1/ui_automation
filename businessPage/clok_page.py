__author__ = 'Administrator'

import time
from selenium.webdriver.common.by import By
from selenium.common.exceptions import NoSuchElementException
from common.common_fun import Common
from common.collector_log import my_log
from common.read_config import get_appPackage
class ClokUnclok(Common):
    appPackage = get_appPackage()
    add=(By.ID,appPackage+':id/btn_sub_add')
    delete=(By.ID,appPackage+':id/btn_sub_delete')
    amount=(By.ID,appPackage+':id/et_sdsl')
    btnclok=(By.ID,appPackage+':id/btn_perform')
    clok_btn = (By.ID, appPackage+':id/rbtn_1')
    unclok_btn=(By.ID,appPackage+':id/rbtn_2')
    kj_num = (By.ID, appPackage+':id/et_kssl') #可解数量框
    code = (By.ID, appPackage+':id/et_zqdm')  # 证券代码


#增加锁定数量操作
    def addclok(self):
        self.get_clickable_element(self.add,"增加锁定数量")

#减少锁定数量
    def deleteclok(self):
        self.get_clickable_element(self.delete,"减少锁定数量")

#点击锁定、解锁按钮
    def clok_click(self):
        self.get_clickable_element(self.btnclok,"锁定/解锁按钮")

#切换到解锁
    def unclok(self):
        self.get_clickable_element(self.unclok_btn,"解锁页")
#锁定操作
    def clok_confirm(self,num=10000):
        self.get_clickable_element(self.clok_btn, "锁定页")
        text = ""
        for i in range(5):
            text = self.get_element_text(self.code, "证券代码")
            if len(text) == 0:
                time.sleep(2)
            else:
                break
        if len(text) == 0:
            return False
        else:
            self.clear_input(self.amount,"清空数量框")
            self.input_send_keys(self.amount,num,"输入锁定数量")
            self.get_clickable_element(self.btnclok, "锁定/解锁按钮")
            self.confirm()
            return True
#解锁操作
    def unclok_confirm(self,num=10000):
        self.get_clickable_element(self.unclok_btn, "解锁页")
        for i in range(10):
            text = self.get_element_text(self.code, "证券代码")
            if len(text) == 0:
                time.sleep(2)
            else:
                break
        text = self.get_element_text(self.kj_num,"可解数量")
        if text == "0":
            my_log.info("可解数量为0")
            return False
        else:
            self.clear_input(self.amount, "清空数量框")
            self.input_send_keys(self.amount, num,"输入解锁数量")
            self.get_clickable_element(self.btnclok, "锁定/解锁按钮")
            self.confirm()
            return True










