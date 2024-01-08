from common.common_fun import Common
from businessPage.exercise_page import Exercise
from businessPage.trade_first_page import TradeFirst
from selenium.webdriver.common.by import By
import pytest
#行权用例
@pytest.mark.usefixtures('login_fixture')
@pytest.mark.usefixtures('driver_fixture')
class TestClok():
    @pytest.fixture(scope='function', autouse=False)
    def setup_fixture(self, driver_fixture):
        driver = driver_fixture
        tradehome = TradeFirst(driver)
        exe = Exercise(driver)
        tradehome.to_trade_page()
        tradehome.to_exercise()
        return exe
    # 行权
    @pytest.mark.usefixtures('back_fixture')
    def test_exe(self,setup_fixture):
        exe = setup_fixture
        res = exe.exercise()
        assert res == True
    # 被指派
    @pytest.mark.usefixtures('back_fixture')
    def test_ass(self,setup_fixture):
        exe = setup_fixture
        res = exe.ass()
        assert res == True
    # 协议行权
    @pytest.mark.usefixtures('back_fixture')
    def test_agree_exercise(self,setup_fixture):
        exe = setup_fixture
        res = exe.agree_exercise(1)
        assert res == True
    # 协议行权修改
    @pytest.mark.usefixtures('back_fixture')
    def test_change_exercise(self,setup_fixture):
        exe = setup_fixture
        res = exe.change_exercise(1)
        assert res == True
    # 行权委托-撤单
    @pytest.mark.usefixtures('back_fixture')
    def test_entrust_exercise(self,setup_fixture):
        exe = setup_fixture
        res = exe.entrust_exercise()
        assert res == True

































# __author__ = 'Administrator'
# from businessPage.trade_first_page import TradeFirst
# from businessPage.exercise_page import Exercise
# import pytest
# from selenium.webdriver.common.by import By
# from common.common_fun import Common
# import time
# @pytest.mark.usefixture("driver_fixture")
# class Test_exercise():
#     def test_exercise(self,driver_fixture):
#         self.driver=driver_fixture
#         exe=TradeFirst(self.driver)
#         exe.toexe()
#         cise=Exercise(self.driver)
#         cise.exercise(1)
#         conf=Common(self.driver)
#         conf.confirm_frame()
#         con=conf.get_toast_text('exercise')
#         assert con=='委托成功'
#
#     def test_agree(self,driver_fixture):
#         self.driver=driver_fixture
#         exe=TradeFirst(self.driver)
#         exe.toexe()
#         cise=Exercise(self.driver)
#         cise.agree_exercise(1)
#         conf=Common(self.driver)
#         conf.confirm_frame()
#         con=conf.get_toast_text('agree exercise')
#         assert con=='委托成功'
#
#     def test_entrust(self,driver_fixture):
#         self.driver=driver_fixture
#         exe=TradeFirst(self.driver)
#         exe.toexe()
#         cise=Exercise(self.driver)
#         ent=cise.entrust_exercise()
#         assert ent==True
#
#
#
#
#
#
#
#
