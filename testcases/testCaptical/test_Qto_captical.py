__author__ = 'Administrator'

from businessPage.qq_target_page import qq_target
from common.desired_caps import app_desired
from businessPage.login_page import Login
from businessPage.trade_first_page import TradeFirst
from common.common_fun import Common
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import pytest,time
#交易主页-资金信息
@pytest.mark.usefixtures('login_fixture')
@pytest.mark.usefixtures('driver_fixture')
class Test_trade():
    @pytest.mark.usefixtures('back_fixture')
    def test_captical(self,driver_fixture):
        self.driver=driver_fixture
        cap=TradeFirst(self.driver)
        cap.to_trade_page()
        result=cap.to_capital()
        assert result==True
    #
    # def test_position(self,driver_fixture):
    #     self.driver=driver_fixture
    #     positn=trade_first(self.driver)
    #     res=positn.to_position()
    #     time.sleep(5)
    #     assert res==True
    #
    # def test_cancelorder(self,driver_fixture):
    #     self.driver=driver_fixture
    #     cancel=trade_first(self.driver)
    #     cel=cancel.to_cancelOrder()
    #     time.sleep(3)
    #     assert cel==True
    #
    # def test_clok(self,driver_fixture):
    #     self.driver=driver_fixture
    #     toclok=trade_first(self.driver)
    #     clok=toclok.to_clok()
    #     time.sleep(3)
    #     assert clok==True








