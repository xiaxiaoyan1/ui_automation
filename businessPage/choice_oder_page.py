__author__ = 'Administrator'
from selenium.webdriver.common.by import By
from selenium.common.exceptions import NoSuchElementException
import pytest
from common.common_fun import Common
from common.read_config import get_appPackage
class ChoiceOrder(Common):
    appPackage = get_appPackage()
    item1 = (By.XPATH,"//android.widget.FrameLayout[1]/android.widget.LinearLayout[1]/android.widget.FrameLayout[1]/android.widget.LinearLayout[1]/androidx.viewpager.widget.ViewPager[1]/android.widget.LinearLayout[1]/android.widget.ListView[1]/android.widget.RelativeLayout[6]/android.widget.TextView[1]")
    rengu = (By.ID,appPackage+":id/tv_put")
    rengou = (By.ID,appPackage+":id/tv_subscribe")
    # 点击合约
    def c_orderpage(self):
        text = self.get_element_text(self.item1, "获取第六个合约名称")
        self.get_clickable_element(self.item1,"选择第六个合约")
        return text
    # 选择认沽
    def c_rengu(self):
        self.get_clickable_element(self.rengu,"点击认沽")
    # 根据合约名称，下较高行权价的合约的单 +/-
    def c_contract(self,old_name,type="购",add="+"):
        if type == "购" and add == "+":
            price = old_name[(old_name.index("月")+1):]
            contract = old_name[:(old_name.index("月")+1)]
            hiprice = int(int(price) + 100)
            new_name = contract + str(hiprice)
            xpath = "//android.widget.TextView[@text='%s']" % new_name.replace("沽","购")
            print(xpath)
            item2 = (By.XPATH, xpath)
            self.get_clickable_element(self.rengou, "点击认购")
            self.get_clickable_element(item2, "选择合约")
            return new_name.replace("沽","购")
        elif type == "购" and add == "-":
            price = old_name[(old_name.index("月") + 1):]
            contract = old_name[:old_name.index("月") + 1]
            lowprice = int(int(price) - 100)
            new_name = contract + str(lowprice)
            xpath = "//android.widget.TextView[@text='%s']" % new_name.replace("沽", "购")
            print(xpath)
            item2 = (By.XPATH, xpath)
            self.get_clickable_element(self.rengou, "点击认购")
            self.get_clickable_element(item2, "选择合约")
            return new_name.replace("沽", "购")
        elif type == "沽" and add == "+":
            price = old_name[(old_name.index("月") + 1):]
            contract = old_name[:old_name.index("月") + 1]
            lowprice = int(int(price) + 100)
            new_name = contract + str(lowprice)
            xpath = "//android.widget.TextView[@text='%s']" % new_name.replace("购", "沽")
            print(xpath)
            item2 = (By.XPATH, xpath)
            self.get_clickable_element(self.rengu, "点击认沽")
            self.get_clickable_element(item2, "选择合约")
            return new_name.replace("购", "沽")
        elif type == "沽" and add == "-":
            price = old_name[(old_name.index("月") + 1):]
            contract = old_name[:old_name.index("月") + 1]
            lowprice = int(int(price) - 100)
            new_name = contract + str(lowprice)
            xpath = "//android.widget.TextView[@text='%s']" % new_name.replace("购", "沽")
            print(xpath)
            item2 = (By.XPATH, xpath)
            self.get_clickable_element(self.rengu, "点击认沽")
            self.get_clickable_element(item2, "选择合约")
            return new_name.replace("购", "沽")
        else:
            print("输入错误")
