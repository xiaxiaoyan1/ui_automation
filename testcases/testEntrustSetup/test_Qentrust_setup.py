__author__ = 'Administrator'

from businessPage.entrust_setup_page import Setup
from businessPage.trade_first_page import TradeFirst
from businessPage.choice_oder_page import ChoiceOrder
from businessPage.order_page import Order
from common.common_fun import Common
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import pytest
import time
#委托设置用例
@pytest.mark.usefixtures('login_fixture')
@pytest.mark.usefixtures('driver_fixture')
class TestEntrustSetup():
    @pytest.fixture(scope='function', autouse=False)
    def setup_fixture(self, driver_fixture):
        driver = driver_fixture
        tradehome = TradeFirst(driver)
        setup = Setup(driver)
        choiceorder = ChoiceOrder(driver)
        order = Order(driver)
        tradehome.to_trade_page()
        tradehome.to_setup()
        return tradehome, setup,choiceorder,order
# 设置对手价
    @pytest.mark.usefixtures('back_fixture')
    def test_setprice_dsj(self,setup_fixture):
        tradehome, setup,choiceorder,order = setup_fixture
        # 设置对手价并去下单页验证
        setup.setprice_dsj()
        setup.page_back()
        tradehome.to_order()
        choiceorder.c_orderpage()
        el_price_text = order.el_text(order.price,"对手价text")
        pytest.assume(el_price_text == "对手价")
# 设置挂单价
    @pytest.mark.usefixtures('back_fixture')
    def test_setprice_gdj(self,setup_fixture):
        tradehome, setup,choiceorder,order = setup_fixture
        setup.setprice_gdj()
        setup.page_back()
        tradehome.to_order()
        choiceorder.c_orderpage()
        el_price_text = order.el_text(order.price,"挂单价text")
        pytest.assume(el_price_text == "挂单价")
# 设置默认开张单数
    @pytest.mark.usefixtures('back_fixture')
    def test_setDefaultNumber(self,setup_fixture):
        tradehome, setup,choiceorder,order = setup_fixture
        setup.setDefaultNumber(2)
        setup.setDefaultNumber()
    # 设置默认下单增加数量超过9999
    @pytest.mark.usefixtures('back_fixture')
    def test_setadd_defaultNumber(self, setup_fixture):
        tradehome, setup, choiceorder, order = setup_fixture
        setup.setadd_defaultNumber(10000)
        text = setup.toastok_text()
        pytest.assume(text == "默认下单增加数量不能超过1~9999")
        setup.toastok()
        setup.setadd_defaultNumber()
# 设置默认下单增加数量
    @pytest.mark.usefixtures('back_fixture')
    def test_setadd_defaultNumber(self,setup_fixture):
        tradehome, setup,choiceorder,order = setup_fixture
        setup.setadd_defaultNumber(2)
        setup.page_back()
        tradehome.to_order()
        choiceorder.c_orderpage()
        el_add_defaultNumber_text = order.el_text(order.add_hand,"默认下单增加数量text")
        pytest.assume(el_add_defaultNumber_text == "2")
        # 恢复之前的设置
        setup.page_back()
        tradehome.to_setup()
        setup.setadd_defaultNumber()
    # 设置关闭下单确认开关
    @pytest.mark.usefixtures('back_fixture')
    def test_setorder_switch_off(self,setup_fixture):
        tradehome, setup,choiceorder,order = setup_fixture
        setup.setorder_switch()
        order_switch_text = setup.el_text(setup.order_switch,"下单确认开关text")
        pytest.assume("关" in order_switch_text)
        print(order_switch_text)
        # 去下单页
        setup.page_back()
        tradehome.to_order()
        choiceorder.c_orderpage()
        # 验证是否关闭下单确认
        order.c_hand(1)
        res = order.c_orderbuy_no_ture()
        pytest.assume(res == False)
    # 设置打开下单确认开关
    @pytest.mark.usefixtures('back_fixture')
    def test_setorder_switch_on(self, setup_fixture):
        tradehome, setup, choiceorder, order = setup_fixture
        setup.setorder_switch()
        order_switch_text = setup.el_text(setup.order_switch, "下单确认开关text")
        pytest.assume("开" in order_switch_text)
        print(order_switch_text)
        # 去下单页
        setup.page_back()
        tradehome.to_order()
        choiceorder.c_orderpage()
        # 验证是否关闭下单确认
        order.c_hand(1)
        res = order.c_orderbuy_no_ture()
        pytest.assume(res == True)
# 设置下单风险提示开关
    @pytest.mark.usefixtures('back_fixture')
    def test_setrisk_switch(self,setup_fixture):
        tradehome, setup,choiceorder,order = setup_fixture
        setup.setrisk_switch()
        risk_switch_text = setup.el_text(setup.risk_switch,"下单风险提示开关text")
        pytest.assume("关" in risk_switch_text)
        setup.setrisk_switch()
        risk_switch_text = setup.el_text(setup.risk_switch,"下单风险提示开关text")
        pytest.assume("开" in risk_switch_text)
# 拆单时间间隔
    @pytest.mark.usefixtures('back_fixture')
    def test_setrl_defaultTime(self,setup_fixture):
        tradehome, setup,choiceorder,order = setup_fixture
        setup.setrl_defaultTime(500)
        setrl_defaultTime_text = setup.el_text(setup.rl_defaultTime,"拆单时间间隔text")
        pytest.assume(setrl_defaultTime_text == "500")
        setup.setrl_defaultTime(400)
        setrl_defaultTime_text = setup.el_text(setup.rl_defaultTime,"拆单时间间隔text")
        pytest.assume(setrl_defaultTime_text == "400")
# 限价拆单开关
    @pytest.mark.usefixtures('back_fixture')
    def test_setxj_defaultDivide_switch(self,setup_fixture):
        tradehome, setup,choiceorder,order = setup_fixture
        setup.setxj_defaultDivide_switch()
        xj_defaultDivide_switch_text = setup.el_text(setup.xj_defaultDivide_switch,"限价拆单开关text")
        pytest.assume("开" in xj_defaultDivide_switch_text)
        setup.setxj_defaultDivide_switch()
        xj_defaultDivide_switch_text = setup.el_text(setup.xj_defaultDivide_switch,"限价拆单开关text")
        pytest.assume("关" in xj_defaultDivide_switch_text)
# 限价每张拆单张数
    @pytest.mark.usefixtures('back_fixture')
    def test_setrl_xj_defaultDivideNum(self,setup_fixture):
        tradehome, setup,choiceorder,order = setup_fixture
        setup.setrl_xj_defaultDivideNum(40)
        rl_xj_defaultDivideNum_text = setup.el_text(setup.rl_xj_defaultDivideNum,"限价每张拆单张数text")
        pytest.assume(rl_xj_defaultDivideNum_text == "40")
        setup.setrl_xj_defaultDivideNum(50)
        rl_xj_defaultDivideNum_text = setup.el_text(setup.rl_xj_defaultDivideNum,"限价每张拆单张数text")
        pytest.assume(rl_xj_defaultDivideNum_text == "50")
# 市价拆单开关设置
    @pytest.mark.usefixtures('back_fixture')
    def test_setsj_defaultDivide_switch(self,setup_fixture):
        tradehome, setup,choiceorder,order = setup_fixture
        setup.setsj_defaultDivide_switch()
        sj_defaultDivide_switch_text = setup.el_text(setup.sj_defaultDivide_switch,"市价拆单开关设置text")
        pytest.assume("开" in sj_defaultDivide_switch_text)
        setup.setsj_defaultDivide_switch()
        sj_defaultDivide_switch_text = setup.el_text(setup.sj_defaultDivide_switch,"市价拆单开关设置text")
        pytest.assume("关" in sj_defaultDivide_switch_text)
# 市价每单拆单张数
    @pytest.mark.usefixtures('back_fixture')
    def test_setrl_sj_defaultDivideNum(self,setup_fixture):
        tradehome, setup,choiceorder,order = setup_fixture
        setup.setrl_sj_defaultDivideNum(5)
        rl_sj_defaultDivideNum_text = setup.el_text(setup.rl_sj_defaultDivideNum,"市价每单拆单张数text")
        pytest.assume(rl_sj_defaultDivideNum_text == "5")
        setup.setrl_sj_defaultDivideNum(10)
        rl_sj_defaultDivideNum_text = setup.el_text(setup.rl_sj_defaultDivideNum,"市价每单拆单张数text")
        pytest.assume(rl_sj_defaultDivideNum_text == "10")

    @pytest.mark.usefixtures('back_fixture')
    def test_setposition_save(self, setup_fixture):
        tradehome, setup, choiceorder, order = setup_fixture
        res = setup.setposition_save()
        position_save_text = setup.el_text(setup.rl_positionFilterConditions, "持仓过滤条件text")
        assert position_save_text == res
    @pytest.mark.usefixtures('back_fixture')
    def test_setposition_notsave(self,setup_fixture):
        tradehome, setup,choiceorder,order = setup_fixture
        res = setup.setposition_save()
        position_notsave_text = setup.el_text(setup.rl_positionFilterConditions,"持仓过滤条件text")
        assert position_notsave_text == res
    @pytest.mark.usefixtures('back_fixture')
    def test_setlogin_15(self,setup_fixture):
        tradehome, setup,choiceorder,order = setup_fixture
        setup.setlogin_15()
        setlogin_text = setup.el_text(setup.rl_setting_login_time,"设置登录时长text")
        pytest.assume(setlogin_text == "15分钟后自动退出")
    @pytest.mark.usefixtures('back_fixture')
    def test_setlogin_30(self,setup_fixture):
        tradehome, setup,choiceorder,order = setup_fixture
        setup.setlogin_30()
        setlogin_text = setup.el_text(setup.rl_setting_login_time,"设置登录时长text")
        pytest.assume(setlogin_text == "30分钟后自动退出")
    @pytest.mark.usefixtures('back_fixture')
    def test_setlogin_always(self,setup_fixture):
        tradehome, setup,choiceorder,order = setup_fixture
        setup.setlogin_always()
        setlogin_text = setup.el_text(setup.rl_setting_login_time,"设置登录时长text")
        pytest.assume(setlogin_text == "始终登录")