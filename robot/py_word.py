import subprocess
import time

import uiautomation as uiauto


# 启动word应用
subprocess.Popen(r'C:/Program Files/Microsoft Office/Office16/WINWORD.EXE')
print("subprocess.popen")

# 获取桌面
desktop = uiauto.GetRootControl()
print(desktop)

# 获取窗口
word_window = desktop.WindowControl(ClassName='OpusApp', searchDepth=1)
print(word_window)

# 启动界面处理
new_link = word_window.HyperlinkControl(AutomationId='AIOStartDocument', Name='空白文档')
print(new_link)
new_link.Click(simulateMove=True)
time.sleep(1)

# 选择字体
font_type_control = word_window.ButtonControl(
    ClassName='NetUIStickyButton', Name='打开', foundIndex=1)
font_type_control.Click(simulateMove=False)
font_type = word_window.ListItemControl(
    ClassName='NetUIGalleryButton', Name='宋体')
font_type.Click()

# 选择字号
font_size_control = word_window.ButtonControl(
    ClassName='NetUIStickyButton', Name='打开', foundIndex=2)
font_size_control.Click(simulateMove=False)
font_size = word_window.ListItemControl(
    ClassName='NetUIGalleryButton', Name='二号')
font_size.Click()

# 选择输入页面
edit_space = word_window.EditControl(
    AutomationId='UIA_AutomationId_Word_Content_Page_1')
edit_space.SendKeys(
    r'所谓“软件机器人”（RPA）实际上是一类应用程序的统称，即通过一段程序代码，完全以拟人的方式操控键盘鼠标，通过软件'+
    r'交互界面（CS构架）或web浏览器界面（BS构架的），完成数据输入或采集，从而实现对另一个软件或系统的控制')
