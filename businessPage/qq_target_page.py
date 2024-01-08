__author__ = 'Administrator'
#期权标的页面
from common.desired_caps import app_desired
from common.common_fun import Common
import time
from common.read_config import get_appPackage
class qq_target(Common):
    appPackage = get_appPackage()
    def to_Toffer(self):
        time.sleep(3)
