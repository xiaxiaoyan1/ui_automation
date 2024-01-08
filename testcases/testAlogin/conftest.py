__author__ = 'Administrator'
import pytest
from businessPage.first_page import First
from businessPage.qq_target_page import qq_target
from businessPage.login_page import Login
from common.desired_caps import app_desired

#启动app前置，测试过程中只启动一次app
# @pytest.fixture(scope="function",autouse="False")
# def back_fixture(driver_fixture):
#     yield
#     driver=driver_fixture
#     com=Common(driver)
#     com.back("返回首页")
#     return driver
#
@pytest.fixture(scope='function',autouse=False)
def exit_fixture(driver_fixture):
#     driver=app_desired()
    yield
    print("后置开始执行")
    driver=driver_fixture
    login=Login(driver)
    login.unLogin()
















