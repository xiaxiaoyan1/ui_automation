__author__ = 'Administrator'
from businessPage.login_page import Login
from common.common_fun import Common
from businessPage.first_page import First
import pytest
import time

# @pytest.fixture(scope="function",autouse=False)
# def back_fixture(driver_fixture):
#     yield
#     driver=driver_fixture
#     com=Common(driver)
#     com.back("返回首页")
#     return driver

@pytest.mark.usefixtures('driver_fixture')
class TestLogin():
    csv_file='D://qqbproject//datas//login.csv'
    @pytest.mark.usefixtures('exit_fixture')
    def test_LoginTrue(self,driver_fixture):
        print("开始执行测试用例")
        self.driver=driver_fixture
        com=Common(self.driver)
        data=com.get_csv_data(self.csv_file,1)
        time.sleep(5)
        trd=First(self.driver)
        trd.to_login()
        logn=Login(self.driver)
        lon=logn.login(data[0],data[1])
        assert lon==True


    # def test_LoginFalse(self,driver_fixture):
    #     self.driver=driver_fixture
    #     unlogn=Login(self.driver)
    #     unlogn.unLogin()
    #     trd=First(self.driver)
    #     trd.to_login()
    #     com=Common(self.driver)
    #     data=com.get_csv_data(self.csv_file,2)
    #     unlogn=unlogn.login(data[0],data[1])
    #     com.back("返回首页")
    #     assert unlogn==True





