import  logging
from common.read_config import conf
from  common.get_path import LOG_DIR
import  os
'''
为了避免程序中创建多个日志收集器而导致日志重复记录
那么我们可以只创建一个日志收集器，别的模块的使用时都导入这个日志收集器
'''
def create_log(name,level = 'DEBUG',filename= 'log',sh_level = 'DEBUG',fh_level='DEBUG'):
# 一、 创建日志收集器
    log = logging.getLogger(name)
# 二、设置日志收集日志的等级
    log.setLevel(level)
# 三、设置日志输出渠道
 # 3.1输出到文件
    fh = logging.FileHandler(filename,encoding = "utf-8")
    fh.setLevel(fh.level)
    log.addHandler(fh)
     # 3.2输出到控制台
    sh = logging.StreamHandler()
    sh.setLevel(sh_level)
    log.addHandler(sh)

    # 四、日志输出的等级   括号内的东西是输入是对应的时间、文件名等，可查看代码添加以%（）s格式
    log_format = logging.Formatter('%(asctime)s %(name)s %(levelname)s %(filename)s-%(lineno)d line：%(message)s')
    # 设置输出到控制台的日志格式
    sh.setFormatter(log_format)
    # 设置输出到文件的日志格式
    fh.setFormatter(log_format)
    return  log

my_log = create_log(
    name = conf.get("logging",'name'),
    level = conf.get("logging",'level'),
    filename = os.path.join(LOG_DIR,conf.get("logging",'filename')),
    sh_level = conf.get("logging",'sh_level'),
    fh_level = conf.get("logging",'fh_level'),
    )