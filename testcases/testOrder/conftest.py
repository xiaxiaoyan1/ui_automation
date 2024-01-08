__author__ = 'Administrator'
import pytest
from businessPage.first_page import First
from businessPage.qq_target_page import qq_target
from businessPage.login_page import Login
from common.desired_caps import app_desired
from common.common_fun import Common
@pytest.fixture(scope='function',autouse=False)
def order_fixture(driver_fixture):
    yield
    print("后置开始执行")
    driver=driver_fixture
    com=Common(driver)
    com.toastok()
    com.back()

@pytest.fixture(scope='function',autouse=False)
def other_fixture(driver_fixture):
    yield
    print("后置开始执行")
    driver=driver_fixture
    com=Common(driver)
    com.back()














