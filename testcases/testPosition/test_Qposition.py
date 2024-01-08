__author__ = 'Administrator'
from businessPage.trade_first_page import TradeFirst
from businessPage.order_page import Order
from businessPage.position_page import Position

import pytest
#持仓用例
@pytest.mark.usefixtures('login_fixture')
@pytest.mark.usefixtures('driver_fixture')
class TestPosition():
    @pytest.fixture(scope='function', autouse=False)
    def setup_fixture(self, driver_fixture):
        driver = driver_fixture
        tradehome = TradeFirst(driver)
        position = Position(driver)
        order = Order(driver)
        tradehome.to_trade_page()
        tradehome.to_position()
        return position,order,tradehome
    #持仓-详情
    @pytest.mark.usefixtures('back_fixture')
    def test_tetail(self,setup_fixture):
        position,order,tradehome = setup_fixture
        position.tipline()
        detail=position.tipdetail()
        assert detail==True
    #-持仓-行情
    @pytest.mark.usefixtures('back_fixture')
    def test_hq(self,setup_fixture):
        position,order,tradehome = setup_fixture
        position.tipline()
        hq=position.tiphq()
        assert hq==True
    #持仓-下单
    @pytest.mark.usefixtures('back_fixture')
    def test_order(self,setup_fixture):
        position,order,tradehome = setup_fixture
        position.tipline()
        hq=position.tiporder()
        assert hq==True
    #持仓-平仓
    @pytest.mark.usefixtures('back_fixture')
    def test_pc(self,setup_fixture):
        position,order,tradehome = setup_fixture
        position.tipline()
        hq=position.tippc()
        assert hq==True
    # 持仓可用排序
    @pytest.mark.usefixtures('back_fixture')
    def test_hold_num(self, setup_fixture):
        position,order,tradehome = setup_fixture
        # 降序
        order.c_hold_num()
        res = order.desc(2)
        pytest.assume(res == True)
        # 升序
        order.c_hold_num()
        res = order.asc(2)
        pytest.assume(res == True)
    # 现价排序
    @pytest.mark.usefixtures('back_fixture')
    def test_now_price(self, setup_fixture):
        position,order,tradehome = setup_fixture
        # 降序
        order.c_hold_now_price()
        res = order.desc(3)
        pytest.assume(res == True)
        # 升序
        order.c_hold_now_price()
        res = order.asc(3)
        pytest.assume(res == True)
    # 盈亏排序
    @pytest.mark.usefixtures('back_fixture')
    def test_rise(self, setup_fixture):
        position,order,tradehome = setup_fixture
        # 降序
        order.c_hold_yk()
        res = order.desc(4)
        pytest.assume(res == True)
        # 升序
        order.c_hold_yk()
        res = order.asc(4)
        pytest.assume(res == True)
    # 排序后跳转行情返回保持排序
    @pytest.mark.usefixtures('back_fixture')
    def test_sort_back(self, setup_fixture):
        position,order,tradehome = setup_fixture
        # 持仓降序
        order.c_hold_num()
        res = order.desc(2)
        pytest.assume(res == True)
        # 跳转行情页
        position.tipline()
        hq = position.tiphq()
        pytest.assume(hq == True)
        # 返回查看排序
        order.hq_back()
        res1 = order.desc(2)
        pytest.assume(res1 == True)
    # 排序后再进入，清空排序规则
    @pytest.mark.usefixtures('back_fixture')
    def test_sort_return(self, setup_fixture):
        position,order,tradehome = setup_fixture
        # 持仓降序
        order.c_hold_num()
        res = order.desc(2)
        pytest.assume(res == True)
        # 返回
        order.back()
        # 再次进入持仓查看是否排序
        tradehome.to_position()
        res1 = position.sort_icon()
        pytest.assume(res1 == False)
    # 排序后跳转下单返回保持排序，并保持二级菜单展开
    @pytest.mark.usefixtures('back_fixture')
    def test_sort_order(self, setup_fixture):
        position, order, tradehome = setup_fixture
        # 持仓降序
        order.c_hold_num()
        res = order.desc(2)
        pytest.assume(res == True)
        # 跳转下单页
        position.tipline()
        hq = position.tiporder()
        pytest.assume(hq == True)
        # 买入下单
        order.c_hand()
        res1 = order.c_orderbuy()
        pytest.assume(hq == True)
        # 返回查看排序
        order.back()
        res2 = order.desc(2)
        pytest.assume(res2 == True)
        # 判断二级菜单是否展开
        res3 = position.secondary_menu()
        pytest.assume(res2 == True)