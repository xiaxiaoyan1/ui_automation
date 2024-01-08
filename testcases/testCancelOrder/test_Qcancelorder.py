__author__ = 'Administrator'
from common.common_fun import Common
from businessPage.cancel_order_page import CancelOrder
from businessPage.trade_first_page import TradeFirst
from businessPage.choice_oder_page import ChoiceOrder
from businessPage.order_page import Order
import pytest,time
from selenium.webdriver.common.by import By
#撤单测试用例
@pytest.mark.usefixtures('login_fixture')
@pytest.mark.usefixtures('driver_fixture')
class TestCancelOrder():
    @pytest.fixture(scope='function', autouse=False)
    def setup_fixture(self, driver_fixture):
        driver = driver_fixture
        tradehome = TradeFirst(driver)
        choiceorder = ChoiceOrder(driver)
        cancleorder = CancelOrder(driver)
        order = Order(driver)
        return cancleorder,tradehome,choiceorder,order
    # 批量撤单
    @pytest.mark.usefixtures('back_fixture')
    def test_confirm_cancel(self,setup_fixture):
        cancleorder,tradehome,choiceorder,order= setup_fixture
        # 构造1个撤单数据
        tradehome.to_trade_page()
        tradehome.to_order()
        choiceorder.c_orderpage()
        order.c_price_ztj()
        order.c_hand(1)
        order.c_ordersell()
        order.order_page_back()
        # 进入撤单页
        tradehome.to_cancelOrder()
        res = cancleorder.c_confirm_cancel()
        assert res == True
    # 二级菜单撤单
    @pytest.mark.usefixtures('back_fixture')
    def test_cancel(self,setup_fixture):
        cancleorder,tradehome,choiceorder,order= setup_fixture
        # 构造1个撤单数据
        tradehome.to_trade_page()
        tradehome.to_order()
        choiceorder.c_orderpage()
        order.c_price_ztj()
        order.c_hand(1)
        order.c_ordersell()
        order.order_page_back()
        # 进入撤单页
        tradehome.to_cancelOrder()
        res = cancleorder.c_cancel()
        assert res == True
    # 全部撤单
    @pytest.mark.usefixtures('back_fixture')
    def test_all_cancel(self, setup_fixture):
        cancleorder,tradehome,choiceorder,order= setup_fixture
        # 构造1个撤单数据
        tradehome.to_trade_page()
        tradehome.to_order()
        choiceorder.c_orderpage()
        order.c_price_ztj()
        order.c_hand(1)
        order.c_ordersell()
        order.order_page_back()
        # 进入撤单页
        tradehome.to_cancelOrder()
        res = cancleorder.c_all_cancel()
        assert res == True
    # 二级菜单撤单后买入
    @pytest.mark.usefixtures('back_fixture')
    def test_cancel_buy(self,setup_fixture):
        cancleorder,tradehome,choiceorder,order= setup_fixture
        # 构造1个买入撤单数据
        tradehome.to_trade_page()
        tradehome.to_order()
        choiceorder.c_orderpage()
        order.c_price_dtj()
        order.c_hand(1)
        order.c_orderbuy()
        order.order_page_back()
        # 进入撤单页
        tradehome.to_cancelOrder()
        # 撤单后买入/卖出/平仓
        res = cancleorder.c_cancel_sell()
        assert res == True
    # 二级菜单撤单后卖出
    @pytest.mark.usefixtures('back_fixture')
    def test_cancel_sell(self,setup_fixture):
        cancleorder,tradehome,choiceorder,order= setup_fixture
        # 构造1个卖出撤单数据
        tradehome.to_trade_page()
        tradehome.to_order()
        choiceorder.c_orderpage()
        order.c_price_ztj()
        order.c_hand(1)
        order.c_ordersell()
        order.order_page_back()
        # 进入撤单页
        tradehome.to_cancelOrder()
        # 撤单后买入/卖出/平仓
        res = cancleorder.c_cancel_sell()
        assert res == True
    # 二级菜单撤单后平仓
    @pytest.mark.usefixtures('back_fixture')
    def test_cancel_flat(self,setup_fixture):
        cancleorder,tradehome,choiceorder,order= setup_fixture
        # 构造1个平仓撤单数据
        tradehome.to_trade_page()
        tradehome.to_order()
        choiceorder.c_orderpage()
        # 点击持仓item，返回权力仓或义务仓
        type = order.get_hold_type()
        count = order.get_hold_count()
        if type == "权利":
            if count == 0:
                order.c_hand(1)
                order.c_orderbuy()
                time.sleep(3)
                # 切换重新请求持仓
                order.c_cancel()
                order.c_hold()
            order.c_price_ztj()
        elif type == "义务":
            if count == 0:
                order.c_hand(1)
                order.c_ordersell()
                time.sleep(3)
                # 切换重新请求持仓
                order.c_cancel()
                order.c_hold()
            order.c_price_dtj()
        else:
            order.c_price_ztj()
        order.c_hand(1)
        order.c_orderflat()
        order.order_page_back()
        # 进入撤单页
        tradehome.to_cancelOrder()
        # 撤单后买入/卖出/平仓
        res = cancleorder.c_cancel_sell()
        assert res == True
    # 撤单后交易再次下单同一合约
    @pytest.mark.usefixtures('back_fixture')
    def test_cancel_order(self, setup_fixture):
        cancleorder, tradehome, choiceorder, order = setup_fixture
        # 构造1个买入撤单数据
        tradehome.to_trade_page()
        tradehome.to_order()
        choiceorder.c_orderpage()
        order.c_price_dtj()
        order.c_hand(1)
        order.c_orderbuy()
        order.order_page_back()
        # 进入撤单页
        tradehome.to_cancelOrder()
        # 撤单后买入/卖出/平仓
        res = cancleorder.c_cancel_sell()
        assert res == True
        # 下单
        res = order.c_orderbuy()
        assert res == True
    # 撤单后交易再次下单不同合约
    @pytest.mark.usefixtures('back_fixture')
    def test_cancel_order_other(self, setup_fixture):
        cancleorder, tradehome, choiceorder, order = setup_fixture
        # 构造1个买入撤单数据
        tradehome.to_trade_page()
        tradehome.to_order()
        choiceorder.c_orderpage()
        order.c_price_dtj()
        order.c_hand(1)
        order.c_orderbuy()
        order.order_page_back()
        # 进入撤单页
        tradehome.to_cancelOrder()
        # 撤单后买入/卖出/平仓
        res = cancleorder.c_cancel_sell()
        assert res == True
        # 切换合约
        order.c_iv_right()
        # 下单
        res = order.c_orderbuy()
        assert res == True

