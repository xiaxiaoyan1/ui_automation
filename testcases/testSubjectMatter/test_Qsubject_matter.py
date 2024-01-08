from common.common_fun import Common
from businessPage.trade_first_page import TradeFirst
from businessPage.contract_page import Contract
from businessPage.optional_page import Optional
from businessPage.first_page import First
from businessPage.subject_matter_page import SubjectMatter
from common.collector_log import my_log

from appium.webdriver.common.mobileby import MobileBy
import pytest
#合约标的
@pytest.mark.usefixtures('login_fixture')
@pytest.mark.usefixtures('driver_fixture')
class TestOrder():
    @pytest.fixture(scope='function', autouse=False)
    def setup_fixture(self, driver_fixture):
        driver = driver_fixture
        tradehome = TradeFirst(driver)
        first = First(driver)
        subjectmatter = SubjectMatter(driver)
        contract = Contract(driver)
        optional = Optional(driver)
        tradehome.to_first_page()
        return subjectmatter, contract, first, optional
    # 指数行情页
    @pytest.mark.usefixtures('back_fixture')
    def test_index(self,setup_fixture):
        subjectmatter, contract, first, optional= setup_fixture
        for i in range(6):
            first.to_hq()
            text = subjectmatter.c_index(i)
            # K线周期切换
            data = ["日", "周", "月", "年"]
            for i in data:
                contract.cycle(i)
            # 成交量等值切换
            type = ["MACD", "KDJ", "RSI", "VOLUME"]
            contract.cycle("日")
            for i in type:
                contract.amount(i)
            # 指数框切换
            contract.index()
            # 资金
            subjectmatter.Capital(text)
            # 新闻
            subjectmatter.News(text)
            # 加自选
            contract_name = contract.get_element_text(contract.title,text)
            addself_text = contract.addSelf()
            contract.hq_back()
            subjectmatter.back()
            first.to_optional()
            contract_loc = (MobileBy.XPATH, "//android.widget.TextView[@text='%s']" % contract_name)
            if addself_text == "加自选":
                # 自选中有此合约名称
                res = optional.find_element(contract_loc, "合约")
                optional.item_del()
                assert res == True
            elif addself_text == "删自选":
                # 自选中没有此合约名称
                try:
                    optional.find_element_noterror(contract_loc, "合约")
                except:
                    subjectmatter.back()
                    res = True
                else:
                    subjectmatter.back()
                    my_log.error("%s加减自选失败"% text)
                    res = False
                assert res == True
            else:
                my_log.error("获取合约详情页的“加自选”text为：%s，错误！" % addself_text)
    # ETF行情页
    @pytest.mark.usefixtures('back_fixture')
    def test_ETF(self, setup_fixture):
        subjectmatter, contract, first, optional = setup_fixture
        for i in range(3):
            first.to_hq()
            text = subjectmatter.c_ETF(i)
            # K线周期切换
            data = ["日", "周", "月", "年", "分时"]
            for i in data:
                contract.cycle(i)
            # 成交量等值切换
            type = ["MACD", "KDJ", "RSI", "VOLUME"]
            contract.cycle("日")
            for i in type:
                contract.amount(i)
            # 指数框切换
            contract.index()
            # 期权
            subjectmatter.option()
            # 加自选
            contract_name = contract.get_element_text(contract.title, text)
            addself_text = contract.addSelf()
            contract.hq_back()
            subjectmatter.back()
            subjectmatter.back()
            first.to_optional()
            contract_loc = (MobileBy.XPATH, "//android.widget.TextView[@text='%s']" % contract_name)
            if addself_text == "加自选":
                # 自选中有此合约名称
                res = optional.find_element(contract_loc, "合约%s"%contract_name)
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
                my_log.error("获取合约详情页的“加自选”text为：%s，错误！" % addself_text)
