import functools

from numpy import random
import matplotlib.pyplot as plt
import matplotlib.animation as animation


def init():
    # 初始化x轴,y轴范围
    ax.set_ylim(0, 100)
    ax.set_xlim(0, 10)
    del x_data[:]
    del y_data[:]
    ln.set_data(x_data, y_data)
    return ln

# 设置画布
fig, ax = plt.subplots()

# 列表存储x,y数据
x_data, y_data = [], []
# 画图
ln, = ax.plot([], [], 'b-')        # 图像格式为蓝色实线


# 自定义动画函数frame
def update(frame, camera):
    # 每次更新传入x,y的值
    x_data.append(frame)
    y_data.append(camera)
    # 分别获取当前横、纵坐标的最大、最小值
    x_min, x_max = ax.get_xlim()
    y_min, y_max = ax.get_ylim()
    # 当数据横坐标超出图像最大横坐标时，横坐标最大值翻倍
    if frame >= x_max:
        ax.set_xlim(x_min, 2 * x_max)
    # 纵坐标操作同上
    if camera >= y_max:
        ax.set_ylim(y_min, 2 * y_max)
    # 更新绘图对象的数据
    ln.set_data(x_data, y_data)
    return ln


# 利用functools.partial传入位置参数和关键字
# 此处camera的传值没写,根据需要传入,作为纵坐标
ani = animation.FuncAnimation(fig, functools.partial(update, camera=), frames=1000, init_func=init, interval=100)
# 展示图像
plt.show()

# FuncAnimation参数说明
"""
    fig: 画布参数
    func: 在本函数中即第二个参数，在每帧中调用的函数(本程序为update)，第一个位置参数必须为frame,要传入多个位置参数使用partial方法
    frames: 动画长度，一次循环包含的帧数，在函数运行时，其值会传递给函数update(frame)的形参"frame"
    init_func: 自定义开始帧，初始化函数,即设计的init函数
    interval: 图像更新频率，以ms为单位
    
"""