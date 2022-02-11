import time
import random
import win32api
import win32con
import Setting
import Image


def start():
    """
    # 开始按钮的坐标
    startpointx, startponity = Setting.startpoint()
    # 开始按钮的rgb
    startponitrgb_r, startponitrgb_g, startponitrgb_b = Setting.startpointrgb()
    # 开始的点击范围
    # startregion_lefttop_x, startregion_lefttop_y, startregion_rightbot_x, startregion_rightbot_y = Setting.startregion()
    # is_start = pyautogui.pixelMatchesColor(startpointx, startponity,
                                            (startponitrgb_r, startponitrgb_g, startponitrgb_b))  # 开始界面
    win32api.SetCursorPos((startpointx, startponity))  # 将鼠标移动到开始按钮

    # 先从setting里取值
    # 目标图片和模板图片
    targetimage, templateimage = Setting.startimage()
    # 截图范围
    region = Setting.starshot()
    # 点击范围
    startregion_lefttop_x, startregion_lefttop_y, startregion_rightbot_x, startregion_rightbot_y = Setting.startclick()
    # 尝试用图形匹配来做
    Image.shot(region)  # 截图
    is_start = Image.match(targetimage, templateimage)  # 开始界面
    """
    filename = Setting.startimage()
    is_start = Image.match(filename)
    time.sleep(0.5)
    if is_start is not None:
        startregion_lefttop_x, startregion_lefttop_y, startregion_rightbot_x, startregion_rightbot_y = Image.match(
            filename)
        win32api.SetCursorPos(
            suiji(startregion_lefttop_x, startregion_lefttop_y, startregion_rightbot_x, startregion_rightbot_y))  # 防检测
        win32api.mouse_event(win32con.MOUSEEVENTF_LEFTUP | win32con.MOUSEEVENTF_LEFTDOWN, 0, 0, 0, 0)  # 单击
        print("开始")
        time.sleep(2)
        """
        win32api.SetCursorPos(
            suiji(startregion_lefttop_x, startregion_lefttop_y, startregion_rightbot_x, startregion_rightbot_y))  # 防检测
        win32api.mouse_event(win32con.MOUSEEVENTF_LEFTUP | win32con.MOUSEEVENTF_LEFTDOWN, 0, 0, 0, 0)  # 单击
        print("开始")
        Image.delet()  # 进去了之后删掉刚刚的截图
          # 稍微等待一下载入时间
        """
    else:
        print("未匹配到")


def battle():
    """
    # 先从setting里取值
    # 战斗界面的坐标
    battlepointx, battleponity = Setting.battlepoint()
    # 战斗界面的rgb
    battleponitrgb_r, battleponitrgb_g, battleponitrgb_b = Setting.battlepointrgb()
    # 战斗界面的范围
    battleregion_lefttop_x, battleregion_lefttop_y, battleregion_rightbot_x, battleregion_rightbot_y = Setting.battleregion()


    is_battle = pyautogui.pixelMatchesColor(battlepointx, battleponity,
                                            (battleponitrgb_r, battleponitrgb_g, battleponitrgb_b))  # 确认是否在战斗界面
    win32api.SetCursorPos((battlepointx, battleponity))
    # 先从setting里取值
    # 目标图片和模板图片
    targetimage, templateimage = Setting.battleimage()
    # 截图范围
    region = Setting.battleshot()
    # 点击范围
    battleregion_lefttop_x, battleregion_lefttop_y, battleregion_rightbot_x, battleregion_rightbot_y = Setting.battleclick()
    # 尝试用图形匹配来做
    Image.shot(region)  # 截图
    """
    filename = Setting.battleimage()
    is_battle = Image.match(filename)  # 战斗界面
    is_battle
    if is_battle is not None:
        # 点击范围
        battleregion_lefttop_x, battleregion_lefttop_y, battleregion_rightbot_x, battleregion_rightbot_y = Image.match(
            filename)
        # 鼠标移动，防检测
        win32api.SetCursorPos(
            suiji(battleregion_lefttop_x, battleregion_lefttop_y, battleregion_rightbot_x,battleregion_rightbot_y))
        print("正在战斗")
        time.sleep(Setting.time())  # 这个就是挂魂土的时间
        print("打完了")
        time.sleep(2)


def end():
    """
    # 先从setting里取值
    # 结束界面的坐标
    endpointx, endponity = Setting.endpoint()
    # 结束界面的rgb
    endponitrgb_r, endponitrgb_g, endponitrgb_b = Setting.endpointrgb()
    # 结束界面的点击范围
    endregion_lefttop_x, endregion_lefttop_y, endregion_rightbot_x, endregion_rightbot_y = Setting.endregion()

    is_end = pyautogui.pixelMatchesColor(endpointx, endponity,
                                         (endponitrgb_r, endponitrgb_g, endponitrgb_b))  # 确认是否在结束界面
    win32api.SetCursorPos((endpointx, endponity))

    # 先从setting里取值
    # 目标图片和模板图片
    targetimage, templateimage = Setting.endimage()
    # 截图范围和是一样的
    region = Setting.endshot()
    # 点击范围
    endregion_lefttop_x, endregion_lefttop_y, endregion_rightbot_x, endregion_rightbot_y = Setting.endclick()
    # 尝试用图形匹配来做
    Image.shot(region)  # 截图
    """
    filename = Setting.endimage()
    is_end = Image.match(filename)  # 结束界面
    if is_end is not None:
        # 点击范围
        endregion_lefttop_x, endregion_lefttop_y, endregion_rightbot_x, endregion_rightbot_y = Image.match(
            filename)
        # 防检测
        win32api.SetCursorPos(
            suiji(endregion_lefttop_x, endregion_lefttop_y, endregion_rightbot_x, endregion_rightbot_y))
        print("结算中")
        time.sleep(1)  # 要等一会，跳出界面点才有用
        print("我在狂点")
        for i in range(0, random.randint(10, 14)):  # 随机点击次数10到14次
            win32api.SetCursorPos(
                suiji(endregion_lefttop_x, endregion_lefttop_y, endregion_rightbot_x, endregion_rightbot_y))  # 防检测
            win32api.mouse_event(win32con.MOUSEEVENTF_LEFTUP | win32con.MOUSEEVENTF_LEFTDOWN, 0, 0, 0, 0)  # 单击
            time.sleep(random.uniform(0.2, 0.4))  # 每次点击间隔随机


# 先确定点击的范围
def suiji(xmin, ymin, xmax, ymax):
    # 在此范围内随机生成一个数
    x = random.randint(xmin, xmax)
    y = random.randint(ymin, ymax)
    return x, y


# 后期要加一个兼容，万一弹出个悬赏框，要点掉
def check():
    print("点太快了，等1秒吧")
    time.sleep(1)  # 现在遇到的情况是，end那边点太快了，还没来得及进准备界面呢，所以等1秒就行
    start()  # 然后再start就行

    """
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
    """


def test():
    win32api.SetCursorPos((705, 1060))  # 防检测
    win32api.mouse_event(win32con.MOUSEEVENTF_LEFTUP | win32con.MOUSEEVENTF_LEFTDOWN, 0, 0, 0, 0)  # 单击
