from common.collector_log import my_log
from selenium.webdriver.common.by import By
from selenium.common.exceptions import NoSuchElementException
from common.common_fun import Common
from common.read_config import get_appPackage
class ChangePwd(Common):
    appPackage = get_appPackage()
    et_pwd = (By.ID, appPackage+':id/et_pwd')
    new_pwd = (By.ID, appPackage+':id/et_newPwd')
    confirm_pwd = (By.ID, appPackage+':id/et_confirmPwd')
    comfrim_btn = (By.XPATH, "//android.widget.Button[@text='确定']")


    def change_pwd(self,etpwd,newpwd,newpwd2):
        self.input_send_keys(self.et_pwd,etpwd,"输入原密码")
        self.input_send_keys(self.new_pwd,newpwd, "输入新密码")
        self.input_send_keys(self.confirm_pwd,newpwd2, "新密码确认")
        self.get_clickable_element(self.comfrim_btn, "确定")

