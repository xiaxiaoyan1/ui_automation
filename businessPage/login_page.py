__author__ = 'Administrator'
from appium.webdriver.common.mobileby import MobileBy
import time
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.common.exceptions import NoSuchElementException
from common.common_fun import Common
from common.collector_log import my_log
from appium import webdriver
from common.read_config import get_appPackage
'''
登录页面对象，实现系统的登录流程操作
核心操作流程：
关联元素：
    账号
    密码
    登录按钮
    确认按钮
'''
# CON_LOG='../config/log.conf'
# logging.config.fileConfig(CON_LOG)
# logging=logging.getLogger()
class Login(Common):
    appPackage = get_appPackage()
    #页面元素
    title = (MobileBy.ID, appPackage + ':id/tv_title')
    et_phone = (MobileBy.ID, appPackage + ':id/et_phone')
    et_smsCode = (MobileBy.ID, appPackage + ':id/et_smsCode')
    btn_getVerCode = (MobileBy.ID, appPackage + ':id/btn_getVerCode')
    btn_confirm = (MobileBy.XPATH, "//android.widget.Button[@text='确定']")
    et_user=(MobileBy.ID,appPackage+':id/et_user')
    et_pwd=(MobileBy.ID,appPackage+':id/et_pwd')
    btn_login_trade=(MobileBy.ID,appPackage+':id/btn_login_trade')
    confirm=(MobileBy.CLASS_NAME,'android.widget.Button')
    tv_account=(MobileBy.ID,appPackage+':id/tv_account')
    exit_login=(MobileBy.ID,appPackage+':id/btn_unLogin')
    login_fail_confirm=(MobileBy.ID,appPackage+':id/btn_toast_ok')
    login_expire_confirm=(MobileBy.ID,appPackage+':id/tv_comfirm')
    gptilte = (MobileBy.ID, appPackage+":id/tv_stock") # 股票title

    #元素的操作流
    def login(self,user,pwd):
        title_text = self.get_element_text(self.title,"title")

        if title_text == "手机号码激活":
            my_log.info("---------手机号码激活-----------")
            self.send_key(self.et_phone,"13123456789","输入手机号")
            self.get_clickable_element(self.btn_getVerCode,"获取验证码")
            self.send_key(self.et_smsCode,"123456","输入手机验证码")
            self.get_clickable_element(self.btn_confirm,"确定")
        my_log.info("---------登录-----------")
        my_log.info("账号：{}".format(user))
        self.get_presence_element(self.et_user,"账号").send_keys(user)
        # self.input_send_keys(self.et_user,user,"账号")
        my_log.info("密码：{}".format(pwd))
        # self.input_send_keys(self.et_pwd,pwd,"密码")
        self.get_presence_element(self.et_pwd,"账号").send_keys(pwd)
        my_log.info("点击登录")
        self.click_element(self.btn_login_trade,"登录")
        # for i in range(3):
        #     loc = (MobileBy.XPATH, "//*[@text='我知道了']")
        #     try:
        #         e = WebDriverWait(self.driver, 1, 0.5).until(EC.presence_of_element_located(loc))
        #         e.click()
        #     except:
        #         print("没有定位到系统弹窗")
        #     else:
        #         break
        for i in range(2):
            loc = (MobileBy.XPATH, "//*[@text='始终允许']")
            try:
                e = WebDriverWait(self.driver, 1, 0.5).until(EC.presence_of_element_located(loc))
                e.click()
            except:
                my_log.info("没有定位到授权弹框")
                # loc = (MobileBy.XPATH, "//*[@text='允许']")
                # try:
                #     e = WebDriverWait(self.driver, 1, 0.5).until(EC.presence_of_element_located(loc))
                #     e.click()
                # except:
                #     print("没有定位到系统授权弹窗")
                # else:
                #     break
            else:
                break
        for i in range(3):
            loc = (MobileBy.XPATH, "//*[@text='确定']")
            loc1 = (MobileBy.XPATH, "//*[@text='确认']")
            loc2 = (MobileBy.XPATH, "//*[@text=' 确定']")
            loc3 = (MobileBy.XPATH, "//*[@text=' 确认']")
            try:
                e = WebDriverWait(self.driver, 1, 0.5).until(EC.presence_of_element_located(loc))
                e.click()
            except:
                try:
                    e = WebDriverWait(self.driver, 1, 0.5).until(EC.presence_of_element_located(loc1))
                    e.click()
                except:
                    try:
                        e = WebDriverWait(self.driver, 1, 0.5).until(EC.presence_of_element_located(loc2))
                        e.click()
                    except:
                        try:
                            e = WebDriverWait(self.driver, 1, 0.5).until(EC.presence_of_element_located(loc3))
                            e.click()
                        except:
                            print("循环等待弹窗")
            else:
                pass
        try:
            self.get_visible_element(self.tv_account,"首页账号",30)
        except NoSuchElementException:
            self.click_element(self.login_fail_confirm,"登录失败弹框-确认")
            my_log.error("登录失败")
            return False
        else:
            my_log.info("登录成功")
            # self.error_save_screenshot("登录成功")
            return True
    # def gp_login(self,user,pwd):
    #     self.get_clickable_element(self.gptilte,"切换股票登录")
    #     my_log.info("---------登录股票-----------")
    #     my_log.info("账号：{}".format(user))
    #     self.get_presence_element(self.et_user, "账号").send_keys(user)
    #     # self.input_send_keys(self.et_user,user,"账号")
    #     my_log.info("密码：{}".format(pwd))
    #     # self.input_send_keys(self.et_pwd,pwd,"密码")
    #     self.get_presence_element(self.et_pwd, "账号").send_keys(pwd)
    #     my_log.info("点击登录")
    #     self.click_element(self.btn_login_trade, "登录")
    #     for i in range(2):
    #         loc = (MobileBy.XPATH, "//*[@text='确定']")
    #         loc1 = (MobileBy.XPATH, "//*[@text='确认']")
    #         loc2 = (MobileBy.XPATH, "//*[@text=' 确定']")
    #         loc3 = (MobileBy.XPATH, "//*[@text=' 确认']")
    #         try:
    #             e = WebDriverWait(self.driver, 1, 0.5).until(EC.presence_of_element_located(loc))
    #             e.click()
    #         except:
    #             try:
    #                 e = WebDriverWait(self.driver, 1, 0.5).until(EC.presence_of_element_located(loc1))
    #                 e.click()
    #             except:
    #                 try:
    #                     e = WebDriverWait(self.driver, 1, 0.5).until(EC.presence_of_element_located(loc2))
    #                     e.click()
    #                 except:
    #                     try:
    #                         e = WebDriverWait(self.driver, 1, 0.5).until(EC.presence_of_element_located(loc3))
    #                         e.click()
    #                     except:
    #                         print("循环等待弹窗")
    #         else:
    #             pass
    def unLogin(self):
        self.swipeup(0.7,0.3)
        self.get_clickable_element(self.exit_login,"退出登录")
        # self.driver.find_element_by_id(appPackage+':id/btn_unLogin').click()
        # self.click_element(self.exit_login,"退出登录")



