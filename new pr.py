import turtle as t
import colorsys
t.bgcolor("red")
t.tracer(10)
t.pensize(2)
h=0.5
for i in range(220):
    c=colorsys.hls_to_rgb(h,1,1)
    h=0.0008
    t.fillcolor(c)
    t.begin_fill()
    t.fd(i)
    t.lt(100)
    t.circle(20)
    for j in range(2):
        t.fd(i*j)
        t.rt(1)
        t.end_fill()