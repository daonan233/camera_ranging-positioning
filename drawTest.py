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


fig, ax = plt.subplots()
x_data, y_data = [], []
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
    ln.set_data(x_data, y_data)
    return ln


# 利用functools.partial传入多个参数
# 此处camera的传值没写,根据需要传入,作为纵坐标
ani = animation.FuncAnimation(fig, functools.partial(update, camera= ), frames=1000, init_func=init, interval=100)
plt.show()