# coding=UTF-8
# This Python file uses the following encoding: utf-8
import turtle as t
import cv2

t.title('BingDwenDwen_CV 公众号：越哥聊IT')
t.getscreen().colormode(255)
# 调用opencv读取并创建灰度图像，按BGR顺序
img = cv2.imread("bingdwendwen.png")[0: -2: 2]
width = len(img[0])
height = len(img)
t.setup(width=width / 2 + 100, height=height + 100)
t.pu()
t.goto(-width / 4 + 10, height / 2 - 10)
t.pd()
t.tracer(2000)
for k1, i in enumerate(img):
    for j in i[::2]:
        t.pencolor((j[0], j[1], j[2]))
        t.fd(1)
    t.pu()
    t.goto(-width / 4 + 10, height / 2 - 10 - k1 - 1)
    t.pd()
t.done()