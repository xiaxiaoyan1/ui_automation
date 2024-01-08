from businessPage.choice_oder_page import ChoiceOrder
from businessPage.order_page import Order
from businessPage.merger_exercise_page import Exercise
from businessPage.trade_first_page import TradeFirst

from common.common_fun import Common
from selenium.webdriver.common.by import By
import pytest
#合并行权用例
@pytest.mark.usefixtures('login_fixture')
@pytest.mark.usefixtures('driver_fixture')
class TestClok():
    def test_init(self,driver_fixture):
        global tradehome, choiceorder, order ,mergerexe
        self.driver = driver_fixture
        tradehome = TradeFirst(self.driver)
        choiceorder = ChoiceOrder(self.driver)
        order = Order(self.driver)
        mergerexe = Exercise(self.driver)
    # 合并行权
    @pytest.mark.usefixtures('back_fixture')
    def test_merger_exercise(self):
        global tradehome, choiceorder, order, mergerexe
        tradehome.to_trade_page()
        # 创造行权价低的认购期权
        tradehome.to_order()
        contract1_name = choiceorder.c_orderpage()  # 获得下单合约名称
        order.c_hand()
        order.c_orderbuy()
        mergerexe.c_back()
        # 创造行权价高的认沽期权
        tradehome.to_order()
        contract2_name = choiceorder.c_contract(contract1_name,"沽","+")  # 获得下单合约名称
        order.c_hand()
        order.c_orderbuy()
        mergerexe.c_back()
        # 合并行权
        tradehome.to_merger_exe()
        res = mergerexe.exercise(contract1_name)
        assert res == True




