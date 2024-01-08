# __author__ = 'Administrator'
# import pytest
# from businessPage.first_page import First
# from businessPage.qq_target_page import qq_target
# from businessPage.login_page import Login
# from common.desired_caps import app_desired
# from common.common_fun import Common
# import time
#
# #启动app前置，测试过程中只启动一次app
# # @pytest.fixture(scope="function",autouse="False")
# # def back_fixture(driver_fixture):
# #     yield
# #     driver=driver_fixture
# #     com=Common(driver)
# #     com.back("返回首页")
# #     return driver
# #
# @pytest.fixture(scope='function',autouse=False)
# def login_fixture(driver_fixture):
#     csv_file='D://q//pycharm2//qqbproject(1)//datas//login.csv'
#     driver=driver_fixture
#     com=Common(driver)
#     data=com.get_csv_data(csv_file,1)
#     time.sleep(5)
#     trd=First(driver)
#     trd.to_login()
#     logn=Login(driver)
#     logn.login(data[0],data[1])
#     yield
#     print("后置开始执行")
#     com.back()
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
