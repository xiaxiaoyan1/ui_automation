__author__ = 'Administrator'
from common.collector_log import my_log
from selenium.webdriver.common.by import By
from selenium.common.exceptions import NoSuchElementException
from common.common_fun import Common
class Style(Common):
    tradition_style = (By.XPATH, "//android.widget.LinearLayout/android.widget.RelativeLayout[2]")
    three_style = (By.XPATH, "//android.widget.LinearLayout/android.widget.RelativeLayout[3]")
    four_style = (By.XPATH, "//android.widget.LinearLayout/android.widget.RelativeLayout[4]")  # 四键下单
    def tradition(self):
        self.get_clickable_element(self.tradition_style,"传统下单")
    def three(self):
        self.get_clickable_element(self.three_style,"三键下单")