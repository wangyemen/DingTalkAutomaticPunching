# coding: utf-8
#
import uiautomator2 as u2
import time

'''
可以加一些判断语句，
但我觉得，没有必要，
因为程序总体上是比较简单的，
只是需要注意一下网络和打开一个页面的时间
时间估计需要1分钟

You can add some judgment statements,
But I don't think it's necessary,
Because the program is relatively simple on the whole,
Just pay attention to the network and the time to open a page
Estimated time: 1 minute
'''

d = u2.connect()

# 手机解锁
d.press("power")

# 向上滑动解锁
d.swipe_ext("up", 1)

# 这是手机密码
time.sleep(2)
d.click(0.477, 0.606)
time.sleep(1)
d.click(0.492, 0.697)
time.sleep(1)
d.click(0.488, 0.779)
time.sleep(1)
d.click(0.485, 0.873)
time.sleep(1)

# 滑动到钉钉所在的页面
d.swipe_ext("left", 0.6) # 向左滑动
time.sleep(2)

# 打开dingtalk并进行“每日打卡”
d.click(0.592, 0.363)
time.sleep(3)

# 进入聊群
d.click(0.196, 0.333)
time.sleep(2)
# 点击打卡
d(resourceId="com.alibaba.android.rimet:id/title", text="打卡").click()
time.sleep(4)
# 进入打卡界面
d.click(0.696, 0.599)
time.sleep(2)
# 点击打卡任务
d.click(0.77, 0.961)
time.sleep(2)
# 点击照片
d.click(0.133, 0.888)
time.sleep(2)
# 点击图片
d.click(0.325, 0.481)
time.sleep(2)
# 选择图片
d.click(0.351, 0.171)
time.sleep(2)
# 放大图片
d.click(0.948, 0.076)
time.sleep(2)
# 勾选图片
d.click(0.914, 0.968)
time.sleep(3)
# 提交图片
d.click(0.444, 0.963)
time.sleep(2)
# 提交打卡任务
d.click(0.444, 0.963)
time.sleep(5)

# 返回主页面然后锁屏
d.press("back")
d.press("back")
d.press("back")
d.press("back")
d.press("home")
d.press("power")
