__author__ = 'Administrator'
import pytest
from businessPage.first_page import First
from businessPage.qq_target_page import qq_target
from businessPage.login_page import Login
from common.desired_caps import app_desired
from common.common_fun import Common
@pytest.fixture(scope='function',autouse=False)
def position_back_fixture(driver_fixture):
    yield
    print("后置开始执行")
    driver=driver_fixture
    com=Common(driver)
    com.back()
    com.back()

@pytest.fixture(scope='function',autouse=False)
def position_hqback_fixture(driver_fixture):
    yield
    print("后置开始执行")
    driver=driver_fixture
    com=Common(driver)
    com.hq_back()
    com.back()














