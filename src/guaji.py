import sys
import time
import pyautogui
import random
import win32api
import win32con

def start():
    is_start = pyautogui.pixelMatchesColor(956, 1059, (66, 66, 66)) # 开始界面
    win32api.SetCursorPos( (956,1059) )
    if is_start:
        win32api.SetCursorPos(fanwei(945, 963, 1046, 1067)) #防检测
        win32api.mouse_event(win32con.MOUSEEVENTF_LEFTUP | win32con.MOUSEEVENTF_LEFTDOWN, 0, 0, 0, 0) #单击
        print('点击开始')


def battle():
    is_battle = pyautogui.pixelMatchesColor(857, 1063, (170, 168, 166))  # 确认是否在战斗界面
    win32api.SetCursorPos( (857,1063) )
    if is_battle:
        win32api.SetCursorPos(fanwei(615, 638, 545, 557)) #鼠标移动，防检测
        print('正在战斗')
        time.sleep(1)
        print('打完了')


def end():
    is_end = pyautogui.pixelMatchesColor(560, 1060, (196, 187, 118))  # 确认是否在结束界面
    win32api.SetCursorPos( (560,1060) )
    if is_end:
        win32api.SetCursorPos(fanwei(615, 638, 545, 557)) #防检测
        print('结算中')
        for i in range(0, random.randint(7, 9)):  # 随机点击次数7到9次
            win32api.SetCursorPos(fanwei(541, 576, 1044, 1068)) #防检测
            win32api.mouse_event(win32con.MOUSEEVENTF_LEFTUP | win32con.MOUSEEVENTF_LEFTDOWN, 0, 0, 0, 0) #单击
            time.sleep(0.3)
        time.sleep(1)  # 执行完成后暂停一秒


# 先确定点击的范围
def fanwei(xmin , xmax , ymin , ymax):

    # 在此范围内随机生成一个数
    x = random.randint(xmin,xmax)
    y = random.randint(ymin,ymax)

    return x,y



def check():
    is_zhunbei = pyautogui.pixelMatchesColor(413, 889, (58, 32, 33)) # 准备界面
    battle = pyautogui.pixelMatchesColor(457, 165, (214, 196, 161))  # 确认是否在战斗界面
    win32api.SetCursorPos( (956,1059) )
    if is_zhunbei:
        print('重新开始')
        time.sleep(0.2)
        start()
    if battle:
        print('进入战斗成功')
    else:
        print('出了问题，退出程序')
        sys.exit(0)
