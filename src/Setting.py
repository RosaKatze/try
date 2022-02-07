def startimage():
    targetimage = r"G:\test\start.png"
    templateimage = r"G:\test\test.png"
    return targetimage, templateimage


def battleimage():
    targetimage = r"G:\test\battle.png"
    templateimage = r"G:\test\test.png"
    return targetimage, templateimage


def endimage():
    targetimage = r"G:\test\end.png"
    templateimage = r"G:\test\test.png"
    return targetimage, templateimage


# 开始的截图范围
def starshot():
    leftop_x = 307
    leftop_y = 0
    rightbot_x = 404
    rightbot_y = 22
    region = (leftop_x, leftop_y, rightbot_x, rightbot_y)
    return region


# 开始的点击范围
def startclick():
    leftop_x = 307
    leftop_y = 0
    rightbot_x = 404
    rightbot_y = 22
    return leftop_x, leftop_y, rightbot_x, rightbot_y


# 战斗界面的截图范围
def battleshot():
    leftop_x = 307
    leftop_y = 0
    rightbot_x = 404
    rightbot_y = 22
    region = (leftop_x, leftop_y, rightbot_x, rightbot_y)
    return region


# 战斗界面的点击范围
def battleclick():
    leftop_x = 1393
    leftop_y = 746
    rightbot_x = 1911
    rightbot_y = 1026
    return leftop_x, leftop_y, rightbot_x, rightbot_y


# 结束界面的截图范围
def endshot():
    leftop_x = 307
    leftop_y = 0
    rightbot_x = 404
    rightbot_y = 22
    region = (leftop_x, leftop_y, rightbot_x, rightbot_y)
    return region


# 结束界面的点击范围
def endclick():
    leftop_x = 1727
    leftop_y = 935
    rightbot_x = 1808
    rightbot_y = 969
    return leftop_x, leftop_y, rightbot_x, rightbot_y


# 挂一次魂土的时间
def time():
    return 3


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
