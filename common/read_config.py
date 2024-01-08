from configparser import ConfigParser
from common.get_path import CONF_DIR,BASE_DIR
import os,yaml
class Config(ConfigParser):
    '''
    在创建对象时，直接加载配置文件中的内容
    '''
    def __init__(self,conf_file):
        super().__init__()
        '''继承'''
        self.read(conf_file,encoding="utf-8")
conf = Config(os.path.join(CONF_DIR,"log_config.ini"))

def get_appPackage():
    Dir = BASE_DIR + '\config\caps.yaml'
    with open(Dir, 'r', encoding='gb18030', errors='ignore') as file:
        data = yaml.load(file, Loader=yaml.FullLoader)
    return data['appPackage1']

