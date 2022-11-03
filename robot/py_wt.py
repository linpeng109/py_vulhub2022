# -*- coding: utf-8 -*-
import time
import sys
import uiautomation as uiauto

from win10toast import ToastNotifier

# 获取命令行参数
# args = sys.argv
# if(len(args) > 1):
#     print('arguments: %s' % args)

# 获取desktop
desktop = uiauto.GetRootControl()
time.sleep(0.5)

# 发送hotkey——win+r
uiauto.SendKeys('{Win}r')

# 获取‘运行’窗口
run_win = desktop.WindowControl(Name='运行')

# 获取运行窗口的输入条
wt = run_win.EditControl(Name='打开(O):')
# 键入cmd回车
wt.SendKeys(r'wt{Enter}')

# 获取命令行窗口
wt_win = uiauto.WindowControl(ClassName='CASCADIA_HOSTING_WINDOW_CLASS')

# 获取命令行窗口的输入框
text_area = wt_win.TextControl(clasName='TermControl')

# 键入nmap命令
text_area.SendKeys('nmap '+r'{Enter}')

# 弹出提示窗口
toaster = ToastNotifier()
toaster.show_toast(title="软件机器人操作提示", msg="机器人程序运行结束后，在命令行窗口中查看运行结果.....")
