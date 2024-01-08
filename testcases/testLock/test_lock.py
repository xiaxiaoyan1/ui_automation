from common.common_fun import Common
from businessPage.clok_page import ClokUnclok
from businessPage.trade_first_page import TradeFirst
from selenium.webdriver.common.by import By
import pytest
#锁定解锁用例
@pytest.mark.usefixtures('login_fixture')
@pytest.mark.usefixtures('driver_fixture')
class TestClok():
    @pytest.fixture(scope='function', autouse=False)
    def setup_fixture(self, driver_fixture):
        driver = driver_fixture
        tradehome = TradeFirst(driver)
        clokunclok = ClokUnclok(driver)
        tradehome.to_trade_page()
        tradehome.to_clok()
        return clokunclok
    # 锁定
    @pytest.mark.usefixtures('back_fixture')
    def test_clok(self,setup_fixture):
        clokunclok = setup_fixture
        res = clokunclok.clok_confirm()
        assert res == True
    # 解锁
    @pytest.mark.usefixtures('back_fixture')
    def test_unclok(self,setup_fixture):
        clokunclok = setup_fixture
        res = clokunclok.unclok_confirm()
        assert res == True









































# __author__ = 'Administrator'
# from businessPage.trade_first_page import TradeFirst
# import pytest
# from selenium.webdriver.common.by import By
# import logging
# from common.common_fun import Common
# from businessPage.clok_page import ClokUnclok
# import time
# @pytest.mark.usefixtures("driver_fixture")
# @pytest.mark.usefixtures("backtest")
# class Test_Clok():
#     add=(By.ID,'com.fzzq.qqb.fz:id/btn_sub_add')
#     amount=(By.ID,'com.fzzq.qqb.fz:id/et_sdsl')
#     btnclok=(By.ID,'com.fzzq.qqb.fz:id/btn_confirm')
#     btncomf=(By.ID,'com.fzzq.qqb.fz:id/btn_confirm')
#     btncancel=(By.ID,'com.fzzq.qqb.fz:id/btn_cancel')
#
#     # def test_clok01(self,driver_fixture):
#     #     self.driver=driver_fixture
#     #     toclok=trade_first(self.driver)
#     #     toclok.to_clok()
#     #     self.driver.find_element(*self.add).click()
#     #     amountscreen=Common(self.driver)
#     #     amountscreen.getScreenShot("clok amount ture")
#     #     clokteail=self.driver.find_element(*self.amount)
#     #     assert clokteail.get_attribute('text') == '10000'
#
#     def test_clok(self,driver_fixture):
#         self.driver=driver_fixture
#         toclok=TradeFirst(self.driver)
#         toclok.to_clok()
#         clokbusy=ClokUnclok(self.driver)
#         clokbusy.addclok()
#         clokbusy.clok()
#         confirm=Common(self.driver)
#         res=confirm.confirm_frame()
#         confirm.get_toast_text('unclok')
#         assert res=='委托成功'
#
#     def test_unclok(self,driver_fixture):
#         self.driver=driver_fixture
#         toclok=TradeFirst(self.driver)
#         toclok.to_clok()
#         clokbusy=ClokUnclok(self.driver)
#         clokbusy.changeclok()
#         clokbusy.addclok()
#         clokbusy.clok()
#         confirm=Common(self.driver)
#         res=confirm.confirm_frame()
#         confirm.get_toast_text('unclok')
#         assert res=='委托成功'
#
#         # self.driver.find_element(*self.add).click()
#         # self.driver.find_element(*self.btnconfirm).click()
#         # time.sleep(3)
#         # self.driver.find_element(*self.btnconfirm).click()
#         # clokscreen=Common(self.driver)
#         # clokscreen.getScreenShot("clok confirm")
#
#
#     # def test_clok03(self,driver_fixture):
#     #     self.driver=driver_fixture
#     #     toclok=trade_first(self.driver)
#     #     toclok.to_clok()
#     #     self.driver.find_element(*self.add).click()
#     #     self.driver.find_element(*self.btncancel).click()
#     #     cancel=Common(self.driver)
#     #     cancel.getScreenShot("cancel clok")
#     #     clokteail=self.driver.find_element(*self.amount)
#     #     assert clokteail.get_attribute('text') == '10000'
#
#
#
#
#
#
#
#
#
#
#
#
#
