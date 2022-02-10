# BingDwenDwen

教你用Python画一个冰墩墩！欢迎关注公众号「越哥聊IT」

![WechatIMG12](https://user-images.githubusercontent.com/5102033/153436564-1c70bd83-6bfd-4aef-961a-a83f1613956a.jpeg)



## 关于turtle 库

Turtle库是Python中的一个绘制图像的函数库，turtle就是一个小乌龟，在一个横轴为x、纵轴为y的坐标系原点，(0,0)位置开始，根据一组函数指令的控制，在这个平面坐标系中移动，从而在它爬行的路径上绘制图形。

## 绘图版冰墩墩

1、打开编辑器，创建一个BingDwenDwen.py文件：

```
# coding=UTF-8
# This Python file uses the following encoding: utf-8
import turtle as t

t.title('BingDwenDwen 公众号：越哥聊IT')

# 调节绘制速度
t.speed(10) 
...

# 代码参考仓库
t.done()
```

2、执行程序：

```
python BingDwenDwen.py 
```

3、成功！
![Xnip2022-02-10_19-58-06](https://user-images.githubusercontent.com/5102033/153437590-d6e2aa61-14e7-4c23-be27-f4eff6b1659d.jpg)



## 扫描版冰墩墩

turtle是一个非常好用的自动绘图工具，但是用它来画图需要提供大量的坐标点，需要反复的执行，适合一些简单的图像描绘。

下面我们用计算机图像识别，来自动获取图片边缘的位置坐标，帮助进行画图，复制一个更加高清的冰墩墩，比如Opencv。

首先你需要一张冰墩墩的图片，命名为bingdwendwen.png，和python代码在同一个目录下。

![bingdwendwen](https://user-images.githubusercontent.com/5102033/153437648-1d347d53-2aa5-4a24-a468-370d93ecf8dd.png)


需要使用open-cv的库，以下步骤如果你的机器已经安装可以跳过：

### 1、安装pip程序库

如果你还未安装pip，则可以使用以下方法来安装，针对Mac系统，Windows系统可以搜索下相关命令：

```
$ curl https://bootstrap.pypa.io/get-pip.py -o get-pip.py  # 下载安装脚本
$ sudo python get-pip.py    # 运行安装脚本
```

注意：用哪个版本的 Python 运行安装脚本，pip 就被关联到哪个版本，如果是 Python3 则执行以下命令：

```
$ sudo python3 get-pip.py    # 运行安装脚本
```
一般情况 pip 对应的是 Python 2.7，pip3 对应的是 Python 3.x。

### 2、安装opencv-python库

opencv-python是一个图像和视频处理库，官网如下 https://pypi.org/project/opencv-python/

可以在terminal输入下面代码直接安装：

```
$  pip install opencv-python
```

命令行下使用pydoc命令查看安装的Module：
在命令行下运行$ pydoc modules即可查看。
 

### 3、运行程序

```
python3 BingDwenDwen_cv.py
```
![Xnip2022-02-10_14-15-01](https://user-images.githubusercontent.com/5102033/153437607-df2fd70a-841b-4710-93d2-948f999cd578.jpg)

