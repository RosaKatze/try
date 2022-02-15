import time
import random
import win32api
import win32con
import Setting
import Image


def start():
    # 开始界面的图片
    filename = Setting.startimage()
    # 匹配一下
    is_start = Image.match(filename)
    time.sleep(0.5)
    if is_start is not None:
        # 如果匹配到了，就直接把4个坐标拿过来
        startregion_lefttop_x, startregion_lefttop_y, startregion_rightbot_x, startregion_rightbot_y = Image.match(
            filename)
        # 移动到随机生成的坐标，防检测
        win32api.SetCursorPos(
            suiji(startregion_lefttop_x, startregion_lefttop_y, startregion_rightbot_x, startregion_rightbot_y))
        # 单击
        win32api.mouse_event(win32con.MOUSEEVENTF_LEFTUP | win32con.MOUSEEVENTF_LEFTDOWN, 0, 0, 0, 0)
        print("开始")
        # 等待加载
        time.sleep(2.5)
    else:
        print("未匹配到")
        endcheck()


def battle():
    # 战斗界面的图片
    filename = Setting.battleimage()
    # 匹配一下
    is_battle = Image.match(filename)
    if is_battle is not None:
        # 如果匹配到了，就直接把4个坐标拿过来
        battleregion_lefttop_x, battleregion_lefttop_y, battleregion_rightbot_x, battleregion_rightbot_y = Image.match(
            filename)
        # 移动到随机生成的坐标，防检测
        win32api.SetCursorPos(
            suiji(battleregion_lefttop_x, battleregion_lefttop_y, battleregion_rightbot_x, battleregion_rightbot_y))
        print("正在战斗")
        # 这个就是挂机的时间
        time.sleep(Setting.time)
        print("打完了")
        time.sleep(2.5)


def end():
    # 结束界面的图片
    filename = Setting.endimage()
    # 匹配一下
    is_end = Image.match(filename)
    if is_end is not None:
        # 如果匹配到了，就直接把4个坐标拿过来
        endregion_lefttop_x, endregion_lefttop_y, endregion_rightbot_x, endregion_rightbot_y = Image.match(
            filename)
        # 移动到随机生成的坐标，防检测
        win32api.SetCursorPos(
            suiji(endregion_lefttop_x, endregion_lefttop_y, endregion_rightbot_x, endregion_rightbot_y))
        print("结算中")
        # 要等一会，跳出界面点才有用
        time.sleep(1)
        print("我在狂点")
        # 随机点击次数5到10次
        for i in range(0, random.randint(6, 8)):
            print(i)
            # 移动到随机生成的坐标，防检测
            win32api.SetCursorPos(
                suiji(endregion_lefttop_x, endregion_lefttop_y, endregion_rightbot_x, endregion_rightbot_y))
            # 单击
            win32api.mouse_event(win32con.MOUSEEVENTF_LEFTUP | win32con.MOUSEEVENTF_LEFTDOWN, 0, 0, 0, 0)
            # 每次点击间隔随机
            time.sleep(random.uniform(0.5, 0.8))



def endcheck():
    # 结束界面的图片
    filename = Setting.endimgcheck()
    # 匹配一下
    is_end = Image.match(filename)
    if is_end is not None:
        # 如果匹配到了，就直接把4个坐标拿过来
        endregion_lefttop_x, endregion_lefttop_y, endregion_rightbot_x, endregion_rightbot_y = Image.match(
            filename)
        # 移动到随机生成的坐标，防检测
        win32api.SetCursorPos(
            suiji(endregion_lefttop_x, endregion_lefttop_y, endregion_rightbot_x, endregion_rightbot_y))
        print("结算中")
        print("我在狂点")
        # 随机点击次数5到10次
        for i in range(0, random.randint(1, 3)):
            print(i)
            # 移动到随机生成的坐标，防检测
            win32api.SetCursorPos(
                suiji(endregion_lefttop_x, endregion_lefttop_y, endregion_rightbot_x, endregion_rightbot_y))
            # 单击
            win32api.mouse_event(win32con.MOUSEEVENTF_LEFTUP | win32con.MOUSEEVENTF_LEFTDOWN, 0, 0, 0, 0)
            # 每次点击间隔随机
            time.sleep(random.uniform(0.2, 0.4))


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


def test():
    win32api.SetCursorPos((705, 1060))  # 防检测
    win32api.mouse_event(win32con.MOUSEEVENTF_LEFTUP | win32con.MOUSEEVENTF_LEFTDOWN, 0, 0, 0, 0)  # 单击
