# import win32gui, win32con
#
#
#
# def window_capture(filename):
#
#     # 获取后台窗口的句柄，注意后台窗口不能最小化,类名可以通过windows元素捕捉工具inspect获取，或Visual Studio的SPY++工具获取
#     hwnd = win32gui.FindWindow("Notepad",None)
#
#     # 获取句柄窗口的大小信息
#     left, top, right, bot = win32gui.GetWindowRect(hwnd)
#     w = right - left
#     h = bot - top
#
#     # 返回句柄窗口的设备环境，覆盖整个窗口，包括非客户区，标题栏，菜单，边框
#     hwndDC = win32gui.GetWindowDC(hwnd)
#
#     # 创建设备描述表
#     mfcDC = win32ui.CreateDCFromHandle(hwndDC)
#
#     # 创建内存设备描述表
#     saveDC = mfcDC.CreateCompatibleDC()
#
#     # 创建位图对象准备保存图片
#     saveBitMap = win32ui.CreateBitmap()
#
#     # 为bitmap开辟存储空间
#     saveBitMap.CreateCompatibleBitmap(mfcDC, w, h)
#
#     # 将截图保存到saveBitMap中
#     saveDC.SelectObject(saveBitMap)
#
#     # 保存bitmap到内存设备描述表
#     saveDC.BitBlt((0, 0), (w, h), mfcDC, (0, 0), win32con.SRCCOPY)
#     # 保存bitmap到文件
#     saveBitMap.SaveBitmapFile(saveDC, filename+"\img_Winapi.bmp")
#
#
#
