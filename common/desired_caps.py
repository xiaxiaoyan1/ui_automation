__author__ = 'Administrator'
from appium import webdriver
from common.collector_log import my_log
import yaml,time
from selenium.common.exceptions import NoSuchElementException
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from time import sleep
from appium.webdriver.common.mobileby import MobileBy
from common.get_path import BASE_DIR
from common.read_config import get_appPackage
def app_desired():
    appPackage = get_appPackage()
    Dir = BASE_DIR + '\config\caps.yaml'
    with open(Dir,'r',encoding='gb18030',errors='ignore') as file:
            data=yaml.load(file,Loader=yaml.FullLoader)
    desired_caps={}
    desired_caps['platformName']=data['platformName']
    desired_caps['platformVersion']=data['platformVersion']
    desired_caps['deviceName']=data['deviceName']
    desired_caps['app']=BASE_DIR+data['app']
    desired_caps['appPackage']=data['appPackage']
    desired_caps['appACtivity']=data['appACtivity']
    desired_caps['noReset']=data['noReset']
    my_log.info("开始启动app")
    print(desired_caps['app'])
    driver=webdriver.Remote('http://'+str(data['ip'])+':'+str(data['port'])+'/wd/hub',desired_caps)
    driver.implicitly_wait(10)
    time.sleep(2)
    my_log.info("隐私协议第一个复选框")
    try:
        el1 = driver.find_elements_by_class_name("android.widget.CheckBox")[0]
    except IndexError:
        my_log.error("没有第一个复选框")
    else:
        el1.click()

    time.sleep(2)
    my_log.info("隐私协议第二个复选框")
    try:
        el2 = driver.find_elements_by_class_name("android.widget.CheckBox")[1]
    except IndexError:
        my_log.error("没有第二个复选框")
    else:
        el2.click()

    time.sleep(2)
    my_log.info("隐私协议确认")
    try:
        el3 = driver.find_element_by_id(appPackage+":id/btn_confirm")
    except NoSuchElementException:
        my_log.error("没有隐私协议确认按钮")
    else:
        el3.click()

    time.sleep(2)
    try:
        el4 = driver.find_element_by_id(appPackage + ":id/message")
        my_log.info("更新")
        if "更新" in el4.text or "升级" in el4.text:
            el5 = driver.find_element_by_id(appPackage + ":id/negativeButton")
            el5.click()
    except:
        my_log.info("没有更新弹框")

    time.sleep(2)
    my_log.info("首页弹框")
    try:
        time.sleep(3)
        el4=driver.find_element_by_id(appPackage+":id/btn_toast_ok")
    except NoSuchElementException:
        my_log.info("没有首页确认弹框")
    else:
        my_log.info("点击首页确认弹框")
        el4.click()

    return driver
if __name__ == '__main__':
    app_desired()