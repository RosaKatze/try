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