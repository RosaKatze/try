import time

import win32api
import win32gui, win32ui, win32con

def setsize():
    # 获取后台窗口的句柄，注意后台窗口不能最小化,类名可以通过windows元素捕捉工具inspect获取，或Visual Studio的SPY++工具获取
    hwnd = win32gui.FindWindow("Notepad",None)

    # 获取句柄窗口的大小信息
    left, top, right, bot = win32gui.GetWindowRect(hwnd)

    print(left,top,right,bot)

    # 顶部中间位置的x坐标
    topmidx = round ( (right - left)/2 + left )
    # 顶部中间位置的y坐标
    topmidy = top + 8

    print(topmidx,topmidy)
    # 移动到顶部中间位置
    win32api.SetCursorPos( (topmidx,topmidy) )
    # 按住左键
    win32api.mouse_event(win32con.MOUSEEVENTF_LEFTDOWN, 0, 0)
    time.sleep(0.5)

    # 拖动到屏幕上角
    win32api.SetCursorPos( (0,0) )
    time.sleep(0.5)
    win32api.mouse_event(win32con.MOUSEEVENTF_LEFTUP, 0, 0)


    time.sleep(1)
    # 获取后台窗口的句柄，注意后台窗口不能最小化,类名可以通过windows元素捕捉工具inspect获取，或Visual Studio的SPY++工具获取
    hwnd = win32gui.FindWindow("Notepad",None)
    # 获取句柄窗口的大小信息
    left, top, right, bot = win32gui.GetWindowRect(hwnd)
    print(left,top,right,bot)

    win32api.SetCursorPos( (right-17,bot-10) )

    win32api.mouse_event(win32con.MOUSEEVENTF_LEFTDOWN, 0, 0)
    time.sleep(0.5)
    win32api.SetCursorPos( (960,540) )
    time.sleep(0.5)
    win32api.mouse_event(win32con.MOUSEEVENTF_LEFTUP, 0, 0)


