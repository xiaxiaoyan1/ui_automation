from common.common_fun import Common
from businessPage.gp_new_page import Gp
from businessPage.trade_first_page import TradeFirst
from businessPage.optional_page import Optional
from businessPage.change_password_page import ChangePwd

from selenium.webdriver.common.by import By
import pytest
#首页用例
@pytest.mark.usefixtures('gp_teardown_fixture')
@pytest.mark.usefixtures('gp_login_fixture')
@pytest.mark.usefixtures('login_fixture')
@pytest.mark.usefixtures('driver_fixture')
@pytest.mark.usefixtures('old_pwd')
class TestGp():
    @pytest.fixture(scope='function', autouse=False)
    def setup_fixture(self, driver_fixture):
        driver = driver_fixture
        tradehome = TradeFirst(driver)
        optional = Optional(driver)
        gp = Gp(driver)
        changepwd = ChangePwd(driver)
        common = Common(driver)
        tradehome.to_trade_page()
        gp.tipGp()
        return gp,tradehome,optional,common,changepwd
    # 查看资金详情
    @pytest.mark.usefixtures('back_fixture')
    def test_zjxq(self,setup_fixture):
        gp,tradehome,optional,common,changepwd = setup_fixture
        res = gp.tipzzc()
        assert res == True
    # 去标识化
    @pytest.mark.usefixtures('back_fixture')
    def test_qbsh(self, setup_fixture):
        gp,tradehome,optional,common,changepwd = setup_fixture
        # 点击去标识化
        res = gp.tipqbsh()
        pytest.assume(res == True)
        res1 = gp.tipqbsh()
        pytest.assume(res1 == True)
    # 买入
    @pytest.mark.usefixtures('back_fixture')
    def test_buy(self, setup_fixture):
        gp,tradehome,optional,common,changepwd = setup_fixture
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
    # 买入-带入持仓股
    @pytest.mark.usefixtures('back_fixture')
    def test_buy_hold(self, setup_fixture):
        gp,tradehome,optional,common,changepwd = setup_fixture
        # 进入限价页面
        gp.tipxj()
        # 点击买入
        gp.tipbuy()
        # 点击持仓带入数据
        res = gp.c_hold()
        assert res == True
    # 买入-带入涨停价、跌停价、五档买卖价
    @pytest.mark.usefixtures('back_fixture')
    def test_buy_zt(self, setup_fixture):
        gp,tradehome,optional,common,changepwd = setup_fixture
        # 进入限价页面
        gp.tipxj()
        # 点击买入
        gp.tipbuy()
        # 点击持仓带入数据
        res = gp.c_hold()
        pytest.assume(res == True)
        # 点击涨停带入数据
        res = gp.send_ztj()
        pytest.assume(res == True)
        # 点击跌停带入数据
        res = gp.send_dtj()
        pytest.assume(res == True)
        # 点击五档买卖带入数据
        res = gp.send_fiveprice()
        pytest.assume(res == True)
    # 全仓/半仓仓位
    @pytest.mark.usefixtures('back_fixture')
    def test_buy_all_hold(self,setup_fixture):
        gp,tradehome,optional,common,changepwd = setup_fixture
        # 进入限价页面
        gp.tipxj()
        # 点击买入
        gp.tipbuy()
        # 输入合约代码并带入价格,默认“000001”
        gp.input_contract()
        # 获取可买数
        num = gp.trade_num()
        # 全仓操作
        gp.c_all()
        # 判断
        num_all = gp.trade_num()
        pytest.assume(num_all == num)
        # 半仓操作
        gp.c_half()
        # 判断
        num_all = gp.trade_num()
        pytest.assume(num_all == num // 2)
        # 1/3仓操作
        gp.c_third()
        # 判断
        num_all = gp.trade_num()
        pytest.assume(num_all == num // 3)
        # 1/4仓操作
        gp.c_quarter()
        # 判断
        num_all = gp.trade_num()
        pytest.assume(num_all == num // 4)
    # 加减价格/数量后买入
    @pytest.mark.usefixtures('back_fixture')
    def test_buy_chenge_price(self,setup_fixture):
        gp,tradehome,optional,common,changepwd = setup_fixture
        # 进入限价页面
        gp.tipxj()
        # 点击买入
        gp.tipbuy()
        # 输入合约代码并带入价格,默认“000001”
        gp.input_contract()
        # 加价格
        gp.add_price()
        # 减价格
        gp.del_price()
        # 输入数量，默认“100”
        gp.input_num()
        # 加数量
        gp.add_num()
        # 减数量
        gp.del_num()
        # 买入
        gp.c_buy()

    # 卖出
    @pytest.mark.usefixtures('back_fixture')
    def test_sell(self, setup_fixture):
        gp,tradehome,optional,common,changepwd = setup_fixture
        # 进入买入页面
        gp.tipxj()
        # 点击卖出
        gp.tipsell()
        # 输入合约代码并带入价格,默认“000001”
        gp.input_contract()
        # 输入数量，默认“100”
        gp.input_num()
        # 卖出
        gp.c_sell()
    # 卖出-带入持仓股
    @pytest.mark.usefixtures('back_fixture')
    def test_sell_hold(self, setup_fixture):
        gp,tradehome,optional,common,changepwd = setup_fixture
        # 进入买入页面
        gp.tipxj()
        # 点击卖出
        gp.tipsell()
        # 点击持仓带入数据
        res = gp.c_hold()
        # 输入数量，默认“100”
        gp.input_num()
        # 卖出
        gp.c_sell()
        assert res == True
    # 卖出-带入涨停价、跌停价、五档买卖价
    @pytest.mark.usefixtures('back_fixture')
    def test_sell_zt(self, setup_fixture):
        gp,tradehome,optional,common,changepwd = setup_fixture
        # 进入限价页面
        gp.tipxj()
        # 点击卖出
        gp.tipsell()
        # 点击持仓带入数据
        res = gp.c_hold()
        pytest.assume(res == True)
        # 点击涨停带入数据
        res = gp.send_ztj()
        pytest.assume(res == True)
        # 点击跌停带入数据
        res = gp.send_dtj()
        pytest.assume(res == True)
        # 点击五档买卖带入数据
        res = gp.send_fiveprice()
        pytest.assume(res == True)
    # 全仓/半仓仓位
    @pytest.mark.usefixtures('back_fixture')
    def test_sell_all_hold(self,setup_fixture):
        gp,tradehome,optional,common,changepwd = setup_fixture
        # 进入限价页面
        gp.tipxj()
        # 点击卖出
        gp.tipsell()
        # 点击持仓带入数据
        res = gp.c_hold()
        # 获取可买数
        num = gp.trade_num()
        # 全仓操作
        gp.c_all()
        # 判断
        num_all = gp.trade_num()
        pytest.assume(num_all == num)
        # 半仓操作
        gp.c_half()
        # 判断
        num_all = gp.trade_num()
        pytest.assume(num_all == num // 2)
        # 1/3仓操作
        gp.c_third()
        # 判断
        num_all = gp.trade_num()
        pytest.assume(num_all == num // 3)
        # 1/4仓操作
        gp.c_quarter()
        # 判断
        num_all = gp.trade_num()
        pytest.assume(num_all == num // 4)
    # 加减价格/数量后卖出
    @pytest.mark.usefixtures('back_fixture')
    def test_sell_chenge_price(self,setup_fixture):
        gp,tradehome,optional,common,changepwd = setup_fixture
        # 进入限价页面
        gp.tipxj()
        # 点击卖出
        gp.tipsell()
        # 点击持仓带入数据
        res = gp.c_hold()
        # 加价格
        gp.add_price()
        # 减价格
        gp.del_price()
        # 输入数量，默认“100”
        gp.input_num()
        # 加数量
        gp.add_num()
        # 减数量
        gp.del_num()
        # 买入
        gp.c_buy()

    # 加/减自选
    @pytest.mark.usefixtures('back_fixture')
    def test_zx1(self, setup_fixture):
        gp,tradehome,optional,common,changepwd = setup_fixture
        # 进入买入页
        gp.tipxj()
        # 输入代码，默认”000001“
        gp.input_contract()
        # 获取股票名称
        name = gp.title_text()
        # 查看当前股票是否已加自选，Ture：已加，False：未加
        res = gp.zx_state()
        if res == True:
            # 删自选
            gp.c_zx()
            # 进入自选页
            gp.back()
            tradehome.to_optional_page()
            # 查看自选页是否存在此股票
            res = optional.have_zx(name)
            assert res == False
        else:
            # 加自选
            gp.c_zx()
            # 进入自选页
            gp.back()
            tradehome.to_optional_page()
            # 查看自选页是否存在此股票
            res = optional.have_zx(name)
            assert res == True
    # 加/减自选
    @pytest.mark.usefixtures('back_fixture')
    def test_zx2(self, setup_fixture):
        gp,tradehome,optional,common,changepwd = setup_fixture
        # 进入买入页
        gp.tipxj()
        # 输入代码，默认”000001“
        gp.input_contract()
        # 获取股票名称
        name = gp.title_text()
        # 查看当前股票是否已加自选，Ture：已加，False：未加
        res = gp.zx_state()
        if res == True:
            # 删自选
            gp.c_zx()
            # 进入自选页
            gp.back()
            tradehome.to_optional_page()
            # 查看自选页是否存在此股票
            res = optional.have_zx(name)
            assert res == False
        else:
            # 加自选
            gp.c_zx()
            # 进入自选页
            gp.back()
            tradehome.to_optional_page()
            # 查看自选页是否存在此股票
            res = optional.have_zx(name)
            assert res == True
    # 更多-加/减自选
    @pytest.mark.usefixtures('back_fixture')
    def test_zx3(self, setup_fixture):
        gp,tradehome,optional,common,changepwd = setup_fixture
        # 进入买入页
        gp.tipxj()
        # 输入代码，默认”000001“
        gp.input_contract()
        # 获取股票名称
        name = gp.title_text()
        # 查看当前股票是否已加自选，Ture：已加，False：未加
        res = gp.zx_state()
        if res == True:
            # 删自选
            gp.c_more_zx()
            # 进入自选页
            gp.back()
            tradehome.to_optional_page()
            # 查看自选页是否存在此股票
            res = optional.have_zx(name)
            assert res == False
        else:
            # 加自选
            gp.c_more_zx()
            # 进入自选页
            gp.back()
            tradehome.to_optional_page()
            # 查看自选页是否存在此股票
            res = optional.have_zx(name)
            assert res == True
    # 更多-加/减自选
    @pytest.mark.usefixtures('back_fixture')
    def test_zx4(self, setup_fixture):
        gp,tradehome,optional,common,changepwd = setup_fixture
        # 进入买入页
        gp.tipxj()
        # 输入代码，默认”000001“
        gp.input_contract()
        # 获取股票名称
        name = gp.title_text()
        # 查看当前股票是否已加自选，Ture：已加，False：未加
        res = gp.zx_state()
        if res == True:
            # 删自选
            gp.c_more_zx()
            # 进入自选页
            gp.back()
            tradehome.to_optional_page()
            # 查看自选页是否存在此股票
            res = optional.have_zx(name)
            assert res == False
        else:
            # 加自选
            gp.c_more_zx()
            # 进入自选页
            gp.back()
            tradehome.to_optional_page()
            # 查看自选页是否存在此股票
            res = optional.have_zx(name)
            assert res == True

    # 持仓-买入
    @pytest.mark.usefixtures('back_fixture')
    def test_hold_mr(self, setup_fixture):
        gp,tradehome,optional,common,changepwd = setup_fixture
        # 进入持仓页面
        gp.tipcc()
        # 持仓-买入
        res = gp.hold_mr()
        assert res == True
    # 持仓-卖出
    @pytest.mark.usefixtures('back_fixture')
    def test_hold_mc(self, setup_fixture):
        gp,tradehome,optional,common,changepwd = setup_fixture
        # 进入持仓页面
        gp.tipcc()
        # 持仓-卖出
        res = gp.hold_mc()
        assert res == True
    # 持仓-行情
    @pytest.mark.usefixtures('back_fixture')
    def test_hold_hq(self, setup_fixture):
        gp,tradehome,optional,common,changepwd = setup_fixture
        # 进入持仓页面
        gp.tipcc()
        # 持仓-行情
        res = gp.hold_hq()
        assert res == True

    # 撤单
    @pytest.mark.usefixtures('back_fixture')
    def test_cancle(self, setup_fixture):
        gp,tradehome,optional,common,changepwd = setup_fixture
        # 进入撤单页面
        gp.tipcd()
        # 撤单-买入
        res = gp.cancle()
        assert res == True

    # 查询-当日成交
    @pytest.mark.usefixtures('back_fixture')
    def test_today_cj(self, setup_fixture):
        gp,tradehome,optional,common,changepwd = setup_fixture
        # 进入查询页面
        gp.tipcx()
        # 查询-当日成交
        res = gp.cx_cj_today()
        assert res == True
    # 查询-当日委托
    @pytest.mark.usefixtures('back_fixture')
    def test_today_wt(self, setup_fixture):
        gp,tradehome,optional,common,changepwd = setup_fixture
        # 进入查询页面
        gp.tipcx()
        # 查询-当日委托
        res = gp.cx_wt_today()
        assert res == True
    # 查询-历史成交
    @pytest.mark.usefixtures('back_fixture')
    def test_history_cj(self, setup_fixture):
        gp,tradehome,optional,common,changepwd = setup_fixture
        # 进入查询页面
        gp.tipcx()
        # 查询-历史成交
        res = gp.cx_cj_history()
        assert res == True

    # 沪市非科创版股票（600000），价格类型包括限价、最优五档即时成交剩余撤销、最优五档即时成交剩余转限价。
    @pytest.mark.usefixtures('back_fixture')
    def test_hu(self,setup_fixture):
        gp,tradehome,optional,common,changepwd = setup_fixture
        arr = ['限价','最优五档即时成交剩余撤销','最优五档即时成交剩余转限价']
        # 进入限价页面
        gp.tipxj()
        # 点击买入
        gp.tipbuy()
        # 输入合约代码并带入价格,默认“000001”
        gp.input_contract("600000")
        # 获取价格类型数组
        arr1 = gp.price_type_arr()
        assert arr == arr1
    # 科创版股票（688001），价格类型包括限价、盘后定价、对手方最优价格、本方最优价格、最优五档即时成交剩余撤销、最优五档即时成交剩余转限价。
    @pytest.mark.usefixtures('back_fixture')
    def test_ke(self, setup_fixture):
        gp,tradehome,optional,common,changepwd = setup_fixture
        arr = ['限价','盘后定价' ,'对手方最优价格','本方最优价格','最优五档即时成交剩余撤销', '最优五档即时成交剩余转限价']
        # 进入限价页面
        gp.tipxj()
        # 点击买入
        gp.tipbuy()
        # 输入合约代码并带入价格,默认“000001”
        gp.input_contract("688001")
        # 获取价格类型数组
        arr1 = gp.price_type_arr()
        assert arr == arr1
    # 深市非创业版股票（000001），价格类型包括限价、对手方最优价格、本方最优价格、最优五档即时成交剩余撤销、即时成交剩余撤销（FAK）、全额成交或撤销委托（FOK）。
    @pytest.mark.usefixtures('back_fixture')
    def test_sheng(self, setup_fixture):
        gp,tradehome,optional,common,changepwd = setup_fixture
        arr = ['限价', '对手方最优价格', '本方最优价格', '最优五档即时成交剩余撤销', '即时成交剩余撤销(FAK)','全额成交或撤销委托(FOK)']
        # 进入限价页面
        gp.tipxj()
        # 点击买入
        gp.tipbuy()
        # 输入合约代码并带入价格,默认“000001”
        gp.input_contract("000001")
        # 获取价格类型数组
        arr1 = gp.price_type_arr()
        assert arr == arr1
    # 创业板股票（300001），价格类型包括限价、盘后定价、对手方最优价格、本方最优价格、最优五档即时成交剩余撤销、即时成交剩余撤销（FAK）、全额成交或撤销委托（FOK）。
    @pytest.mark.usefixtures('back_fixture')
    def test_chuang(self, setup_fixture):
        gp,tradehome,optional,common,changepwd = setup_fixture
        arr = ['限价','盘后定价', '对手方最优价格', '本方最优价格', '最优五档即时成交剩余撤销', '即时成交剩余撤销(FAK)', '全额成交或撤销委托(FOK)']
        # 进入限价页面
        gp.tipxj()
        # 点击买入
        gp.tipbuy()
        # 输入合约代码并带入价格,默认“000001”
        gp.input_contract("300001")
        # 获取价格类型数组
        arr1 = gp.price_type_arr()
        assert arr == arr1

    # 原密码为空格，提示”请输入原密码“
    @pytest.mark.usefixtures('back_fixture')
    def test_oldpwd_null(self,setup_fixture):
        gp,tradehome,optional,common,changepwd = setup_fixture
        tradehome.to_password()
        changepwd.change_pwd(" ","abcdefghijk","abcdefghijk")
        text = common.find_toast_text()
        assert text == "请输入原密码"
    # 原密码错误，提示”原密码输入错误“
    @pytest.mark.usefixtures('back_fixture')
    def test_oldpwd_error(self,setup_fixture):
        gp,tradehome,optional,common,changepwd = setup_fixture
        tradehome.to_password()
        changepwd.change_pwd("g","abcdefghijk","abcdefghijk")
        text = common.find_toast_text()
        assert text == "原密码输入错误"
    # 新密码为空格，提示”请输入新密码“
    @pytest.mark.usefixtures('back_fixture')
    def test_newpwd_null(self, setup_fixture, old_pwd):
        gp,tradehome,optional,common,changepwd = setup_fixture
        tradehome.to_password()
        changepwd.change_pwd(old_pwd, " ", "abcdefghijk")
        text = common.find_toast_text()
        assert text == "请输入新密码"
    # 确认密码为空格，提示”请输入确认密码“
    @pytest.mark.usefixtures('back_fixture')
    def test_confirmpwd_null(self, setup_fixture, old_pwd):
        gp,tradehome,optional,common,changepwd = setup_fixture
        tradehome.to_password()
        changepwd.change_pwd(old_pwd, "abcdefghijk", " ")
        text = common.find_toast_text()
        assert text == "请输入确认密码"
    # 确认密码与新密码不一致，提示”新密码与确认密码不一致,请重新输入“
    @pytest.mark.usefixtures('back_fixture')
    def test_confirmpwd_atypism(self, setup_fixture, old_pwd):
        gp,tradehome,optional,common,changepwd = setup_fixture
        tradehome.to_password()
        changepwd.change_pwd(old_pwd, "abcdefghijk", "abcdegghijk")
        tradehome.to_password()
        text = common.find_toast_text()
        assert text == "新密码与确认密码不一致,请重新输入"

    # 原密码为空格，提示”请输入原密码“
    @pytest.mark.usefixtures('back_fixture')
    def test_oldpwd_null_zj(self,setup_fixture):
        gp,tradehome,optional,common,changepwd = setup_fixture
        tradehome.to_password_zj()
        changepwd.change_pwd(" ","abcdefghijk","abcdefghijk")
        text = common.find_toast_text()
        assert text == "请输入原密码"
    # 原密码错误，提示”原密码输入错误“
    @pytest.mark.usefixtures('back_fixture')
    def test_oldpwd_error_zj(self,setup_fixture):
        gp,tradehome,optional,common,changepwd = setup_fixture
        tradehome.to_password_zj()
        changepwd.change_pwd("g","abcdefghijk","abcdefghijk")
        try:
            common.toastok()
        except:
            text = common.find_toast_text()
            assert text == "原密码输入错误"
    # 新密码为空格，提示”请输入新密码“
    @pytest.mark.usefixtures('back_fixture')
    def test_newpwd_null_zj(self, setup_fixture, old_pwd):
        gp,tradehome,optional,common,changepwd = setup_fixture
        tradehome.to_password_zj()
        changepwd.change_pwd(old_pwd, " ", "abcdefghijk")
        text = common.find_toast_text()
        assert text == "请输入新密码"
    # 确认密码为空格，提示”请输入确认密码“
    @pytest.mark.usefixtures('back_fixture')
    def test_confirmpwd_null_zj(self, setup_fixture, old_pwd):
        gp,tradehome,optional,common,changepwd = setup_fixture
        tradehome.to_password_zj()
        changepwd.change_pwd(old_pwd, "abcdefghijk", " ")
        text = common.find_toast_text()
        assert text == "请输入确认密码"
    # 确认密码与新密码不一致，提示”新密码与确认密码不一致,请重新输入“
    @pytest.mark.usefixtures('back_fixture')
    def test_confirmpwd_atypism_zj(self, setup_fixture, old_pwd):
        gp,tradehome,optional,common,changepwd = setup_fixture
        tradehome.to_password_zj()
        changepwd.change_pwd(old_pwd, "abcdefghijk", "abcdegghijk")
        text = common.find_toast_text()
        assert text == "新密码与确认密码不一致,请重新输入"