from businessPage.choice_oder_page import ChoiceOrder
from businessPage.order_page import Order
from businessPage.entrust_style_page import Style
from businessPage.trade_first_page import TradeFirst

from common.common_fun import Common
from selenium.webdriver.common.by import By
import pytest
#委托风格用例
@pytest.mark.usefixtures('login_fixture')
@pytest.mark.usefixtures('driver_fixture')
class TestStyle():
    @pytest.fixture(scope='function', autouse=False)
    def setup_fixture(self, driver_fixture):
        driver = driver_fixture
        tradehome = TradeFirst(driver)
        style = Style(driver)
        choiceorder = ChoiceOrder(driver)
        order = Order(driver)
        tradehome.to_trade_page()
        tradehome.to_style()
        return tradehome, style ,choiceorder ,order
    # 传统风格
    @pytest.mark.usefixtures('back_fixture')
    def test_tradition(self,setup_fixture):
        tradehome, style ,choiceorder ,order = setup_fixture
        style.tradition()
        tradehome.to_order()
        choiceorder.c_orderpage()
        result = order.find_traditional_buy()
        assert result == True
    # 三键下单
    @pytest.mark.usefixtures('back_fixture')
    def test_three(self,setup_fixture):
        tradehome, style ,choiceorder ,order = setup_fixture
        style.three()
        tradehome.to_order()
        choiceorder.c_orderpage()
        result = order.find_three_buy()
        assert result == True


