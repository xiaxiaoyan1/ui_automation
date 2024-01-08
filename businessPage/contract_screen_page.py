import time
from appium.webdriver.common.mobileby import MobileBy

from common.collector_log import my_log
from common.common_fun import Common
from common.read_config import get_appPackage
#首页
class Screen(Common):
    appPackage = get_appPackage()
    # 筛选页
    sx = (MobileBy.ID,appPackage+":id/iv_sx")
    search = (MobileBy.ID,appPackage+":id/iv_refresh")
    showSx = (MobileBy.ID, appPackage+":id/tv_showSx")
    new_price = (MobileBy.XPATH, "//android.widget.HorizontalScrollView/android.widget.LinearLayout[1]/android.widget.LinearLayout[1]")
    rise = (MobileBy.XPATH, "//android.widget.LinearLayout/android.widget.LinearLayout[2]")
    rise_rate = (MobileBy.XPATH, "//android.widget.LinearLayout/android.widget.LinearLayout[3]")
    count = (MobileBy.XPATH, "//android.widget.LinearLayout/android.widget.LinearLayout[4]")
    item = "//android.widget.FrameLayout[1]/android.widget.LinearLayout[1]/android.widget.FrameLayout[1]/android.widget.LinearLayout[1]/android.widget.ListView[1]/android.widget.LinearLayout[1]/android.widget.TextView[1]"
    # 筛选条件页
    market = (MobileBy.ID, appPackage+":id/tv_market")
    stock = (MobileBy.ID, appPackage+":id/tv_stock")
    tp = appPackage+":id/type_1"  # 类型
    tm = appPackage+":id/date_1"  # 时间
    vl = appPackage+":id/xsd_1"  # 值
    at = appPackage+":id/hyd_1"  # 活跃度
    save = (MobileBy.ID, appPackage+":id/iv_save")
    btn_ok = (MobileBy.ID, appPackage+":id/btn_ok")  # 执行
    btnOk = (MobileBy.ID, appPackage+":id/btnOk")  # 确认
    # 搜索页
    edt_search = (MobileBy.ID, appPackage+":id/edt_search")
    search_item = (MobileBy.ID, appPackage+":id/name")
    btn_operator = (MobileBy.ID, appPackage+":id/btn_operator")
    day_K = (MobileBy.ID, appPackage+":id/radiobtn_2")
    item_name = (MobileBy.ID, appPackage+":id/code")

    def search_toK(self):
        self.input_send_keys(self.edt_search,"000001","输入代码搜索框")
        self.get_clickable_element(self.search_item,"点击item")
        try:
            self.get_visible_element(self.day_K,"日K")
        except Exception:
            my_log.error("没有进入K线页")
            self.error_save_screenshot("没有进入K线页")
            return False
        else:
            return True
    def screen_toK(self):
        self.get_clickable_element((MobileBy.XPATH,self.item),"点击item")
        try:
            self.get_visible_element(self.day_K,"日K")
        except Exception:
            my_log.error("没有进入K线页")
            self.error_save_screenshot("没有进入K线页")
            return False
        else:
            return True
    # 获取M行N列的数据
    def get_num(self,M,N):
        item_path = "//android.widget.FrameLayout[1]/android.widget.LinearLayout[1]/android.widget.FrameLayout[1]/android.widget.LinearLayout[1]/android.widget.ListView[1]/android.widget.LinearLayout[%s]/android.widget.HorizontalScrollView[1]/android.widget.LinearLayout[1]/android.widget.TextView[%s]" %(M+1,N)
        item = (MobileBy.XPATH, item_path)
        num = self.get_element_text(item,"%s行%s列的数据"%(M,N))
        return float(num)
    def c_search(self):
        self.get_clickable_element(self.search,"搜索")
    def c_input(self,code="000"):
        self.input_send_keys(self.edt_search, code, "输入代码")
        time.sleep(1)
    # 加自选并获取名称，返回列表
    def addself_list(self):
        arr = []
        for i in range(5):
            btn_addself = (MobileBy.XPATH,
                           "//android.widget.LinearLayout[@resource-id='" + self.appPackage + ":id/lv_item']/android.widget.RelativeLayout[%s]/android.widget.ImageButton[1]" %(i+1))
            text_addself = (MobileBy.XPATH,
                            "//android.widget.FrameLayout[1]/android.widget.LinearLayout[1]/android.widget.FrameLayout[1]/android.widget.RelativeLayout[1]/android.widget.FrameLayout[2]/android.widget.ScrollView[1]/android.widget.LinearLayout[1]/android.widget.LinearLayout[1]/android.widget.RelativeLayout[%s]/android.widget.TextView[1]" %(i+1))
            try:
                self.get_clickable_element(btn_addself,"加自选按钮")
                arr.append(self.get_element_text(text_addself, "自选名称"))
            except:
                my_log.info("搜索出的自选不够")
                self.error_save_screenshot("自选搜索列表")
                break
        return arr
    def c_new_price(self):
        self.get_clickable_element(self.new_price, "最新")
    def c_rise(self):
        self.get_clickable_element(self.rise, "涨跌")
    def c_rise_rate(self):
        self.get_clickable_element(self.rise_rate, "涨跌幅")
    def c_count(self):
        self.get_clickable_element(self.count, "总量")
    def c_item(self):
        text = self.get_element_text((MobileBy.XPATH,self.item),"item")
        self.get_clickable_element((MobileBy.XPATH,self.item), "item")
        return text
    def sx_text(self):
        return self.get_element_text(self.showSx,"筛选组合text")
    def to_sx(self):
        self.get_clickable_element(self.sx, "筛选")
    def c_save(self):
        self.get_clickable_element(self.save,"保存点击")
    def c_btn_ok(self):
        self.get_clickable_element(self.btn_ok,"执行")
    # 筛选条件默认认购、当月、深实值、非常活跃、上证50ETF。stock传1是“深圳100ETF易方达”
    def c_sx(self, type=1, data=1, xsd=1, hyd=1, stock=0):
        arr = [["全部", "认购", "认沽"], ["全部", "当月", "下月", "下季", "隔季"], ["全部", "深实值", "中实值", "浅实值", "浅虚值", "中虚值", "深虚值"],
               ["全部", "非常活跃", "较活跃", "不活跃"]]
        market = ["上证50ETF", "深证100ETF易方达"]
        show_sx = ''
        if stock == 0:
            show_sx = market[0] + "+" + arr[0][type] + "+" + arr[1][data] + "+" + arr[2][xsd] + "+" + arr[3][hyd]
            self.get_clickable_element(self.market,"市场")
            self.swipeup(0.9, 0.99)
            self.get_clickable_element(self.btnOk,"确认")
            self.get_clickable_element(self.stock,"标的")
            self.swipeup(0.9, 0.99)
            self.get_clickable_element(self.btnOk, "确认")
        else:
            show_sx = market[1] + "+" + arr[0][type] + "+" + arr[1][data] + "+" + arr[2][xsd] + "+" + arr[3][hyd]
            self.get_clickable_element(self.market, "市场")
            self.swipeup(0.99, 0.9)
            self.get_clickable_element(self.btnOk, "确认")
            self.get_clickable_element(self.stock, "标的")
            self.swipeup(0.9, 0.99)
            self.get_clickable_element(self.btnOk, "确认")
        type += 1
        data += 1
        xsd += 1
        hyd += 1
        xpath1 = self.tp.replace('1', str(type))
        xpath2 = self.tm.replace('1', str(data))
        xpath3 = self.vl.replace('1', str(xsd))
        xpath4 = self.at.replace('1', str(hyd))
        self.get_clickable_element((MobileBy.ID, xpath1),"类型")
        self.get_clickable_element((MobileBy.ID, xpath2),"时间")
        self.get_clickable_element((MobileBy.ID, xpath3), "值")
        self.get_clickable_element((MobileBy.ID, xpath4), "活跃度")
        self.get_clickable_element(self.btn_ok,"执行")
        return show_sx
    # 降序判断,第N列数据，N>=0
    def desc(self,N):
        time.sleep(3)
        arr = []
        res = False
        for i in range(4):
            arr.append(self.get_num(i, N))
        for i in range(3):
            if arr[i] >= arr[i + 1]:
                res = True
            else:
                my_log.error("此顺序非降序")
                self.error_save_screenshot("此顺序非降序")
                res = False
                break
        print(arr)
        return res
    # 升序判断，第N列数据，N>=0
    def asc(self,N):
        time.sleep(10)
        arr = []
        res = False
        for i in range(4):
            arr.append(self.get_num(i, N))
        for i in range(3):
            if arr[i] <= arr[i + 1]:
                res = True
            else:
                my_log.error("此顺序非升序")
                self.error_save_screenshot("此顺序非升序")
                res = False
                break
        print(arr)
        return res
    # 乱序判断，第N列数据，N>=0
    def no_asc(self,N):
        time.sleep(3)
        arr = []
        res = False
        for i in range(4):
            arr.append(self.get_num(i, N))
        for i in range(3):
            if arr[i] <= arr[i + 1]:
                res = True
            else:
                my_log.info("此顺序为乱序")
                res = False
                break
        print(arr)
        return res