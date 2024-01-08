__author__ = 'Administrator'
from businessPage.trade_first_page import TradeFirst
from businessPage.search_page import Search
import pytest,time,logging
from selenium.webdriver.common.by import By
from common.common_fun import Common

#查询用例
@pytest.mark.usefixtures('login_fixture')
@pytest.mark.usefixtures('driver_fixture')
class TestSearch():
    @pytest.fixture(scope='function', autouse=False)
    def setup_fixture(self, driver_fixture):
        print("开始执行前置")
        driver = driver_fixture
        toSearch = TradeFirst(driver)
        toSearch.to_trade_page()
        toSearch.to_search()
        daySearch = Search(driver)
        return toSearch, daySearch
    #查询当日成交
    @pytest.mark.usefixtures('search_fixture')
    def test_Search_daytrad(self,setup_fixture):
        toSearch,daySearch = setup_fixture
        daytrad = daySearch.search_day_transaction()
        assert daytrad==True
#查询当日委托
    @pytest.mark.usefixtures('search_fixture')
    def test_Search_dayentrust(self,setup_fixture):
        toSearch,daySearch = setup_fixture
        daytrad=daySearch.search_day_entrust()
        assert daytrad==True
#查询历史成交
    @pytest.mark.usefixtures('search_fixture')
    def test_Search_histrad(self,setup_fixture):
        toSearch,daySearch = setup_fixture
        daytrad=daySearch.search_history_transaction()
        assert daytrad==True
#查询当日行权被指派
    @pytest.mark.usefixtures('search_fixture')
    def test_Search_dayexe(self,setup_fixture):
        toSearch, daySearch = setup_fixture
        daytrad=daySearch.search_day_exercise()
        assert daytrad==True
#查询历史行权被指派
    @pytest.mark.usefixtures('search_fixture')
    def test_Search_hisexe(self,setup_fixture):
        toSearch,daySearch = setup_fixture
        daytrad=daySearch.search_history_exercise()
        assert daytrad==True
#查询锁定解锁
    @pytest.mark.usefixtures('search_fixture')
    def test_Search_clok(self,setup_fixture):
        toSearch,daySearch = setup_fixture
        daytrad=daySearch.search_clok_unclok()
        assert daytrad==True

#查询历史资金流水
    @pytest.mark.usefixtures('search_fixture')
    def test_Search_hiscapflow(self,setup_fixture):
        toSearch,daySearch = setup_fixture
        daytrad=daySearch.search_hiscapitalflow()
        assert daytrad==True
#查询当日行权委托
    @pytest.mark.usefixtures('search_fixture')
    def test_Search_dayexetru(self,setup_fixture):
        toSearch,daySearch = setup_fixture
        daytrad=daySearch.search_day_exentrust()
        assert daytrad==True
##组合策略持仓查询
    @pytest.mark.usefixtures('search_fixture')
    def test_Search_grouposition(self,setup_fixture):
        toSearch,daySearch = setup_fixture
        daytrad=daySearch.search_group_Position()
        assert daytrad==True
##组合策略信息查询
    @pytest.mark.usefixtures('search_fixture')
    def test_Search_groupinform(self,setup_fixture):
        toSearch,daySearch = setup_fixture
        daytrad=daySearch.search_group_message()
##组合策略流水查询
    @pytest.mark.usefixtures('search_fixture')
    def test_Search_groupflow(self,setup_fixture):
        toSearch,daySearch = setup_fixture
        daytrad=daySearch.search_stream()
        assert daytrad==True

##历史组合委托流水查询
    @pytest.mark.usefixtures('search_fixture')
    def test_Search_hisgroupflow(self,setup_fixture):
        toSearch,daySearch = setup_fixture
        daytrad=daySearch.search_history_stream()
        assert daytrad==True
