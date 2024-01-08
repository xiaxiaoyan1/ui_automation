from common.common_fun import Common
import pytest,random

from businessPage.trade_first_page import TradeFirst
from businessPage.first_page import First
from businessPage.contract_screen_page import Screen
from businessPage.optional_page import Optional
from common.collector_log import my_log
#合约筛选用例
@pytest.mark.usefixtures('login_fixture')
@pytest.mark.usefixtures('driver_fixture')
class TestContractScreen():
    @pytest.fixture(scope='function', autouse=False)
    def setup_fixture(self, driver_fixture):
        driver = driver_fixture
        tradehome = TradeFirst(driver)
        first = First(driver)
        screen = Screen(driver)
        optional = Optional(driver)
        tradehome.to_first_page()
        first.to_contract_screen()
        return screen,first,optional
    #最新价排序
    @pytest.mark.usefixtures('back_fixture')
    def test_new_price(self, setup_fixture):
        screen,first,optional = setup_fixture
        # 降序
        screen.c_new_price()
        res = screen.desc(1)
        pytest.assume(res == True)
        # 升序
        screen.c_new_price()
        res = screen.asc(1)
        pytest.assume(res == True)
    #涨跌排序
    @pytest.mark.usefixtures('back_fixture')
    def test_rise(self, setup_fixture):
        screen,first,optional = setup_fixture
        # 降序
        screen.c_rise()
        res = screen.desc(2)
        pytest.assume(res == True)
        # 升序
        screen.c_rise()
        res = screen.asc(2)
        pytest.assume(res == True)
    #合约筛选
    @pytest.mark.usefixtures('back_fixture')
    def test_sx(self, setup_fixture):
        screen,first,optional = setup_fixture
        for i in range(10):
            j = random.randint(0, 2)
            k = random.randint(0, 4)
            l = random.randint(0, 6)
            m = random.randint(0, 3)
            n = random.randint(0, 1)
            screen.to_sx()
            res = screen.c_sx(j,k,l,m,n)
            text = screen.sx_text()
            if res != text:
                my_log.error("执行的筛选操作是'%s'"% res)
                my_log.error("筛选后的结果是'%s'" % text)
                my_log.error("筛选组合%d+%d+%d+%d+%d出错"%(j,k,l,m,n))
                Common.error_save_screenshot("筛选组合%d+%d+%d+%d+%d出错"%(j,k,l,m,n))
            print(type(res),type(text),res,text)
            pytest.assume(res == text)

    # 保存筛选条件
    @pytest.mark.usefixtures('back_fixture')
    def test_save(self, setup_fixture):
        screen,first,optional = setup_fixture
        screen.to_sx()
        screen.c_save()
        # 认购、当月、深实值、非常活跃、上证50ETF
        screen.c_sx(1,1,1,1,0)
        text1 = screen.sx_text()
        screen.to_sx()
        screen.c_btn_ok()
        text2 = screen.sx_text()
        print(text2, text1)
        # 恢复至不保存状态
        screen.to_sx()
        screen.c_save()
        screen.c_btn_ok()
        assert text2 == text1
    # 搜索股票跳转行情
    @pytest.mark.usefixtures('back_fixture')
    def test_search_toK(self, setup_fixture):
        screen,first,optional = setup_fixture
        screen.c_search()
        res = screen.search_toK()
        screen.hq_back()
        assert res == True
    # 筛选跳转行情
    @pytest.mark.usefixtures('back_fixture')
    def test_screen_toK(self, setup_fixture):
        screen,first,optional = setup_fixture
        res = screen.screen_toK()
        screen.hq_back()
        assert res == True
    # 搜索-加自选
    @pytest.mark.usefixtures('back_fixture')
    def test_search_add(self, setup_fixture):
        screen,first,optional = setup_fixture
        screen.c_search()
        screen.c_input("000")
        res1 = screen.addself_list()
        print("res1:%s"%res1)
        screen.back()
        screen.back()
        first.to_optional()
        res2 = optional.zx_name_all()
        print("res2:%s"%res2)
        res = True
        for i in res1:
            if i in res2:
                pass
            else:
                res = False
        # 清空自选
        optional.item_del()
        assert res == True

