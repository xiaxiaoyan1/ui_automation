from common.common_fun import Common
from businessPage.first_page import First
from businessPage.trade_first_page import TradeFirst

from selenium.webdriver.common.by import By
import pytest
#首页用例
@pytest.mark.usefixtures('login_fixture')
@pytest.mark.usefixtures('driver_fixture')
class TestClok():
    @pytest.fixture(scope='function', autouse=False)
    def setup_fixture(self, driver_fixture):
        driver = driver_fixture
        tradehome = TradeFirst(driver)
        first = First(driver)
        tradehome.to_first_page()
        return first
    # 策略交易
    @pytest.mark.usefixtures('back_fixture')
    def test_to_strategy(self,setup_fixture):
        first = setup_fixture
        res = first.to_strategy()
        first.back()
        assert res == True
    # 期权交易
    @pytest.mark.usefixtures('back_fixture')
    def test_to_trade(self,setup_fixture):
        first = setup_fixture
        res = first.to_trade()
        assert res == True
    # 重要通告
    @pytest.mark.usefixtures('back_fixture')
    def test_to_notice(self,setup_fixture):
        first = setup_fixture
        res = first.to_notice()
        assert res == True
    # 自选
    @pytest.mark.usefixtures('back_fixture')
    def test_to_optional(self,setup_fixture):
        first = setup_fixture
        res = first.to_optional()
        assert res == True
    # 市场统计
    @pytest.mark.usefixtures('back_fixture')
    def test_to_statistics(self,setup_fixture):
        first = setup_fixture
        text1,text2 = first.to_statistics()
        print(text1,text2)
        assert (text1 >= 0 and text2 >= 0)
    # 波动指数
    @pytest.mark.usefixtures('back_fixture')
    def test_to_wave_index(self,setup_fixture):
        first = setup_fixture
        res = first.to_wave_index()
        first.hq_back()
        assert res == True