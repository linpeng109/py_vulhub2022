# -*- coding: utf-8 -*-
import subprocess
import time

from uiautomation import uiautomation as uiauto
from win10toast import ToastNotifier

from py_config import ConfigFactory
from py_logging import LoggerFactory


# 配置初始化
config = ConfigFactory(config_file='py_clipboard.ini').get_config()
logger = LoggerFactory(config_factory=config).get_logger()

# 启动putty
putty_executer = config.get('robots', 'putty_executer')
pid = subprocess.Popen(putty_executer).pid

# 获取putty窗口
putty_window = uiauto.WindowControl(Name=r'PuTTY Configuration')

time.sleep(1)
# 写入目标ip
ip_edit = putty_window.EditControl(Name='Host Name (or IP address)')

# ip = '192.168.1.1'
ip_edit.SendKeys(ip)
time.sleep(3)

# 弹出提示窗口
toaster = ToastNotifier()
toaster.show_toast(title="软件机器人操作提示", msg="机器人程序运行结束后，在命令行窗口中查看运行结果.....")
