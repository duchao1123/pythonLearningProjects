"""
pygame库 api文档 及 使用例子
"""
import pygame as py

'''
初始化，
'''
py.init()

'''
获取显示的窗口surface
传入元组为宽高
'''
screen = py.display.set_mode((1200, 100))

'''
填充背景颜色
'''
screen.fill((255, 255, 255))

'''
获取屏幕rect
'''
rect = screen.get_rect()

'''
加载图片资源，返回surface
可以推断绘制是surface组合和堆叠
'''
image = py.image.load('../images/ship.bmp')

'''
image 同 screen一样都是surface，所以可以获取rect
'''
image_rect = image.get_rect()

'''
midbottom = Tuple[int, int]，应该就是坐标值x, y
'''
image_rect.midbottom = rect.midbottom

'''
在screen指定位置image_rect，绘制图片
'''
screen.blit(image, image_rect)

'''
设置窗口标题
'''
py.display.set_caption("title")

'''
获取事件
包括键盘和鼠标
'''
py.event.get()

'''
用户点击退出
pygame内置了很多事件
见 {@link Constants}
'''
py.QUIT

'''
刷新，
将原来的ui清掉，渲染新的ui
'''
py.display.flip()


'''
创建时钟，调用tick，控制游戏帧率
'''
clock = py.time.Clock()
clock.tick(60)







