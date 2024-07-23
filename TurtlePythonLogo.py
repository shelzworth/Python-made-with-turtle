from turtle import*

#snake1
screensize(1000,800)
speed(0)
pensize(6)
penup()
color('gold1')
fillcolor('gold1')
pendown()
begin_fill()
setheading(180)
circle(50,90)
forward(50)
circle(70,90)
forward(50)
circle(50,90)
forward(30)
left(90)
forward(80)
right(90)
forward(10)
right(90)
forward(120)
circle(70,90)
forward(60)
circle(50,90)
forward(30)
left(90)
forward(50)
setheading(90)
circle(50,-90)
setheading(180)
forward(100)
end_fill()
penup()

#snake2
color('dodgerblue3')
fillcolor('dodgerblue3')
setheading(90)
forward(20)
begin_fill()
left(90)
pendown()
forward(10)
circle(60,90)
forward(35)
right(90)
forward(30)
setheading(0)
circle(50,-90)
setheading(90)
forward(60)
setheading(270)
circle(70,-90)
setheading(0)
forward(120)
left(90)
forward(10)
left(90)
forward(80)
right(90)
forward(30)
setheading(270)
circle(50,-90)
setheading(0)
forward(70)
setheading(180)
circle(50,-90)
setheading(270)
forward(80)
setheading(90)
circle(45,-90)
setheading(180)
forward(100)
end_fill()
penup()

#eyes
goto(0,0)
color('white')
fillcolor('white')
setheading(90)
forward(140)
setheading(0)
pendown()
begin_fill()
circle(15,360)
end_fill()
penup()


goto(0,0)
setheading(270)
forward(140)
setheading(0)
forward(80)
pendown()
begin_fill()
circle(15,360)
end_fill()
penup()

#words
goto(0,0)
setheading(270)
forward(300)
setheading(180)
forward(160)
color('grey')
write('python',font=('FluxRegular',90,))
setheading(90)
forward(100)
setheading(0)
forward(360)
write('TM',font=('FluxRegular',15,))
hideturtle()
input('Press ENTER to exit')




























