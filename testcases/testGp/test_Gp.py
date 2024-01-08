from common.common_fun import Common
from businessPage.gp_page import Gp
from businessPage.trade_first_page import TradeFirst
from businessPage.order_page import Order

from selenium.webdriver.common.by import By
import pytest
#首页用例
@pytest.mark.usefixtures('gp_login_fixture')
@pytest.mark.usefixtures('login_fixture')
@pytest.mark.usefixtures('driver_fixture')
class TestGp():
    @pytest.fixture(scope='function', autouse=False)
    def setup_fixture(self, driver_fixture):
        driver = driver_fixture
        tradehome = TradeFirst(driver)
        gp = Gp(driver)
        order = Order(driver)
        tradehome.to_trade_page()
        gp.tipGp()
        return gp,order
    # 查看资金详情
    @pytest.mark.usefixtures('back_fixture')
    def test_zjxq(self,setup_fixture):
        gp,order = setup_fixture
        res = gp.tipzzc()
        assert res == True
    # 限价买入
    @pytest.mark.usefixtures('back_fixture')
    def test_xjbuy(self, setup_fixture):
        gp,order = setup_fixture
        # 进入限价页面
        gp.tipxj()
        # 点击买入
        gp.tipbuy()
        # 输入合约代码并带入价格,默认“000001”
        gp.input_contract()
        # 输入数量，默认“100”
        gp.input_num()
        # 买入
        gp.c_buy()
    # 限价-买入-带入持仓股
    @pytest.mark.usefixtures('back_fixture')
    def test_hold(self):
        gp, order = setup_fixture
        # 进入限价页面
        gp.tipxj()
        # 点击买入
        gp.tipbuy()
        # 点击持仓带入数据
        res = gp.c_hold()
        assert res == True
    # 限价-买入-带入涨停价、跌停价、五档买卖价
    @pytest.mark.usefixtures('back_fixture')
    def test_zt(self):
        gp, order = setup_fixture
        # 进入限价页面
        gp.tipxj()
        # 点击买入
        gp.tipbuy()
        # 点击涨停带入数据
        res = gp.send_ztj()
        pytest.assume(res == True)
        # 点击跌停带入数据
        res = gp.send_dtj()
        pytest.assume(res == True)
        # 点击五档买卖带入数据
        res = gp.send_fiveprice()
        pytest.assume(res == True)

    # 限价-买入-全部撤单
    @pytest.mark.usefixtures('back_fixture')
    def test_cancle(self):
        gp, order = setup_fixture
        # 进入限价页面
        gp.tipxj()
        # 点击买入
        gp.tipbuy()
        # 构造撤单数据
        gp.input_contract()
        gp.del_price()
        gp.del_price()
        gp.input_num()
        gp.c_buy()
        # 全部撤单
        order.c_cancel()
        res = order.c_all_cancel()
        assert res == True
    # 限价-买入-批量撤单
    @pytest.mark.usefixtures('back_fixture')
    def test_cancle(self):
        gp, order = setup_fixture
        # 进入限价页面
        gp.tipxj()
        # 点击买入
        gp.tipbuy()
        # 构造撤单数据
        gp.input_contract()
        gp.del_price()
        gp.del_price()
        gp.input_num()
        gp.c_buy()
        # 批量撤单
        order.c_cancel()
        res = order.c_confirm_cancel()
        assert res == True
    # 限价-买入-委托
    @pytest.mark.usefixtures('back_fixture')
    def test_cancle(self):
        gp, order = setup_fixture
        # 进入限价页面
        gp.tipxj()
        # 点击买入
        gp.tipbuy()
        # 委托
        order.c_entrust()

    # 限价-买入-成交
    @pytest.mark.usefixtures('back_fixture')
    def test_cancle(self):
        gp, order = setup_fixture
        # 进入限价页面
        gp.tipxj()
        # 点击买入
        gp.tipbuy()
        # 成交
        order.c_deal()

