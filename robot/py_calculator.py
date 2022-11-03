#!python3
# -*- coding: utf-8 -*-

import uiautomation as auto
import os
import sys
import time
import subprocess


sys.path.append(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))


auto.uiautomation.DEBUG_EXIST_DISAPPEAR = True

auto.uiautomation.DEBUG_SEARCH_TIME = True
auto.uiautomation.TIME_OUT_SECOND = 10  # global time out


def Calc(window, btns, expression):
    expression = ''.join(expression.split())
    if not expression.endswith('='):
        expression += '='
    for char in expression:
        auto.Logger.Write(char, writeToFile=False)
        btns[char].Click(waitTime=0.05)
    time.sleep(0.1)
    window.SendKeys('{Ctrl}c', waitTime=0.1)
    result = auto.GetClipboardText()
    auto.Logger.WriteLine(result, auto.ConsoleColor.Cyan, writeToFile=False)
    time.sleep(1)

# 在win10中打开计算器
def CalcOnWindows10():
    """works on Windows 10.0.19042"""
    char2Id = {
        '0': 'num0Button',
        '1': 'num1Button',
        '2': 'num2Button',
        '3': 'num3Button',
        '4': 'num4Button',
        '5': 'num5Button',
        '6': 'num6Button',
        '7': 'num7Button',
        '8': 'num8Button',
        '9': 'num9Button',
        '.': 'decimalSeparatorButton',
        '+': 'plusButton',
        '-': 'minusButton',
        '*': 'multiplyButton',
        '/': 'divideButton',
        '=': 'equalButton',
        '(': 'openParenthesisButton',
        ')': 'closeParenthesisButton',
    }
    # Desc一般不做为搜索项使用
    calcWindow = auto.WindowControl(searchDepth=1, ClassName='ApplicationFrameWindow',
                                    Compare=lambda c, d: c.Name == 'Calculator' or c.Name == '计算器', Desc='Calculator Window')
    if not calcWindow.Exists(0, 0):
        subprocess.Popen('calc')
    calcWindow.SetActive()
    calcWindow.ButtonControl(AutomationId='TogglePaneButton').Click()
    calcWindow.ListItemControl(AutomationId='Scientific').Click()
    calcWindow.ButtonControl(AutomationId='clearButton').Click()
    if 0:
        char2Button = {key: calcWindow.ButtonControl(
            AutomationId=char2Id[key], Desc='Button ' + key) for key in char2Id}
    else:
        
        id2char = {v: k for k, v in char2Id.items()}
        char2Button = {}
        for c, d in auto.WalkControl(calcWindow):
            if c.AutomationId in id2char:
                char2Button[id2char[c.AutomationId]] = c
    Calc(calcWindow, char2Button, '1234 * (4 + 5 + 6) - 78 / 90.8')
    Calc(calcWindow, char2Button, '3*3+4*4')
    Calc(calcWindow, char2Button, '2*3.14159*10')
    # on windows 10, 7 pixels of windows border are transparent
    calcWindow.CaptureToImage('calc.png', 7, 0, -14, -7)
    calcWindow.Disappears(1)
    calcWindow.GetWindowPattern().Close()
    calcWindow.Exists(1)


if __name__ == '__main__':
    CalcOnWindows10()
    auto.Logger.Write('\nPress any key to exit', auto.ConsoleColor.Cyan)
    import msvcrt
    while not msvcrt.kbhit():
        time.sleep(0.05)
