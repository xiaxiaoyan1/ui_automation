from businessPage.choice_oder_page import ChoiceOrder
from businessPage.order_page import Order
from businessPage.combination_report_page import CombinationReport
from businessPage.trade_first_page import TradeFirst

from common.common_fun import Common
import pytest
#组合申报测试用例
@pytest.mark.usefixtures('login_fixture')
@pytest.mark.usefixtures('driver_fixture')
class TestEntrustSetup():
    @pytest.fixture(scope='function', autouse=False)
    def setup_fixture(self, driver_fixture):
        driver = driver_fixture
        tradehome = TradeFirst(driver)
        choiceorder = ChoiceOrder(driver)
        order = Order(driver)
        combinationreport = CombinationReport(driver)
        tradehome.to_trade_page()
        return tradehome, choiceorder, order, combinationreport
    @pytest.mark.usefixtures('back_fixture')
    def test_apply(self,setup_fixture):
        tradehome, choiceorder, order, combinationreport = setup_fixture
        # 认购牛市价差组合：一个较低行权价的认购期权权利方头寸，一个相同标的、相同到期曰、行权价较高的认购期权义务方头寸。
        # 创造一个低行权价的认购权力期权（相同标的、到期日）
        tradehome.to_order()
        contract1_name = choiceorder.c_orderpage()  # 获得下单合约名称
        order.c_hand(1)
        order.c_orderbuy()
        order.back()
        # 创造一个高行权价的认购义务期权（相同标的、到期日）
        tradehome.to_order()
        contract2_name = choiceorder.c_contract(contract1_name, "购", "+")  # 获得下单合约名称
        order.c_hand(1)
        order.c_ordersell()
        order.back()
        # 开始组合申报
        tradehome.to_comb_report()
        res = combinationreport.apply()
        assert res == True

    # @pytest.mark.usefixtures('back_fixture')
    # def test_holdRelieve(self):
    #     tradehome, choiceorder, order, combinationreport = setup_fixture
    #     tradehome.to_comb_report()
    #     combinationreport.holdRelieve()

    @pytest.mark.usefixtures('back_fixture')
    def test_relieveComb(self,setup_fixture):
        tradehome, choiceorder, order, combinationreport = setup_fixture
        tradehome.to_comb_report()
        res = combinationreport.relieveComb()
        assert res == True