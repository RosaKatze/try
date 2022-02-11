"""
1. [python打印出所有窗体的句柄类名和标题和句柄（可显示子句柄）](https://www.cnblogs.com/myfriend/articles/12509278.html)
2. [python3应用windows api对后台程序窗口及桌面截图并保存的方法](https://www.jb51.net/article/168576.htm)
3. [如何利用Python和win32编程避免重复性体力劳动（一）——开始、FindWindow和FindWindowEx](https://blog.csdn.net/seele52/article/details/17504925)
4. [通过截图匹配原图中的位置（opencv）](https://blog.csdn.net/ns2250225/article/details/60334176/)
Aircv是一款基于Python-opencv2的目标定位。
5. [窗口的位置：GetWindowRect与MoveWindow等](https://blog.csdn.net/fyyyr/article/details/79252897?utm_medium=distribute.pc_relevant.none-task-blog-BlogCommendFromBaidu-1.control&depth_1-utm_source=distribute.pc_relevant.none-task-blog-BlogCommendFromBaidu-1.control)
6. [python---win32gui、win32con、win32api：winAPI操作](https://www.cnblogs.com/liming19680104/p/11988565.html)
7. [Python基础系列讲解-自动控制windows桌面](https://www.imooc.com/article/288884)
8. [python：pyautogui自动化操作](https://blog.csdn.net/weixin_44374471/article/details/99753617?utm_medium=distribute.pc_relevant.none-task-blog-2~default~baidujs_baidulandingword~default-1.pc_relevant_default&spm=1001.2101.3001.4242.2&utm_relevant_index=4)
"""

# """"""
# import time
# import random
# import win32api
# import win32con
# import Setting
# import Image
#
#
# def start():
#     """
#     # 开始按钮的坐标
#     startpointx, startponity = Setting.startpoint()
#     # 开始按钮的rgb
#     startponitrgb_r, startponitrgb_g, startponitrgb_b = Setting.startpointrgb()
#     # 开始的点击范围
#     # startregion_lefttop_x, startregion_lefttop_y, startregion_rightbot_x, startregion_rightbot_y = Setting.startregion()
#     # is_start = pyautogui.pixelMatchesColor(startpointx, startponity,
#                                             (startponitrgb_r, startponitrgb_g, startponitrgb_b))  # 开始界面
#     win32api.SetCursorPos((startpointx, startponity))  # 将鼠标移动到开始按钮
#
#     # 先从setting里取值
#     # 目标图片和模板图片
#     targetimage, templateimage = Setting.startimage()
#     # 截图范围
#     region = Setting.starshot()
#     # 点击范围
#     startregion_lefttop_x, startregion_lefttop_y, startregion_rightbot_x, startregion_rightbot_y = Setting.startclick()
#     # 尝试用图形匹配来做
#     Image.shot(region)  # 截图
#     is_start = Image.match(targetimage, templateimage)  # 开始界面
#     """
#     filename = Setting.startimage()
#     is_start = Image.match(filename)
#     time.sleep(0.5)
#     if is_start is not None:
#         startregion_lefttop_x, startregion_lefttop_y, startregion_rightbot_x, startregion_rightbot_y = Image.match(
#             filename)
#         win32api.SetCursorPos(
#             suiji(startregion_lefttop_x, startregion_lefttop_y, startregion_rightbot_x, startregion_rightbot_y))  # 防检测
#         win32api.mouse_event(win32con.MOUSEEVENTF_LEFTUP | win32con.MOUSEEVENTF_LEFTDOWN, 0, 0, 0, 0)  # 单击
#         print("开始")
#         time.sleep(2)
#         """
#         win32api.SetCursorPos(
#             suiji(startregion_lefttop_x, startregion_lefttop_y, startregion_rightbot_x, startregion_rightbot_y))  # 防检测
#         win32api.mouse_event(win32con.MOUSEEVENTF_LEFTUP | win32con.MOUSEEVENTF_LEFTDOWN, 0, 0, 0, 0)  # 单击
#         print("开始")
#         Image.delet()  # 进去了之后删掉刚刚的截图
#           # 稍微等待一下载入时间
#         """
#     else:
#         print("未匹配到")
#
#
# def battle():
#     """
#     # 先从setting里取值
#     # 战斗界面的坐标
#     battlepointx, battleponity = Setting.battlepoint()
#     # 战斗界面的rgb
#     battleponitrgb_r, battleponitrgb_g, battleponitrgb_b = Setting.battlepointrgb()
#     # 战斗界面的范围
#     battleregion_lefttop_x, battleregion_lefttop_y, battleregion_rightbot_x, battleregion_rightbot_y = Setting.battleregion()
#
#
#     is_battle = pyautogui.pixelMatchesColor(battlepointx, battleponity,
#                                             (battleponitrgb_r, battleponitrgb_g, battleponitrgb_b))  # 确认是否在战斗界面
#     win32api.SetCursorPos((battlepointx, battleponity))
#     # 先从setting里取值
#     # 目标图片和模板图片
#     targetimage, templateimage = Setting.battleimage()
#     # 截图范围
#     region = Setting.battleshot()
#     # 点击范围
#     battleregion_lefttop_x, battleregion_lefttop_y, battleregion_rightbot_x, battleregion_rightbot_y = Setting.battleclick()
#     # 尝试用图形匹配来做
#     Image.shot(region)  # 截图
#     """
#     filename = Setting.battleimage()
#     is_battle = Image.match(filename)  # 战斗界面
#     is_battle
#     if is_battle is not None:
#         # 点击范围
#         battleregion_lefttop_x, battleregion_lefttop_y, battleregion_rightbot_x, battleregion_rightbot_y = Image.match(
#             filename)
#         # 鼠标移动，防检测
#         win32api.SetCursorPos(
#             suiji(battleregion_lefttop_x, battleregion_lefttop_y, battleregion_rightbot_x,battleregion_rightbot_y))
#         print("正在战斗")
#         time.sleep(Setting.time())  # 这个就是挂魂土的时间
#         print("打完了")
#         time.sleep(2)
#
#
# def end():
#     """
#     # 先从setting里取值
#     # 结束界面的坐标
#     endpointx, endponity = Setting.endpoint()
#     # 结束界面的rgb
#     endponitrgb_r, endponitrgb_g, endponitrgb_b = Setting.endpointrgb()
#     # 结束界面的点击范围
#     endregion_lefttop_x, endregion_lefttop_y, endregion_rightbot_x, endregion_rightbot_y = Setting.endregion()
#
#     is_end = pyautogui.pixelMatchesColor(endpointx, endponity,
#                                          (endponitrgb_r, endponitrgb_g, endponitrgb_b))  # 确认是否在结束界面
#     win32api.SetCursorPos((endpointx, endponity))
#
#     # 先从setting里取值
#     # 目标图片和模板图片
#     targetimage, templateimage = Setting.endimage()
#     # 截图范围和是一样的
#     region = Setting.endshot()
#     # 点击范围
#     endregion_lefttop_x, endregion_lefttop_y, endregion_rightbot_x, endregion_rightbot_y = Setting.endclick()
#     # 尝试用图形匹配来做
#     Image.shot(region)  # 截图
#     """
#     filename = Setting.endimage()
#     is_end = Image.match(filename)  # 结束界面
#     if is_end is not None:
#         # 点击范围
#         endregion_lefttop_x, endregion_lefttop_y, endregion_rightbot_x, endregion_rightbot_y = Image.match(
#             filename)
#         # 防检测
#         win32api.SetCursorPos(
#             suiji(endregion_lefttop_x, endregion_lefttop_y, endregion_rightbot_x, endregion_rightbot_y))
#         print("结算中")
#         time.sleep(1)  # 要等一会，跳出界面点才有用
#         print("我在狂点")
#         for i in range(0, random.randint(10, 14)):  # 随机点击次数10到14次
#             win32api.SetCursorPos(
#                 suiji(endregion_lefttop_x, endregion_lefttop_y, endregion_rightbot_x, endregion_rightbot_y))  # 防检测
#             win32api.mouse_event(win32con.MOUSEEVENTF_LEFTUP | win32con.MOUSEEVENTF_LEFTDOWN, 0, 0, 0, 0)  # 单击
#             time.sleep(random.uniform(0.2, 0.4))  # 每次点击间隔随机
#
#
# # 先确定点击的范围
# def suiji(xmin, ymin, xmax, ymax):
#     # 在此范围内随机生成一个数
#     x = random.randint(xmin, xmax)
#     y = random.randint(ymin, ymax)
#     return x, y
#
#
# # 后期要加一个兼容，万一弹出个悬赏框，要点掉
# def check():
#     print("点太快了，等1秒吧")
#     time.sleep(1)  # 现在遇到的情况是，end那边点太快了，还没来得及进准备界面呢，所以等1秒就行
#     start()  # 然后再start就行
#
#     """
#     battle = pyautogui.pixelMatchesColor(457, 165, (214, 196, 161))  # 确认是否在战斗界面
#     win32api.SetCursorPos( (956,1059) )
#     if is_zhunbei:
#         print('重新开始')
#         time.sleep(0.2)
#         start()
#     if battle:
#         print('进入战斗成功')
#     else:
#         print('出了问题，退出程序')
#         sys.exit(0)
#     """
#
#
# def test():
#     win32api.SetCursorPos((705, 1060))  # 防检测
#     win32api.mouse_event(win32con.MOUSEEVENTF_LEFTUP | win32con.MOUSEEVENTF_LEFTDOWN, 0, 0, 0, 0)  # 单击
#
# import os
# import cv2
# import pyautogui
# from PIL import ImageGrab
# import cv2
#
#
# def match(filename):
#     location = pyautogui.locateOnScreen(filename, confidence=0.9)
#     if location is not None:
#         xmin = location.left
#         ymin = location.top
#         xmax = location.left + location.width
#         ymax = location.top + location.height
#         return xmin, ymin, xmax, ymax
#     else:
#         return None
#
#     # print(center)
#     # pyautogui.moveTo(center)
#     # pyautogui.click(center, clicks=2, interval=0.1, button='left')
#
#
# # file = r"G:\test\test.png"
# # match(file)
#
# """
# # 对指定区域进行截图，并保存
# def shot(region):
#     img = ImageGrab.grab(region)
#     img.save(r"G:\test\test.png")
#
#
# # 删除图片
# def delet():
#     file_name = r"G:\test\test.png"
#     if os.path.exists(file_name):
#         os.remove(file_name)
#         print('成功删除文件:', file_name)
#     else:
#         print('未找到此文件:', file_name)
#
#
# # 图片匹配
# def match(targetimage, templateimage):
#     # 读取目标图片
#     target = cv2.imread(targetimage)
#     # 读取模板图片
#     template = cv2.imread(templateimage)
#     # 获得模板图片的高宽尺寸
#     # theight, twidth = template.shape[:2]
#     # 执行模板匹配，采用的匹配方式cv2.TM_SQDIFF_NORMED
#     result = cv2.matchTemplate(target, template, cv2.TM_SQDIFF_NORMED)
#     # 归一化处理
#     cv2.normalize(result, result, 0, 1, cv2.NORM_MINMAX, -1)
#     # 寻找矩阵（一维数组当做向量，用Mat定义）中的最大值和最小值的匹配结果及其位置
#     min_val, max_val, min_loc, max_loc = cv2.minMaxLoc(result)
#     # 匹配值转换为字符串
#     # 对于cv2.TM_SQDIFF及cv2.TM_SQDIFF_NORMED方法min_val越趋近与0匹配度越好，匹配位置取min_loc
#     # 对于其他方法max_val越趋近于1匹配度越好，匹配位置取max_loc
#     # strmin_val = str(min_val)
#     # 绘制矩形边框，将匹配区域标注出来
#     # min_loc：矩形定点
#     # (min_loc[0]+twidth,min_loc[1]+theight)：矩形的宽高
#     # (0,0,225)：矩形的边框颜色；2：矩形边框宽度
#     # cv2.rectangle(target, min_loc, (min_loc[0] + twidth, min_loc[1] + theight), (0, 0, 225), 2)
#     # 显示结果,并将匹配值显示在标题栏上
#     # cv2.imshow("MatchResult----MatchingValue=" + strmin_val, target)
#     # cv2.waitKey()
#     # cv2.destroyAllWindows()
#     print("期望：", min_val)
#     expectation = 1e-10
#     if 0 < min_val < expectation:
#         print("匹配到了")
#         return 1
#     else:
#         print("未匹配到")
#         return 0
#
#
# """
#
# import win32gui
#
#
# def startimage():
#     templateimage = r"G:\test\star.png"
#     return templateimage
#
#
# def battleimage():
#     templateimage = r"G:\test\battle.png"
#     return templateimage
#
#
# def endimage():
#     templateimage = r"G:\test\end.png"
#     return templateimage
#
#
# # 挂一次魂土的时间
# def time():
#     return 3
#
#
# """
# # 开始的截图范围
# def starshot():
#     titlename = "阴阳师 - MuMu模拟器"
#     hwnd = win32gui.FindWindow(0, titlename)
#     left, top, right, bot = win32gui.GetWindowRect(hwnd)
#     print(left, top, right, bot)
#     leftop_x = int((right - left) * 0.842105 + left)
#     leftop_y = int((bot - top) * 0.8090909 + top)
#     rightbot_x = int((right - left) * 0.949248 + left)
#     rightbot_y = int((bot - top) * 0.954545 + top)
#     region = (leftop_x, leftop_y, rightbot_x, rightbot_y)
#     print(leftop_x, leftop_y, rightbot_x, rightbot_y)
#     return region
#
#
# # 开始的点击范围
# def startclick():
#     titlename = "阴阳师 - MuMu模拟器"
#     hwnd = win32gui.FindWindow(0, titlename)
#     left, top, right, bot = win32gui.GetWindowRect(hwnd)
#     print(left, top, right, bot)
#     leftop_x = int((right - left) * 0.879699 + left)
#     leftop_y = int((bot - top) * 0.854545 + top)
#     rightbot_x = int((right - left) * 0.93233 + left)
#     rightbot_y = int((bot - top) * 0.8969697 + top)
#     print(leftop_x, leftop_y, rightbot_x, rightbot_y)
#     return leftop_x, leftop_y, rightbot_x, rightbot_y
#
# # 战斗界面的截图范围
# def battleshot():
#     titlename = "阴阳师 - MuMu模拟器"
#     hwnd = win32gui.FindWindow(0, titlename)
#     left, top, right, bot = win32gui.GetWindowRect(hwnd)
#     print(left, top, right, bot)
#     percent = 1
#     leftop_x = (right - left) * percent + left
#     leftop_y = (bot - top) * percent + top
#     rightbot_x = (right - left) * percent + left
#     rightbot_y = (bot - top) * percent + top
#     region = (leftop_x, leftop_y, rightbot_x, rightbot_y)
#     return region
#
# # 战斗界面的点击范围
# def battleclick():
#     titlename = "阴阳师 - MuMu模拟器"
#     hwnd = win32gui.FindWindow(0, titlename)
#     left, top, right, bot = win32gui.GetWindowRect(hwnd)
#     print(left, top, right, bot)
#     percent = 1
#     leftop_x = int((right - left) * 0.879699 + left)
#     leftop_y = int((bot - top) * 0.854545 + top)
#     rightbot_x = int((right - left) * 0.93233 + left)
#     rightbot_y = int((bot - top) * 0.8969697 + top)
#     return leftop_x, leftop_y, rightbot_x, rightbot_y
#
# # 结束界面的截图范围
# def endshot():
#     titlename = "阴阳师 - MuMu模拟器"
#     hwnd = win32gui.FindWindow(0, titlename)
#     left, top, right, bot = win32gui.GetWindowRect(hwnd)
#     print(left, top, right, bot)
#     percent = 1
#     leftop_x = int((right - left) * 0.879699 + left)
#     leftop_y = int((bot - top) * 0.854545 + top)
#     rightbot_x = int((right - left) * 0.93233 + left)
#     rightbot_y = int((bot - top) * 0.8969697 + top)
#     region = (leftop_x, leftop_y, rightbot_x, rightbot_y)
#     return region
#
# # 结束界面的点击范围
# def endclick():
#     titlename = "阴阳师 - MuMu模拟器"
#     hwnd = win32gui.FindWindow(0, titlename)
#     left, top, right, bot = win32gui.GetWindowRect(hwnd)
#     print(left, top, right, bot)
#     percent = 1
#     leftop_x = int((right - left) * 0.879699 + left)
#     leftop_y = int((bot - top) * 0.854545 + top)
#     rightbot_x = int((right - left) * 0.93233 + left)
#     rightbot_y = int((bot - top) * 0.8969697 + top)
#     return leftop_x, leftop_y, rightbot_x, rightbot_y
# """
#
# """
# # 开始按钮的坐标
# def startpoint():
#     x = 1867
#     y = 990
#     return x, y
#
#
# # 开始按钮的rgb
# def startpointrgb():
#     r = 220
#     g = 208
#     b = 185
#     return r, g, b
#
#
# # 战斗界面的坐标
# def battlepoint():
#     x = 1432
#     y = 755
#     return x, y
#
#
# # 战斗界面的rgb
# def battlepointrgb():
#     r = 199
#     g = 166
#     b = 124
#     return r, g, b
#
#
# # 结束界面的坐标
# def endpoint():
#     x = 1420
#     y = 1011
#     return x, y
#
#
# # 结束界面的rgb
# def endpointrgb():
#     r = 187
#     g = 153
#     b = 108
#     return r, g, b
# """
