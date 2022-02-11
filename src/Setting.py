import win32gui


def startimage():
    templateimage = r"G:\test\star.png"
    return templateimage


def battleimage():
    templateimage = r"G:\test\battle.png"
    return templateimage


def endimage():
    templateimage = r"G:\test\end.png"
    return templateimage


# 挂一次魂土的时间
def time():
    return 3


"""
# 开始的截图范围
def starshot():
    titlename = "阴阳师 - MuMu模拟器"
    hwnd = win32gui.FindWindow(0, titlename)
    left, top, right, bot = win32gui.GetWindowRect(hwnd)
    print(left, top, right, bot)
    leftop_x = int((right - left) * 0.842105 + left)
    leftop_y = int((bot - top) * 0.8090909 + top)
    rightbot_x = int((right - left) * 0.949248 + left)
    rightbot_y = int((bot - top) * 0.954545 + top)
    region = (leftop_x, leftop_y, rightbot_x, rightbot_y)
    print(leftop_x, leftop_y, rightbot_x, rightbot_y)
    return region


# 开始的点击范围
def startclick():
    titlename = "阴阳师 - MuMu模拟器"
    hwnd = win32gui.FindWindow(0, titlename)
    left, top, right, bot = win32gui.GetWindowRect(hwnd)
    print(left, top, right, bot)
    leftop_x = int((right - left) * 0.879699 + left)
    leftop_y = int((bot - top) * 0.854545 + top)
    rightbot_x = int((right - left) * 0.93233 + left)
    rightbot_y = int((bot - top) * 0.8969697 + top)
    print(leftop_x, leftop_y, rightbot_x, rightbot_y)
    return leftop_x, leftop_y, rightbot_x, rightbot_y

# 战斗界面的截图范围
def battleshot():
    titlename = "阴阳师 - MuMu模拟器"
    hwnd = win32gui.FindWindow(0, titlename)
    left, top, right, bot = win32gui.GetWindowRect(hwnd)
    print(left, top, right, bot)
    percent = 1
    leftop_x = (right - left) * percent + left
    leftop_y = (bot - top) * percent + top
    rightbot_x = (right - left) * percent + left
    rightbot_y = (bot - top) * percent + top
    region = (leftop_x, leftop_y, rightbot_x, rightbot_y)
    return region

# 战斗界面的点击范围
def battleclick():
    titlename = "阴阳师 - MuMu模拟器"
    hwnd = win32gui.FindWindow(0, titlename)
    left, top, right, bot = win32gui.GetWindowRect(hwnd)
    print(left, top, right, bot)
    percent = 1
    leftop_x = int((right - left) * 0.879699 + left)
    leftop_y = int((bot - top) * 0.854545 + top)
    rightbot_x = int((right - left) * 0.93233 + left)
    rightbot_y = int((bot - top) * 0.8969697 + top)
    return leftop_x, leftop_y, rightbot_x, rightbot_y

# 结束界面的截图范围
def endshot():
    titlename = "阴阳师 - MuMu模拟器"
    hwnd = win32gui.FindWindow(0, titlename)
    left, top, right, bot = win32gui.GetWindowRect(hwnd)
    print(left, top, right, bot)
    percent = 1
    leftop_x = int((right - left) * 0.879699 + left)
    leftop_y = int((bot - top) * 0.854545 + top)
    rightbot_x = int((right - left) * 0.93233 + left)
    rightbot_y = int((bot - top) * 0.8969697 + top)
    region = (leftop_x, leftop_y, rightbot_x, rightbot_y)
    return region

# 结束界面的点击范围
def endclick():
    titlename = "阴阳师 - MuMu模拟器"
    hwnd = win32gui.FindWindow(0, titlename)
    left, top, right, bot = win32gui.GetWindowRect(hwnd)
    print(left, top, right, bot)
    percent = 1
    leftop_x = int((right - left) * 0.879699 + left)
    leftop_y = int((bot - top) * 0.854545 + top)
    rightbot_x = int((right - left) * 0.93233 + left)
    rightbot_y = int((bot - top) * 0.8969697 + top)
    return leftop_x, leftop_y, rightbot_x, rightbot_y
"""

"""
# 开始按钮的坐标
def startpoint():
    x = 1867
    y = 990
    return x, y


# 开始按钮的rgb
def startpointrgb():
    r = 220
    g = 208
    b = 185
    return r, g, b


# 战斗界面的坐标
def battlepoint():
    x = 1432
    y = 755
    return x, y


# 战斗界面的rgb
def battlepointrgb():
    r = 199
    g = 166
    b = 124
    return r, g, b


# 结束界面的坐标
def endpoint():
    x = 1420
    y = 1011
    return x, y


# 结束界面的rgb
def endpointrgb():
    r = 187
    g = 153
    b = 108
    return r, g, b
"""
