# -*- coding: utf-8 -*-
import time
import uiautomation as uiauto

from win10toast import ToastNotifier


# 获取desktop
desktop = uiauto.GetRootControl()
time.sleep(0.5)

# 发送hotkey——win+r
uiauto.SendKeys('{Win}r')

# 获取‘运行’窗口
run_win = desktop.WindowControl(Name='运行')

# 获取运行窗口的输入条
cmd = run_win.EditControl(Name='打开(O):')

# 键入mstsc回车
cmd.SendKeys(r'mstsc{Enter}')

# 获取远程桌面窗口
mstsc_win = uiauto.WindowControl(ClassName='#32770')

# 获取远程桌面窗口的输入框
options_button = mstsc_win.ButtonControl(Name='显示选项(O)')

# 单击显示选项按钮
options_button.Click(simulateMove=False)

# 输入远程主机ip地址
host_edit = mstsc_win.EditControl(Name=r'计算机(C):')
host_edit.SendKeys(host+r'')

# 输入用户名
username_edit = mstsc_win.EditControl(Name=r'用户名:', ClassName=r'Edit')
username_edit.SendKeys(username+r'')

# 单击链接按钮
connect_button = mstsc_win.ButtonControl(Name='连接(N)')
connect_button.Click(simulateMove=False)

# 弹出提示窗口
toaster = ToastNotifier()
toaster.show_toast(title="软件机器人操作提示", msg="机器人程序运行结束后，在命令行窗口中查看运行结果.....")
