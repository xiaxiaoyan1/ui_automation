__author__ = 'Administrator'
import pytest,time,datetime
from businessPage.first_page import First
from businessPage.qq_target_page import qq_target
from businessPage.login_page import Login
from businessPage.gp_new_page import Gp
from common.desired_caps import app_desired
from common.common_fun import Common
from common.collector_log import my_log
from common.get_path import BASE_DIR
from common.read_config import get_appPackage
from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

#启动app前置，测试过程中只启动一次app
# @pytest.fixture(scope="function",autouse="False")
# def back_fixture(driver_fixture):
#     yield
#     driver=driver_fixture
#     com=Common(driver)
#     com.back("返回首页")
#     return driver

@pytest.fixture(scope='session')
def driver_fixture():
    driver=app_desired()
    yield driver

@pytest.fixture(scope='session',autouse=False)
def login_fixture(driver_fixture):
    csv_file=BASE_DIR + '\datas\login.csv'
    print("csv_file:%s"%csv_file)
    driver=driver_fixture
    com=Common(driver)
    data=com.get_csv_data(csv_file,1)
    time.sleep(2)
    trd=First(driver)
    trd.to_login()
    logn=Login(driver)
    logn.login(data[0],data[1])

@pytest.fixture(scope='session',autouse=False)
def gp_login_fixture(driver_fixture):
    csv_file=BASE_DIR + '\datas\login.csv'
    print("csv_file:%s"%csv_file)
    driver=driver_fixture
    com=Common(driver)
    data=com.get_csv_data(csv_file,2)
    time.sleep(2)
    trd=First(driver)
    trd.to_login()
    logn=Login(driver)
    logn.gp_login(data[0],data[1])
@pytest.fixture(scope='class',autouse=False)
def gp_teardown_fixture(driver_fixture):
    yield
    driver = driver_fixture
    gp = Gp(driver)
    gp.tipQq()
@pytest.fixture(scope='session')
def old_pwd(driver_fixture):
    csv_file=BASE_DIR + '\datas\login.csv'
    com = Common(driver_fixture)
    data = com.get_csv_data(csv_file, 1)
    yield data[1]

@pytest.fixture(scope='function',autouse=False)
def back_fixture(driver_fixture):
    yield
    print("后置开始执行")
    driver=driver_fixture
    com=Common(driver)
    com.back()

#@pytest.fixture(scope='function',autouse=False)
# def back_fixture(driver_fixture):
#     yield
#     print("后置开始执行")
#     my_log.info("后置开始执行")
#     driver=driver_fixture
#     appPackage = get_appPackage()
#     for i in range(10):
#         dt = datetime.datetime.now().strftime('%Y-%m-%d %H:%M:%S')
#         print("时间：%s后置开始循环第：%s次"%(dt,i))
#         try:
#             # 为什么找不到元素总是最少要等待10秒？
#             print("时间：%s后置开始循环第：%s次,开始找首页元素" % (datetime.datetime.now().strftime('%Y-%m-%d %H:%M:%S'), i))
#             # WebDriverWait(driver, 1).until(EC.visibility_of_element_located((By.XPATH,"//android.widget.RadioButton[@text='首页']")))
#             time.sleep(1)
#             driver.find_element_by_xpath("//android.widget.RadioButton[@text='首页']")
#             print("时间：%s后置开始循环第：%s次,结束找首页元素" % (datetime.datetime.now().strftime('%Y-%m-%d %H:%M:%S'), i))
#         except:
#             try:
#                 print("时间：%s后置开始循环第：%s次,开始找tv_back元素" % (datetime.datetime.now().strftime('%Y-%m-%d %H:%M:%S'), i))
#                 # el = WebDriverWait(driver, 1).until(
#                 #     EC.visibility_of_element_located((By.ID, appPackage + ":id/tv_back")))
#                 time.sleep(1)
#                 el = driver.find_element(By.ID, appPackage + ":id/tv_back")
#                 el.click()
#                 print("时间：%s后置开始循环第：%s次,结束找tv_back元素" % (datetime.datetime.now().strftime('%Y-%m-%d %H:%M:%S'), i))
#             except:
#                 try:
#                     print("时间：%s后置开始循环第：%s次,开始找iv_back元素" % (datetime.datetime.now().strftime('%Y-%m-%d %H:%M:%S'), i))
#                     el = WebDriverWait(driver, 1).until(
#                         EC.visibility_of_element_located((By.ID, appPackage + ":id/iv_back")))
#                     el.click()
#                     print("时间：%s后置开始循环第：%s次,结束找iv_back元素" % (datetime.datetime.now().strftime('%Y-%m-%d %H:%M:%S'), i))
#                 except:
#                     try:
#                         el = WebDriverWait(driver, 1).until(EC.visibility_of_element_located((By.ID, appPackage+":id/btn_toast_ok")))
#                         el.click()
#                     except:
#                         try:
#                             el = WebDriverWait(driver, 1).until(EC.visibility_of_element_located((By.ID, appPackage+":id/btn_confirm")))
#                             el.click()
#                         except:
#                             try:
#                                 el = WebDriverWait(driver, 1).until(
#                                     EC.visibility_of_element_located((By.XPATH, "//*[@text='确定']")))
#                                 el.click()
#                             except:
#                                 try:
#                                     el = WebDriverWait(driver, 1).until(
#                                         EC.visibility_of_element_located((By.XPATH, "//*[@text='确认']")))
#                                     el.click()
#                                 except Exception:
#                                     pass
#         else:
#             break










