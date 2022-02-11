import guaji
"""
用模拟器吧，官服的yys窗口调整大小会有bug
Setwindow.setsize()
"""

guaji.start()
guaji.battle()
guaji.end()

cishu = 0
while cishu > 0:

    guaji.start()
    guaji.battle()
    guaji.end()
    cishu = cishu-1
    print("剩余次数:", cishu)


"""
1. [python打印出所有窗体的句柄类名和标题和句柄（可显示子句柄）](https://www.cnblogs.com/myfriend/articles/12509278.html)
2. [python3应用windows api对后台程序窗口及桌面截图并保存的方法](https://www.jb51.net/article/168576.htm)
3. [如何利用Python和win32编程避免重复性体力劳动（一）——开始、FindWindow和FindWindowEx](https://blog.csdn.net/seele52/article/details/17504925)
4. [通过截图匹配原图中的位置（opencv）](https://blog.csdn.net/ns2250225/article/details/60334176/)
Aircv是一款基于Python-opencv2的目标定位。
5. [窗口的位置：GetWindowRect与MoveWindow等](https://blog.csdn.net/fyyyr/article/details/79252897?utm_medium=distribute.pc_relevant.none-task-blog-BlogCommendFromBaidu-1.control&depth_1-utm_source=distribute.pc_relevant.none-task-blog-BlogCommendFromBaidu-1.control)
6. [python---win32gui、win32con、win32api：winAPI操作](https://www.cnblogs.com/liming19680104/p/11988565.html)
7. [Python基础系列讲解-自动控制windows桌面](https://www.imooc.com/article/288884)
"""
