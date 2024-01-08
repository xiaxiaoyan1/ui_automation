from common.common_fun import Common
from businessPage.order_page import Order
from businessPage.trade_first_page import TradeFirst
from businessPage.choice_oder_page import ChoiceOrder
from businessPage.optional_page import Optional
from selenium.webdriver.common.by import By
import pytest
#下单用例
@pytest.mark.usefixtures('login_fixture')
@pytest.mark.usefixtures('driver_fixture')
class TestOrder():
    @pytest.fixture(scope='function', autouse=False)
    def setup_fixture(self, driver_fixture):
        driver = driver_fixture
        tradehome = TradeFirst(driver)
        choiceorder = ChoiceOrder(driver)
        order = Order(driver)
        optional = Optional(driver)
        tradehome.to_trade_page()
        tradehome.to_order()
        choiceorder.c_orderpage()
        return order,tradehome,optional
    # # 加自选
    # @pytest.mark.usefixtures('back_fixture')
    # def test_optional(self,setup_fixture):
    #     order,tradehome,optional = setup_fixture
    #     name = order.c_add_optional()
    #     order.back()
    #     tradehome.to_optional_page()
    #     res = optional.have_zx(name)
    #     assert res == True
    # # 对手价买开
    # @pytest.mark.usefixtures('back_fixture')
    # def test_buy_dsj(self,setup_fixture):
    #     order,tradehome,optional = setup_fixture
    #     order.c_price_dsj()
    #     order.c_hand(1)
    #     res = order.c_orderbuy()
    #     assert res == True
    # # 涨停价卖开
    # @pytest.mark.usefixtures('back_fixture')
    # def test_sell_ztj(self,setup_fixture):
    #     order,tradehome,optional = setup_fixture
    #     order.c_price_ztj()
    #     order.c_hand(1)
    #     res = order.c_ordersell()
    #     assert res == True
    # # 平仓
    # @pytest.mark.usefixtures('back_fixture')
    # def test_flat(self,setup_fixture):
    #     order,tradehome,optional = setup_fixture
    #     order.c_price_dsj()
    #     order.c_hand(1)
    #     res = order.c_orderflat()
    #     assert res == True
    # # 撤单
    # @pytest.mark.usefixtures('back_fixture')
    # def test_cancel(self,setup_fixture):
    #     order,tradehome,optional = setup_fixture
    #     # 构造两个撤单数据
    #     order.c_price_ztj()
    #     order.c_hand(1)
    #     order.c_ordersell()
    #     order.c_price_dtj()
    #     order.c_hand(1)
    #     order.c_orderbuy()
    #     order.c_cancel()
    #     res = order.c_confirm_cancel()
    #     pytest.assume(res == True)
    #     res = order.c_all_cancel()
    #     assert res == True
    # # table切换
    # @pytest.mark.usefixtures('back_fixture')
    # def test_table(self,setup_fixture):
    #     order,tradehome,optional = setup_fixture
    #     # 委托
    #     res1 = order.c_entrust()
    #     pytest.assume(res1 == True)
    #     # 成交
    #     res2 = order.c_deal()
    #     pytest.assume(res2 == True)
    #     # 走势
    #     res3 = order.c_trend()
    #     pytest.assume(res3 == True)
    #     # 自选
    #     res4 = order.c_optional()
    #     pytest.assume(res4 == True)
    # # 带入最新价下单
    # @pytest.mark.usefixtures('back_fixture')
    # def test_now_price(self,setup_fixture):
    #     order, tradehome, optional = setup_fixture
    #     # 点击最新价带入数据
    #     res = order.c_now_price()
    #     pytest.assume(res == True)
    #     # 输入数量
    #     order.c_hand()
    #     # 买开
    #     res2 = order.c_orderbuy()
    #     assert res2 == True
    # # 带入涨停价下单
    # @pytest.mark.usefixtures('back_fixture')
    # def test_ztj_price(self, setup_fixture):
    #     order, tradehome, optional = setup_fixture
    #     # 点击涨停带入数据
    #     res1 = order.c_ztj_price()
    #     pytest.assume(res1 == True)
    #     # 输入数量
    #     order.c_hand()
    #     # 买开
    #     res2 = order.c_orderbuy()
    #     assert res2 == True
    # # 带入跌停价下单
    # @pytest.mark.usefixtures('back_fixture')
    # def test_dtj_price(self, setup_fixture):
    #     order, tradehome, optional = setup_fixture
    #     # 点击跌停带入数据
    #     res1 = order.c_dtj_price()
    #     pytest.assume(res1 == True)
    #     # 输入数量
    #     order.c_hand()
    #     # 买开
    #     res2 = order.c_orderbuy()
    #     assert res2 == True
    # # 带入卖一价下单
    # @pytest.mark.usefixtures('back_fixture')
    # def test_firstsell_price(self, setup_fixture):
    #     order, tradehome, optional = setup_fixture
    #     # 点击卖一价带入数据
    #     res1 = order.c_firstsell_price()
    #     pytest.assume(res1 == True)
    #     # 输入数量
    #     order.c_hand()
    #     # 买开
    #     res2 = order.c_orderbuy()
    #     assert res2 == True
    # # 点击持仓平仓
    # @pytest.mark.usefixtures('back_fixture')
    # def test_hold_flat(self, setup_fixture):
    #     order, tradehome, optional = setup_fixture
    #     # 点击持仓
    #     order.c_hold()
    #     res1 = order.c_hold_item()
    #     pytest.assume(res1 == True)
    #     # 输入数量
    #     order.c_hand()
    #     # 平仓
    #     res2 = order.c_orderflat()
    #     assert res2 == True
    # # FOK下单
    # @pytest.mark.usefixtures('back_fixture')
    # def test_FOKorder(self, setup_fixture):
    #     order, tradehome, optional = setup_fixture
    #     # 勾选FOK
    #     order.c_price_ztj()
    #     res1 = order.c_FOK()
    #     pytest.assume(res1 == True)
    #     # 输入数量
    #     order.c_hand()
    #     # 下单
    #     res2 = order.c_orderbuy()
    #     assert res2 == True
    # # 三键下单，备兑开仓
    # @pytest.mark.usefixtures('back_fixture')
    # def test_covered_sell(self, setup_fixture):
    #     order, tradehome, optional = setup_fixture
    #     # 勾选备兑
    #     res1 = order.c_covered()
    #     pytest.assume(res1 == True)
    #     # 输入数量
    #     order.c_hand()
    #     # 备兑开仓
    #     res2 = order.c_covered_sell()
    #     pytest.assume(res2 == True)
    # # 三键下单，勾选备兑，跳转锁定解锁
    # @pytest.mark.usefixtures('back_fixture')
    # def test_clock(self, setup_fixture):
    #     order, tradehome, optional = setup_fixture
    #     # 勾选备兑
    #     res1 = order.c_covered()
    #     pytest.assume(res1 == True)
    #     # 点击锁定解锁
    #     res2 = order.c_clock()
    #     assert res2 == True
    # # 持仓/自选-排序构造数据
    # @pytest.mark.usefixtures('back_fixture')
    # def test_add_data(self, setup_fixture):
    #     order, tradehome, optional = setup_fixture
    #     for i in range(5):
    #         # 切换合约
    #         order.c_iv_right()
    #         # 加自选
    #         order.c_add_optional()
    #         # 点击最新价带入数据
    #         res = order.c_now_price()
    #         # 输入数量
    #         order.c_hand()
    #         # 买开
    #         res2 = order.c_orderbuy()
    # # 持仓可用排序
    # @pytest.mark.usefixtures('back_fixture')
    # def test_hold_num(self, setup_fixture):
    #     order, tradehome, optional = setup_fixture
    #     # 点击持仓
    #     order.c_hold()
    #     # 降序
    #     order.c_hold_num()
    #     res = order.desc(2)
    #     pytest.assume(res == True)
    #     # 升序
    #     order.c_hold_num()
    #     res = order.asc(2)
    #     pytest.assume(res == True)
    # # 现价排序
    # @pytest.mark.usefixtures('back_fixture')
    # def test_now_price(self, setup_fixture):
    #     order, tradehome, optional = setup_fixture
    #     # 点击持仓
    #     order.c_hold()
    #     # 降序
    #     order.c_hold_now_price()
    #     res = order.desc(3)
    #     pytest.assume(res == True)
    #     # 升序
    #     order.c_hold_now_price()
    #     res = order.asc(3)
    #     pytest.assume(res == True)
    # # 盈亏排序
    # @pytest.mark.usefixtures('back_fixture')
    # def test_rise(self, setup_fixture):
    #     order, tradehome, optional = setup_fixture
    #     # 点击持仓
    #     order.c_hold()
    #     # 降序
    #     order.c_hold_yk()
    #     res = order.desc(4)
    #     pytest.assume(res == True)
    #     # 升序
    #     order.c_hold_yk()
    #     res = order.asc(4)
    #     pytest.assume(res == True)
    # # 自选-排序
    # # 最新排序
    # @pytest.mark.usefixtures('back_fixture')
    # def test_new_price(self, setup_fixture):
    #     order, tradehome, optional = setup_fixture
    #     # 点击自选
    #     order.c_optional()
    #     # 降序
    #     order.c_new_price()
    #     res = order.desc1(2)
    #     pytest.assume(res == True)
    #     # 升序
    #     order.c_new_price()
    #     res = order.asc1(2)
    #     pytest.assume(res == True)
    # # 涨跌排序
    # @pytest.mark.usefixtures('back_fixture')
    # def test_rise(self, setup_fixture):
    #     order, tradehome, optional = setup_fixture
    #     # 点击自选
    #     order.c_optional()
    #     # 降序
    #     order.c_rise()
    #     res = order.desc1(3)
    #     pytest.assume(res == True)
    #     # 升序
    #     order.c_rise()
    #     res = order.asc1(3)
    #     pytest.assume(res == True)
    # # # 总量排序,需处理“万”字转换
    # # @pytest.mark.usefixtures('back_fixture')
    # # def test_count(self, setup_fixture):
    # #     order, tradehome, optional = setup_fixture
    # #     # 点击自选
    # #     order.c_optional()
    # #     # 降序
    # #     order.c_count()
    # #     res = order.desc1(5)
    # #     pytest.assume(res == True)
    # #     # 升序
    # #     order.c_count()
    # #     res = order.asc1(5)
    # #     pytest.assume(res == True)
    # # 点击自选切换合约下单
    # @pytest.mark.usefixtures('back_fixture')
    # def test_buy_addself(self, setup_fixture):
    #     order, tradehome, optional = setup_fixture
    #     # 点击自选
    #     res1 = order.c_optional()
    #     pytest.assume(res1 == True)
    #     # 点击自选item
    #     res2 = order.c_optional_item()
    #     pytest.assume(res2 == True)
    #     # 输入数量
    #     order.c_hand()
    #     # 下单
    #     res3 = order.c_orderbuy()
    #     assert res3 == True
    # # # 走势跳转行情页
    # # @pytest.mark.usefixtures('back_fixture')
    # # def test_trend_to_hq(self, setup_fixture):
    # #     order, tradehome, optional = setup_fixture
    # #     # 切换走势
    # #     res = order.c_trend()
    # #     pytest.assume(res == True)
    # #     # 双击跳转行情页
    # #     order.double_c_trend()
    # # # 全部平仓
    # # @pytest.mark.usefixtures('back_fixture')
    # # def test_all_flat(self, setup_fixture):
    # #     order, tradehome, optional = setup_fixture
    # #     count = 0
    # #     while count == 0:
    # #         # 获取第一条持仓可用数量
    # #         count = order.get_hold_count()
    # #         if count == 0:
    # #             order.c_hand()
    # #             order.c_orderbuy()
    # #             order.c_ordersell()
    # #         else:
    # #             # 全部平仓
    # #             order.c_hold_more()
    # #             res = order.c_all_flat()
    # #             pytest.assume("成功" in res)
    # # # 快捷反手
    # # @pytest.mark.usefixtures('back_fixture')
    # # def test_quick_back(self, setup_fixture):
    # #     order, tradehome, optional = setup_fixture
    # #     count = 0
    # #     while count == 0:
    # #         # 获取第一条持仓可用数量
    # #         count = order.get_hold_count()
    # #         if count == 0:
    # #             order.c_hand()
    # #             order.c_orderbuy()
    # #             order.c_ordersell()
    # #         else:
    # #             # 全部平仓
    # #             order.c_hold_more()
    # #             res = order.c_quick_back()
    # #             pytest.assume("成功" in res)
# 传统风格
    # FOK买入开仓
    @pytest.mark.usefixtures('back_fixture')
    def test_FOK_traditionalbuy(self, setup_fixture):
        order, tradehome, optional = setup_fixture
        # 切换传统风格
        res = order.change_style("传统")
        pytest.assume(res == True)
        # 勾选FOK
        order.c_price_ztj()
        res1 = order.c_FOK()
        pytest.assume(res1 == True)
        # 输入数量
        order.c_hand()
        # 传统下单
        res2 = order.c_traditional_buy()
        pytest.assume(res2 == True)
        # 切换三键风格
        order.change_style("三键")
    # 备兑卖出开仓
    @pytest.mark.usefixtures('back_fixture')
    def test_traditional_coveredsell(self, setup_fixture):
        order, tradehome, optional = setup_fixture
        # 切换传统风格
        res = order.change_style("传统")
        pytest.assume(res == True)
        # 勾选备兑
        order.c_traditional_covered()
        # 输入数量
        order.c_hand()
        # 备兑开仓(因其委托失败与账号相关，在此不对服务器返回委托结果断言)
        res2 = order.c_traditional_sell()
        # pytest.assume(res2 == True)
        # 切换三键风格
        order.change_style("三键")
    # 平仓（有持仓）
    @pytest.mark.usefixtures('back_fixture')
    def test_traditional_flat(self, setup_fixture):
        order, tradehome, optional = setup_fixture
        # 切换传统风格
        res = order.change_style("传统")
        # 点击持仓切换
        type = order.get_hold_type()
        if type == "权力":
            # 传统买入平仓失败
            res = order.c_traditional_buy_flat()
            pytest.assume(res == False)
            # 传统卖出平仓成功
            res = order.c_traditional_sell_flat()
            pytest.assume(res == True)
        elif type == "义务":
            # 传统买入平仓失败
            res = order.c_traditional_buy_flat()
            pytest.assume(res == False)
            # 传统卖出平仓成功
            res = order.c_traditional_sell_flat()
            pytest.assume(res == True)
        # 切换三键风格
        order.change_style("三键")
    # 平仓（无持仓，无法平仓）







