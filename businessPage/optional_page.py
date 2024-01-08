
from appium.webdriver.common.mobileby import MobileBy
import logging,time
from common.read_config import get_appPackage
from common.collector_log import my_log
from common.common_fun import Common
class Optional(Common):
    appPackage = get_appPackage()
    edit = (MobileBy.ID, appPackage+':id/tv_right')
    zx = (MobileBy.ID, appPackage+':id/lv_zx')
    items = (MobileBy.ID, appPackage+':id/tv_name')
    iv_del = (MobileBy.ID, appPackage+':id/iv_del')
    # 删除所有自选
    def item_del(self):
        self.get_clickable_element(self.edit,"编辑")
        while True:
            try:
                self.find_element_noterror(self.iv_del, "删除")
            except:
                self.back()
                try:
                    time.sleep(2)
                    self.find_element_noterror(self.zx,"自选")
                except:
                    break
                else:
                    my_log.error("自选删除失败")
                    self.error_save_screenshot("自选删除失败")
                    break
            else:
                self.get_clickable_element(self.iv_del,"删除")
                self.toastok()
                time.sleep(1)
        self.back()
    # 传入股票名称，查看自选是否存在该股票
    def have_zx(self,name):
        contract_loc = (MobileBy.XPATH, "//android.widget.TextView[@text='%s']" % name)
        try:
            time.sleep(2)
            self.find_element(contract_loc,"自选股：%s"%name)
        except:
            return False
        else:
            return True
    # 查看存在的自选股名称，返回数组
    def zx_name_all(self):
        el = self.get_visible_elements(self.items,"自选股item")
        arr = []
        for i in el:
            arr.append(i.text)
        del(arr[0])
        return arr