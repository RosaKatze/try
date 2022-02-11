import win32gui


def setsize():
    # 获取后台窗口的句柄，注意后台窗口不能最小化
    titlename = "阴阳师 - MuMu模拟器"
    classname = ""
    hwnd = win32gui.FindWindow(0, titlename)

    # 获取句柄窗口的大小信息
    left, top, right, bot = win32gui.GetWindowRect(hwnd)
    print(left, top, right, bot)

    # 移动窗口到目标位置
    # win32gui.MoveWindow(hwnd, 961, 0, 966, 526, 0)
