import time

import win32api
import win32gui, win32ui, win32con

def setsize():
    # 获取后台窗口的句柄，注意后台窗口不能最小化
    titlename = "此电脑"
    hwnd = win32gui.FindWindow(0,titlename)

    # 获取句柄窗口的大小信息
    left, top, right, bot = win32gui.GetWindowRect(hwnd)

    print(left,top,right,bot)

    # 移动窗口到目标位置
    win32gui.MoveWindow(hwnd, -7, 0, 953, 540, 0)


