from common.common_fun import Common
from businessPage.trade_first_page import TradeFirst
from businessPage.first_page import First
from businessPage.contract_screen_page import Screen
from businessPage.contract_page import Contract
from businessPage.order_page import Order
from businessPage.optional_page import Optional
from common.collector_log import my_log

from appium.webdriver.common.mobileby import MobileBy
import pytest
#行情分时页面用例
@pytest.mark.usefixtures('login_fixture')
@pytest.mark.usefixtures('driver_fixture')
class TestOrder():
    @pytest.fixture(scope='function', autouse=False)
    def setup_fixture(self, driver_fixture):
        driver = driver_fixture
        tradehome = TradeFirst(driver)
        first = First(driver)
        screen = Screen(driver)
        contract = Contract(driver)
        order = Order(driver)
        optional = Optional(driver)
        tradehome.to_first_page()
        first.to_contract_screen()
        return screen, contract, first, optional, order
    # 顶部箭头切换合约
    @pytest.mark.usefixtures('back_fixture')
    def test_arrow(self,setup_fixture):
        screen, contract, first, optional, order = setup_fixture
        screen.screen_toK()
        old_title,new_title = contract.arrow("right")
        pytest.assume(old_title != new_title)
        old_title1, new_title1 = contract.arrow("left")
        pytest.assume(old_title == new_title1)
        screen.hq_back()
    # 切换K线类型
    @pytest.mark.usefixtures('back_fixture')
    def test_cycle(self,setup_fixture):
        data = ["日" ,"周" ,"月" ,"年" ,"分时"]
        screen, contract, first, optional, order = setup_fixture
        screen.screen_toK()
        for i in data:
            contract.cycle(i)
        screen.hq_back()
    # 切换
    @pytest.mark.usefixtures('back_fixture')
    def test_amount(self,setup_fixture):
        type = ["MACD","KDJ","RSI","VOLUME"]
        screen, contract, first, optional, order = setup_fixture
        screen.screen_toK()
        contract.cycle("日")
        for i in type:
            contract.amount(i)
        screen.hq_back()
    # T型报价
    @pytest.mark.usefixtures('back_fixture')
    def test_tPrice(self,setup_fixture):
        screen, contract, first, optional, order = setup_fixture
        screen.screen_toK()
        contract.tPrice()
        screen.hq_back()
    # 明细
    @pytest.mark.usefixtures('back_fixture')
    def test_Detailed(self, setup_fixture):
        screen, contract, first, optional, order = setup_fixture
        screen.screen_toK()
        contract.Detailed()
        screen.hq_back()
    # 盘口
    @pytest.mark.usefixtures('back_fixture')
    def test_Handicap(self,setup_fixture):
        screen, contract, first, optional, order = setup_fixture
        screen.screen_toK()
        contract.Handicap()
        screen.hq_back()
    # 指数
    @pytest.mark.usefixtures('back_fixture')
    def test_index(self,setup_fixture):
        screen, contract, first, optional, order = setup_fixture
        screen.screen_toK()
        contract.index()
        screen.hq_back()
    # 快买
    @pytest.mark.usefixtures('back_fixture')
    def test_fastBuy(self,setup_fixture):
        screen, contract, first, optional, order = setup_fixture
        screen.screen_toK()
        res = contract.fastBuy()
        pytest.assume(res == True)
        screen.hq_back()
    # 快卖
    @pytest.mark.usefixtures('back_fixture')
    def test_fastSell(self,setup_fixture):
        screen, contract, first, optional, order = setup_fixture
        screen.screen_toK()
        res = contract.fastSell()
        pytest.assume(res == True)
        screen.hq_back()
    # 交易
    @pytest.mark.usefixtures('back_fixture')
    def test_toOrder(self,setup_fixture):
        screen, contract, first, optional, order = setup_fixture
        screen.screen_toK()
        contract.to_order()
        res = contract.find_element(order.contract,"下单页合约输入框")
        pytest.assume(res == True)
        order.back()
        screen.hq_back()
    # 加自选
    @pytest.mark.usefixtures('back_fixture')
    def test_addSelf(self,setup_fixture):
        screen, contract, first, optional, order = setup_fixture
        contract_name = screen.c_item()
        addself_text = contract.addSelf()
        screen.hq_back()
        screen.back()
        first.to_optional()
        contract = (MobileBy.XPATH,"//android.widget.TextView[@text='%s']" %contract_name)
        if addself_text == "加自选":
            # 自选中有此合约名称
            res = optional.find_element(contract,"合约%s"%contract_name)
            optional.item_del()
            assert res == True
        elif addself_text == "删自选":
            # 自选中没有此合约名称
            try:
                optional.find_element_noterror(contract_loc, "合约%s"%contract_name)
            except:
                subjectmatter.back()
                res = True
            else:
                optional.item_del()
                res = False
            assert res == True
        else:
            my_log.error("获取合约详情页的“加自选”text为：%s，错误！"%addself_text)

