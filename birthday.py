# _*_coding:utf-8_*_
# created by cy on 2022/12/16
# optimized and enhanced by [你的名字] on 2025/03/12

import turtle as t
import time
import math as m
import random as r

# ------------------------------
# 画布和工具函数
# ------------------------------
def setup_canvas():
    """初始化画布和基本设置"""
    t.setup(1.0, 1.0)  # 全屏比例
    t.bgcolor('white')
    t.title('生日快乐！')
    t.speed(2)
    t.delay(2)
    t.shape('turtle')
    # 如需瞬间出图调试，可取消下面注释：
    # t.tracer(False)

def write_text_letter_by_letter(text, start_pos=(-500, 250), font=('方正舒体', 70, 'normal'), color='green', delay=0.3):
    """逐个字符书写文本"""
    t.penup()
    t.goto(start_pos)
    for char in text:
        t.color(color)
        t.write(char, align='left', font=font)
        time.sleep(delay)

def draw_signature(signature="—小 y", pos=(450, -350), font=('JetBrains Moon', 45, 'normal'), color='green', delay=0.3):
    """逐个字符绘制署名"""
    t.penup()
    t.goto(pos)
    for char in signature:
        t.color(color)
        t.write(char, align='left', font=font)
        time.sleep(delay)

# ------------------------------
# 大熊绘制函数
# ------------------------------
def draw_bear():
    """绘制大熊图像，包括耳朵、头部、眼睛、鼻子、嘴、四肢、心形装饰以及冰糖外壳和面罩"""
    # 左耳
    t.color('black')
    t.penup()
    t.goto(-150, 200)
    t.setheading(160)
    t.begin_fill()
    t.pendown()
    t.circle(-30, 230)
    t.setheading(180)
    t.circle(37, 90)
    t.end_fill()
    # 右耳
    t.penup()
    t.goto(60, 200)
    t.setheading(20)
    t.begin_fill()
    t.pendown()
    t.circle(30, 230)
    t.setheading(0)
    t.circle(-37, 90)
    t.end_fill()
    # 头部轮廓
    t.pensize(5)
    t.penup()
    t.goto(-113, 237)
    t.setheading(30)
    t.pendown()
    t.circle(-134, 60)
    t.penup()
    t.goto(-150, 200)
    t.setheading(-120)
    t.pendown()
    t.circle(200, 80)
    t.penup()
    t.goto(60, 200)
    t.setheading(-60)
    t.pendown()
    t.circle(-200, 80)
    t.penup()
    t.setheading(210)
    t.pendown()
    t.circle(-120, 60)
    # 左眼（眼圈、眼白、眼珠）
    t.speed(10)
    t.delay(1)
    t.penup()
    t.goto(-140, 100)
    t.setheading(-45)
    t.begin_fill()
    t.pendown()
    a = 0.2
    for i in range(120):
        if 0 <= i < 30 or 60 <= i < 90:
            a += 0.1
            t.lt(3)
            t.fd(a)
        else:
            a -= 0.1
            t.lt(3)
            t.fd(a)
    t.end_fill()
    t.fillcolor("white")
    t.penup()
    t.goto(-103, 125)
    t.setheading(0)
    t.begin_fill()
    t.pendown()
    t.circle(14, 360)
    t.end_fill()
    t.penup()
    t.goto(-102, 133)
    t.setheading(0)
    t.begin_fill()
    t.pendown()
    t.circle(6, 360)
    t.end_fill()
    # 右眼（眼圈、眼白、眼珠）
    t.penup()
    t.goto(50, 100)
    t.setheading(45)
    t.fillcolor("black")
    t.pencolor("black")
    t.begin_fill()
    t.pendown()
    a = 0.2
    for i in range(120):
        if 0 <= i < 30 or 60 <= i < 90:
            a += 0.1
            t.lt(3)
            t.fd(a)
        else:
            a -= 0.1
            t.lt(3)
            t.fd(a)
    t.end_fill()
    t.fillcolor("white")
    t.penup()
    t.goto(13, 125)
    t.setheading(0)
    t.begin_fill()
    t.pendown()
    t.circle(14, 360)
    t.end_fill()
    t.penup()
    t.goto(12, 133)
    t.setheading(0)
    t.begin_fill()
    t.pendown()
    t.circle(6, 360)
    t.end_fill()
    # 鼻子
    t.speed(2)
    t.delay(2)
    t.pencolor("black")
    t.fillcolor("black")
    t.penup()
    t.goto(-55, 133)
    t.begin_fill()
    t.pendown()
    t.fd(20)
    t.seth(-120)
    t.fd(20)
    t.seth(120)
    t.fd(20)
    t.end_fill()
    # 嘴部
    t.penup()
    t.goto(-70, 110)
    t.setheading(-30)
    t.fillcolor("red")
    t.begin_fill()
    t.pendown()
    t.circle(50, 60)
    t.setheading(-120)
    t.circle(-100, 15)
    t.circle(-15, 90)
    t.circle(-100, 15)
    t.end_fill()
    # 四肢—左臂
    t.penup()
    t.goto(-175, 100)
    t.fillcolor("black")
    t.begin_fill()
    t.setheading(-120)
    t.pendown()
    t.fd(100)
    t.setheading(-110)
    t.circle(20, 180)
    t.fd(30)
    t.circle(-5, 160)
    t.end_fill()
    # 四肢—右臂
    t.penup()
    t.goto(85, 100)
    t.setheading(60)
    t.begin_fill()
    t.pendown()
    t.fd(100)
    t.setheading(70)
    t.circle(20, 180)
    t.fd(30)
    t.circle(-5, 160)
    t.end_fill()
    # 小红心装饰
    t.penup()
    t.pencolor("red")
    t.fillcolor('red')
    t.goto(105, 200)
    t.begin_fill()
    t.pendown()
    t.circle(-5, 180)
    t.setheading(90)
    t.circle(-5, 180)
    t.setheading(-120)
    t.fd(17)
    t.penup()
    t.goto(105, 200)
    t.pendown()
    t.setheading(-60)
    t.fd(17)
    t.end_fill()
    t.pencolor("black")
    t.fillcolor("black")
    # 四肢—左腿
    t.penup()
    t.goto(-120, -45)
    t.begin_fill()
    t.pendown()
    t.setheading(-90)
    t.circle(-140, 20)
    t.circle(5, 109)
    t.fd(30)
    t.circle(10, 120)
    t.setheading(90)
    t.circle(-140, 10)
    t.end_fill()
    # 四肢—右腿
    t.penup()
    t.goto(30, -45)
    t.begin_fill()
    t.pendown()
    t.setheading(-90)
    t.circle(140, 20)
    t.circle(-5, 109)
    t.fd(30)
    t.circle(-10, 120)
    t.setheading(90)
    t.circle(140, 10)
    t.end_fill()
    # 冰糖外壳
    t.pensize(3)
    t.penup()
    t.goto(-160, 195)
    t.setheading(160)
    t.pendown()
    t.circle(-40, 230)
    t.setheading(30)
    t.circle(-134, 58)
    t.setheading(60)
    t.circle(-40, 215)
    t.setheading(-60)
    t.fd(15)
    t.circle(2, 200)
    t.setheading(65)
    t.fd(30)
    t.circle(-25, 180)
    t.fd(100)
    t.circle(2, 25)
    t.circle(-200, 47)
    t.circle(2, 60)
    t.circle(140, 23)
    t.circle(-2, 90)
    t.setheading(180)
    t.fd(70)
    t.circle(-2, 90)
    t.fd(30)
    t.setheading(-160)
    t.circle(-100, 35)
    t.setheading(-90)
    t.fd(30)
    t.circle(-2, 90)
    t.fd(70)
    t.circle(-2, 90)
    t.setheading(60)
    t.circle(140, 30)
    t.circle(2, 45)
    t.circle(-200, 19)
    t.circle(2, 130)
    t.fd(30)
    t.circle(-25, 180)
    t.fd(100)
    t.setheading(90)
    t.circle(-200, 30)
    # 冰糖面罩（多彩边框）
    t.speed(1)
    t.delay(0)
    t.pensize(3)
    t.penup()
    t.goto(65, 120)
    t.setheading(90)
    t.pendown()
    t.pencolor("red")
    a_val = 1
    for i in range(120):
        if 0 <= i < 30 or 60 <= i < 90:
            a_val += 0.25
            t.lt(3)
            t.fd(a_val)
        else:
            a_val -= 0.25
            t.lt(3)
            t.fd(a_val)
    t.pencolor("orange")
    t.penup()
    t.goto(66, 120)
    t.pendown()
    a_val = 1
    for i in range(120):
        if 0 <= i < 30 or 60 <= i < 90:
            a_val += 0.255
            t.lt(3)
            t.fd(a_val)
        else:
            a_val -= 0.255
            t.lt(3)
            t.fd(a_val)
    t.pencolor("green")
    t.penup()
    t.goto(67, 120)
    t.pendown()
    a_val = 1
    for i in range(120):
        if 0 <= i < 30 or 60 <= i < 90:
            a_val += 0.2555
            t.lt(3)
            t.fd(a_val)
        else:
            a_val -= 0.2555
            t.lt(3)
            t.fd(a_val)
    t.pencolor("deep sky blue")
    t.penup()
    t.goto(68, 120)
    t.pendown()
    a_val = 1
    for i in range(120):
        if 0 <= i < 30 or 60 <= i < 90:
            a_val += 0.25955
            t.lt(3)
            t.fd(a_val)
        else:
            a_val -= 0.25955
            t.lt(3)
            t.fd(a_val)
    t.pencolor("pink")
    t.penup()
    t.goto(71, 120)
    t.pendown()
    a_val = 1
    for i in range(120):
        if 0 <= i < 30 or 60 <= i < 90:
            a_val += 0.26
            t.lt(3)
            t.fd(a_val)
        else:
            a_val -= 0.26
            t.lt(3)
            t.fd(a_val)
    t.pencolor("purple")
    t.penup()
    t.goto(72, 120)
    t.pendown()
    a_val = 1
    for i in range(120):
        if 0 <= i < 30 or 60 <= i < 90:
            a_val += 0.269
            t.lt(3)
            t.fd(a_val)
        else:
            a_val -= 0.269
            t.lt(3)
            t.fd(a_val)
    # 五环装饰
    t.penup()
    t.goto(-55, -10)
    t.pendown()
    t.pencolor("blue")
    t.circle(10)
    t.penup()
    t.goto(-40, -10)
    t.pendown()
    t.pencolor("black")
    t.circle(10)
    t.penup()
    t.goto(-25, -10)
    t.pendown()
    t.pencolor("red")
    t.circle(10)
    t.penup()
    t.goto(-50, -20)
    t.pendown()
    t.pencolor("yellow")
    t.circle(10)
    t.penup()
    t.goto(-30, -20)
    t.pendown()
    t.pencolor("green")
    t.circle(10)

# ------------------------------
# 蛋糕绘制函数
# ------------------------------
def draw_birthday_cake():
    """绘制生日蛋糕，分层绘制并添加装饰"""
    # 内部辅助函数：根据椭圆公式计算坐标
    def drawx(a, angle):
        return a * m.cos(m.radians(angle))
    def drawy(b, angle):
        return b * m.sin(m.radians(angle))
    
    # 设置蛋糕背景
    t.bgcolor("#d3dae8")
    t.speed(10)
    t.pensize(1)
    t.penup()
    t.goto(150, 0)
    t.pendown()
    
    # 第1层：基本椭圆形
    t.pencolor("white")
    t.begin_fill()
    for i in range(360):
        x = drawx(150, i)
        y = drawy(60, i)
        t.goto(x, y)
    t.fillcolor("#fef5f7")
    t.end_fill()
    
    # 第2层
    t.begin_fill()
    for i in range(180):
        x = drawx(150, -i)
        y = drawy(70, -i)
        t.goto(x, y)
    for i in range(180, 360):
        x = drawx(150, i)
        y = drawy(60, i)
        t.goto(x, y)
    t.fillcolor("#f2d7dd")
    t.end_fill()
    
    # 第3层
    t.penup()
    t.goto(120, 0)
    t.pendown()
    t.begin_fill()
    for i in range(360):
        x = drawx(120, i)
        y = drawy(48, i)
        t.goto(x, y)
    t.fillcolor("#cbd9f9")
    t.end_fill()
    
    # 第4层
    t.begin_fill()
    t.pencolor("#fee48c")
    for i in range(540):
        x = drawx(120, i)
        y = drawy(48, i) + 70
        t.goto(x, y)
    t.goto(-120, 0)
    t.fillcolor("#cbd9f9")
    t.end_fill()
    
    # 第5层
    t.penup()
    t.goto(120, 70)
    t.pendown()
    t.pencolor("#fff0f3")
    t.begin_fill()
    for i in range(360):
        x = drawx(120, i)
        y = drawy(48, i) + 70
        t.goto(x, y)
    t.fillcolor("#fff0f3")
    t.end_fill()
    
    # 第6层
    t.penup()
    t.goto(110, 70)
    t.pendown()
    t.pencolor("#fff9fb")
    t.begin_fill()
    for i in range(360):
        x = drawx(110, i)
        y = drawy(44, i) + 70
        t.goto(x, y)
    t.fillcolor("#fff9fb")
    t.end_fill()
    
    # 第7层
    t.penup()
    t.goto(120, 0)
    t.pendown()
    t.begin_fill()
    t.pencolor("#ffa79d")
    for i in range(180):
        x = drawx(120, -i)
        y = drawy(48, -i) + 10
        t.goto(x, y)
    t.goto(-120, 0)
    for i in range(180, 360):
        x = drawx(120, i)
        y = drawy(48, i)
        t.goto(x, y)
    t.fillcolor("#ffa79d")
    t.end_fill()
    
    # 第8层
    t.penup()
    t.goto(120, 70)
    t.pendown()
    t.begin_fill()
    t.pensize(4)
    t.pencolor("#fff0f3")
    for i in range(1800):
        x = drawx(120, 0.1 * i)
        y = drawy(-18, i) + 10
        t.goto(x, y)
    t.goto(-120, 70)
    t.pensize(1)
    for i in range(180, 360):
        x = drawx(120, i)
        y = drawy(48, i) + 70
        t.goto(x, y)
    t.fillcolor("#fff0f3")
    t.end_fill()
    
    # 后续层次与左右对称部分（第9至第17层）略去部分注释，均采用类似方式绘制，
    # 此处代码与原版基本一致，仅做了函数封装以提高可读性……
    # 第9层：蜡烛区域装饰
    t.penup()
    t.goto(80, 70)
    t.pendown()
    t.begin_fill()
    t.pencolor("#6f3732")
    t.goto(80, 120)
    for i in range(180):
        x = drawx(80, i)
        y = drawy(32, i) + 120
        t.goto(x, y)
    t.goto(-80, 70)
    for i in range(180, 360):
        x = drawx(80, i)
        y = drawy(32, i) + 70
        t.goto(x, y)
    t.fillcolor("#6f3732")
    t.end_fill()
    # 第10层
    t.penup()
    t.goto(80, 120)
    t.pendown()
    t.pencolor("#ffaaa0")
    t.begin_fill()
    for i in range(360):
        x = drawx(80, i)
        y = drawy(32, i) + 120
        t.goto(x, y)
    t.fillcolor("#ffaaa0")
    t.end_fill()
    # 第11层
    t.penup()
    t.goto(70, 120)
    t.pendown()
    t.pencolor("#ffc3be")
    t.begin_fill()
    for i in range(360):
        x = drawx(70, i)
        y = drawy(28, i) + 120
        t.goto(x, y)
    t.fillcolor("#ffc3be")
    t.end_fill()
    # 第12层
    t.penup()
    t.goto(80, 120)
    t.pendown()
    t.begin_fill()
    t.pensize(3)
    t.pencolor("#ffaaa0")
    for i in range(1800):
        x = drawx(80, 0.1 * i)
        y = drawy(-12, i) + 80
        t.goto(x, y)
    t.goto(-80, 120)
    t.pensize(1)
    for i in range(180, 360):
        x = drawx(80, i)
        y = drawy(32, i) + 120
        t.goto(x, y)
    t.fillcolor("#ffaaa0")
    t.end_fill()
    # 第13层
    t.penup()
    t.goto(64, 120)
    t.pendown()
    t.pencolor("#b1c9e9")
    t.begin_fill()
    for i in range(360):
        x = drawx(4, i) + 60
        y = drawy(1, i) + 120
        t.goto(x, y)
    t.goto(64, 170)
    for i in range(540):
        x = drawx(4, i) + 60
        y = drawy(1, i) + 170
        t.goto(x, y)
    t.goto(56, 120)
    t.fillcolor("#b1c9e9")
    t.end_fill()
    t.pencolor("white")
    t.pensize(2)
    for i in range(1, 6):
        t.goto(64, 120 + 10 * i)
        t.penup()
        t.goto(56, 120 + 10 * i)
        t.pendown()
    t.penup()
    t.goto(60, 170)
    t.pendown()
    t.goto(60, 180)
    t.pensize(1)
    t.penup()
    t.goto(64, 190)
    t.pendown()
    t.pencolor("#f1add1")
    t.begin_fill()
    for i in range(360):
        x = drawx(4, i) + 60
        y = drawy(10, i) + 190
        t.goto(x, y)
    t.fillcolor("#f1add1")
    t.end_fill()
    # 第14层（左右对称的第13层）
    t.penup()
    t.goto(-56, 120)
    t.pendown()
    t.pencolor("#b1c9e9")
    t.begin_fill()
    for i in range(360):
        x = drawx(4, i) - 60
        y = drawy(1, i) + 120
        t.goto(x, y)
    t.goto(-56, 170)
    for i in range(540):
        x = drawx(4, i) - 60
        y = drawy(1, i) + 170
        t.goto(x, y)
    t.goto(-64, 120)
    t.fillcolor("#b1c9e9")
    t.end_fill()
    t.pencolor("white")
    t.pensize(2)
    for i in range(1, 6):
        t.goto(-56, 120 + 10 * i)
        t.penup()
        t.goto(-64, 120 + 10 * i)
        t.pendown()
    t.penup()
    t.goto(-60, 170)
    t.pendown()
    t.goto(-60, 180)
    t.pensize(1)
    t.penup()
    t.goto(-56, 190)
    t.pendown()
    t.pencolor("#f1add1")
    t.begin_fill()
    for i in range(360):
        x = drawx(4, i) - 60
        y = drawy(10, i) + 190
        t.goto(x, y)
    t.fillcolor("#f1add1")
    t.end_fill()
    # 第15层：中心装饰
    t.penup()
    t.goto(0, 130)
    t.pendown()
    t.pencolor("#b1c9e9")
    t.begin_fill()
    for i in range(360):
        x = drawx(4, i)
        y = drawy(1, i) + 130
        t.goto(x, y)
    t.goto(4, 180)
    for i in range(540):
        x = drawx(4, i)
        y = drawy(1, i) + 180
        t.goto(x, y)
    t.goto(-4, 130)
    t.fillcolor("#b1c9e9")
    t.end_fill()
    t.pencolor("white")
    t.pensize(2)
    for i in range(1, 6):
        t.goto(4, 130 + 10 * i)
        t.penup()
        t.goto(-4, 130 + 10 * i)
        t.pendown()
    t.penup()
    t.goto(0, 180)
    t.pendown()
    t.goto(0, 190)
    t.pensize(1)
    t.penup()
    t.goto(4, 200)
    t.pendown()
    t.pencolor("#f1add1")
    t.begin_fill()
    for i in range(360):
        x = drawx(4, i)
        y = drawy(10, i) + 200
        t.goto(x, y)
    t.fillcolor("#f1add1")
    t.end_fill()
    # 第16层
    t.penup()
    t.goto(30, 110)
    t.pendown()
    t.pencolor("#b1c9e9")
    t.begin_fill()
    for i in range(360):
        x = drawx(4, i) + 30
        y = drawy(1, i) + 110
        t.goto(x, y)
    t.goto(34, 160)
    for i in range(540):
        x = drawx(4, i) + 30
        y = drawy(1, i) + 160
        t.goto(x, y)
    t.goto(26, 110)
    t.fillcolor("#b1c9e9")
    t.end_fill()
    t.pencolor("white")
    t.pensize(2)
    for i in range(1, 6):
        t.goto(34, 110 + 10 * i)
        t.penup()
        t.goto(26, 110 + 10 * i)
        t.pendown()
    t.penup()
    t.goto(30, 160)
    t.pendown()
    t.goto(30, 170)
    t.pensize(1)
    t.penup()
    t.goto(34, 180)
    t.pendown()
    t.pencolor("#f1add1")
    t.begin_fill()
    for i in range(360):
        x = drawx(4, i) + 30
        y = drawy(10, i) + 180
        t.goto(x, y)
    t.fillcolor("#f1add1")
    t.end_fill()
    # 第17层（对称）
    t.penup()
    t.goto(-30, 110)
    t.pendown()
    t.pencolor("#b1c9e9")
    t.begin_fill()
    for i in range(360):
        x = drawx(4, i) - 30
        y = drawy(1, i) + 110
        t.goto(x, y)
    t.goto(-26, 160)
    for i in range(540):
        x = drawx(4, i) - 30
        y = drawy(1, i) + 160
        t.goto(x, y)
    t.goto(-34, 110)
    t.fillcolor("#b1c9e9")
    t.end_fill()
    t.pencolor("white")
    t.pensize(2)
    for i in range(1, 6):
        t.goto(-26, 110 + 10 * i)
        t.penup()
        t.goto(-34, 110 + 10 * i)
        t.pendown()
    t.penup()
    t.goto(-30, 160)
    t.pendown()
    t.goto(-30, 170)
    t.pensize(1)
    t.penup()
    t.goto(-26, 180)
    t.pendown()
    t.pencolor("#f1add1")
    t.begin_fill()
    for i in range(360):
        x = drawx(4, i) - 30
        y = drawy(10, i) + 180
        t.goto(x, y)
    t.fillcolor("#f1add1")
    t.end_fill()
    # 在蛋糕上添加一些随机彩点作为装饰
    colors = ["#e28cb9", "#805a8c", "#eaa989", "#6e90b7", "#b8b68f", "#e174b5", "#cf737c", "#7c8782"]
    for i in range(80):
        t.penup()
        x = r.randint(-120, 120)
        y = r.randint(-25, 30)
        t.goto(x, y)
        t.pendown()
        t.dot(r.randint(2, 5), r.choice(colors))
    for i in range(40):
        t.penup()
        x = r.randint(-90, 90)
        y = r.randint(-35, 10)
        t.goto(x, y)
        t.pendown()
        t.dot(r.randint(2, 5), r.choice(colors))
    for i in range(40):
        t.penup()
        x = r.randint(-80, 80)
        y = r.randint(60, 90)
        t.goto(x, y)
        t.pendown()
        t.dot(r.randint(2, 5), r.choice(colors))
    for i in range(30):
        t.penup()
        x = r.randint(-50, 50)
        y = r.randint(45, 70)
        t.goto(x, y)
        t.pendown()
        t.dot(r.randint(2, 5), r.choice(colors))
    for i in range(50):
        t.penup()
        x = r.randint(-500, 500)
        y = r.randint(120, 300)
        t.goto(x, y)
        t.pendown()
        t.dot(r.randint(3, 5), r.choice(colors))
    # 最后写上蛋糕文字
    t.seth(90)
    t.penup()
    t.goto(0, 0)
    t.fd(210)
    t.left(90)
    t.fd(170)
    t.pendown()
    t.write("Happy Birthday", font=("Curlz MT", 50))

# ------------------------------
# 烟花效果（额外内容）
# ------------------------------
def draw_fireworks(num_fireworks=10):
    """在屏幕上随机位置绘制简单烟花爆炸效果"""
    fireworks_colors = ["red", "yellow", "blue", "green", "purple", "orange", "pink"]
    for _ in range(num_fireworks):
        t.penup()
        x = r.randint(-300, 300)
        y = r.randint(100, 300)
        t.goto(x, y)
        t.pendown()
        color = r.choice(fireworks_colors)
        t.pencolor(color)
        # 绘制辐射线
        for angle in range(0, 360, 30):
            t.penup()
            t.goto(x, y)
            t.setheading(angle)
            t.pendown()
            t.fd(50)
        time.sleep(0.5)

# ------------------------------
# 绘制生日祝福文字
# ------------------------------
def draw_birthday_message(message="生日快乐！", pos=(0, -250), font=("Curlz MT", 60, "normal"), color="magenta"):
    t.penup()
    t.goto(pos)
    t.pendown()
    t.color(color)
    t.write(message, align="center", font=font)

# ------------------------------
# 主程序入口
# ------------------------------
def main():
    setup_canvas()
    # 绘制昵称
    t.penup()
    t.goto(-500, 250)
    msg = '杨希'  # todo 此处可以修改昵称
    for i in msg:
        t.color('green')
        t.write(i, True, align='left', font=('方正舒体', 70, 'normal'))
        time.sleep(0.3)
    # 绘制大熊形象
    draw_bear()
    # 绘制署名
    draw_signature("—小 y", pos=(450, -350))
    # 暂停3秒后清屏，准备绘制生日蛋糕
    t.clear()
    time.sleep(3)
    # 绘制生日蛋糕
    draw_birthday_cake()
    # 在蛋糕下方写上生日祝福文字
    draw_birthday_message("Happy Birthday", pos=(0, -250))
    # 增加烟花效果
    draw_fireworks(10)
    t.done()

if __name__ == '__main__':
    main()
