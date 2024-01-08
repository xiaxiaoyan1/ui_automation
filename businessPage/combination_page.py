__author__ = 'Administrator'
from common.collector_log import my_log
from selenium.webdriver.common.by import By
from selenium.common.exceptions import NoSuchElementException
from common.common_fun import Common
from common.read_config import get_appPackage
class Combination(Common):
    appPackage = get_appPackage()
    comb_apply = (By.ID, appPackage+':id/rbtn_1')
    comb_hold = (By.ID, appPackage+':id/rbtn_2')
    comb_relieve = (By.ID, appPackage+':id/rbtn_3')


