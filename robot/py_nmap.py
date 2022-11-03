# -*- coding: utf-8 -*-
import time
import uiautomation as uiauto

from win10toast import ToastNotifier

# 获取参数
args = '192.168.33.1'

# 获取desktop
desktop = uiauto.GetRootControl()
time.sleep(1)

# 发送hotkey——win+r
uiauto.SendKeys('{Win}r')

# 获取‘运行’窗口
run_win = desktop.WindowControl(Name='运行')

# 获取运行窗口的输入条
cmd = run_win.EditControl(Name='打开(O):')
# 键入cmd回车
cmd.SendKeys(r'cmd{Enter}')

# 获取命令行窗口
cmd_win = uiauto.WindowControl(ClassName='ConsoleWindowClass')

# 获取命令行窗口的输入框
text_area = cmd_win.DocumentControl(Name='Text Area')

# 键入cmd命令
text_area.SendKeys('nmap '+args + r'{Enter}')

# 弹出提示窗口
toaster = ToastNotifier()
toaster.show_toast(title="软件机器人操作提示", msg="机器人程序运行结束后，在命令行窗口中查看运行结果.....")
