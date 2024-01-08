from businessPage.change_password_page import ChangePwd
from businessPage.trade_first_page import TradeFirst
from common.common_fun import Common

import pytest
#修改交易密码测试用例，为防止密码被修改，以下用例均为异常用例
@pytest.mark.usefixtures('login_fixture')
@pytest.mark.usefixtures('driver_fixture')
@pytest.mark.usefixtures('old_pwd')
class TestChangePassword():
    @pytest.fixture(scope='function', autouse=False)
    def setup_fixture(self, driver_fixture):
        driver = driver_fixture
        tradehome = TradeFirst(driver)
        changepwd = ChangePwd(driver)
        common = Common(driver)
        tradehome.to_trade_page()

        return changepwd,common,tradehome
    # 原密码为空格，提示”请输入原密码“
    @pytest.mark.usefixtures('back_fixture')
    def test_oldpwd_null(self,setup_fixture):
        changepwd,common,tradehome = setup_fixture
        tradehome.to_password()
        changepwd.change_pwd(" ","abcdefghijk","abcdefghijk")
        text = common.find_toast_text()
        assert text == "请输入原密码"
    # 原密码错误，提示”原密码输入错误“
    @pytest.mark.usefixtures('back_fixture')
    def test_oldpwd_error(self,setup_fixture):
        changepwd,common,tradehome = setup_fixture
        tradehome.to_password()
        changepwd.change_pwd("g","abcdefghijk","abcdefghijk")
        text = common.find_toast_text()
        assert text == "原密码输入错误"
    # 新密码为空格，提示”请输入新密码“
    @pytest.mark.usefixtures('back_fixture')
    def test_newpwd_null(self, setup_fixture, old_pwd):
        changepwd,common,tradehome = setup_fixture
        tradehome.to_password()
        changepwd.change_pwd(old_pwd, " ", "abcdefghijk")
        text = common.find_toast_text()
        assert text == "请输入新密码"
    # 确认密码为空格，提示”请输入确认密码“
    @pytest.mark.usefixtures('back_fixture')
    def test_confirmpwd_null(self, setup_fixture, old_pwd):
        changepwd,common,tradehome = setup_fixture
        tradehome.to_password()
        changepwd.change_pwd(old_pwd, "abcdefghijk", " ")
        text = common.find_toast_text()
        assert text == "请输入确认密码"
    # 确认密码与新密码不一致，提示”新密码与确认密码不一致,请重新输入“
    @pytest.mark.usefixtures('back_fixture')
    def test_confirmpwd_null(self, setup_fixture, old_pwd):
        changepwd,common,tradehome = setup_fixture
        tradehome.to_password()
        changepwd.change_pwd(old_pwd, "abcdefghijk", "abcdegghijk")
        text = common.find_toast_text()
        assert text == "新密码与确认密码不一致,请重新输入"

    # 原密码为空格，提示”请输入原密码“
    @pytest.mark.usefixtures('back_fixture')
    def test_oldpwd_null_zj(self,setup_fixture):
        changepwd,common,tradehome = setup_fixture
        tradehome.to_password_zj()
        changepwd.change_pwd(" ","abcdefghijk","abcdefghijk")
        text = common.find_toast_text()
        assert text == "请输入原密码"
    # 原密码错误，提示”原密码输入错误“
    @pytest.mark.usefixtures('back_fixture')
    def test_oldpwd_error_zj(self,setup_fixture):
        changepwd,common,tradehome = setup_fixture
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
        changepwd,common,tradehome = setup_fixture
        tradehome.to_password_zj()
        changepwd.change_pwd(old_pwd, " ", "abcdefghijk")
        text = common.find_toast_text()
        assert text == "请输入新密码"
    # 确认密码为空格，提示”请输入确认密码“
    @pytest.mark.usefixtures('back_fixture')
    def test_confirmpwd_null_zj(self, setup_fixture, old_pwd):
        changepwd,common,tradehome = setup_fixture
        tradehome.to_password_zj()
        changepwd.change_pwd(old_pwd, "abcdefghijk", " ")
        text = common.find_toast_text()
        assert text == "请输入确认密码"
    # 确认密码与新密码不一致，提示”新密码与确认密码不一致,请重新输入“
    @pytest.mark.usefixtures('back_fixture')
    def test_confirmpwd_null_zj(self, setup_fixture, old_pwd):
        changepwd,common,tradehome = setup_fixture
        tradehome.to_password_zj()
        changepwd.change_pwd(old_pwd, "abcdefghijk", "abcdegghijk")
        text = common.find_toast_text()
        assert text == "新密码与确认密码不一致,请重新输入"

