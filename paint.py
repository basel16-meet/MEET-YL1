#There are two programs(both are paint,but the second one has more things to do in it tan the first one) 
#And thanks ;)
#1)
import turtle
from turtle import turtle

turtle.speed(100)
turtle.hideturtle()

color="red"
shape="circle"

def change_color():

  global color

  if color=="red"
    color="blue"
  if color=="blue"
    color="red"

def circle():
  global color
  turtle.begin_fill()
  turtle.fillcolor(color)
  turtle.circle(5)
  turtle.end_fill()

def square():

  global color

  turtle.forward(5)
  turtle.right(90)
  turtle.forward(5)
  turtle.right(90)
  turtle.forward(5)
  turtle.right(90)
  turtle.forward(5)
  turtle.right(90)

def change_shape():
  
  global shape

  if shape=="circle"
    shape="square"
  if shape=="square"
    shape="circle"

def make_shape():

  global shape

  if shape=="circle"
    turtle.circle()
  if shape=="square"
    turtle.square()

def clear():
  turtle.clear()

turtle.getscreen().onkeypress(change_color,"c")
turtle.getscreen().onkeypress(change_shape,"s")
turtle.onscreenclick(make_shape,btn-"1",add=True)
turtle.getscreen().onkeypress(clear,"e")  

turtle.turtle.getscreen().listen()
turtle.mainloop()

####
#2)
import turtle
from turtle import turtle

turtle.speed(100)
turtle,hideturtle()


color_list = ["red","blue","green","yellow","black","white","brown","orange","pink","purple","gray"]
shape_list = ["circle","square","triangle","widh_square","height_square","star_4","star_5","nothing"]
size = 1

chs = 0
cc = 0
cs = 0

color="red"

def hide/see_turtle():
 
  chs = chs + 1

  if chs == 0
    turtle.hideturtle()
  elif chs == 1
    turtle.showsturtle()
    chs = chs - 2
  else  
    chs =0
    turtle.hideturtle()

def size_big():

  global size

  size = size+1
  if size > 10
    size = 10

def size_smaller():

  global size

  size=size=1
  if size < 0
    size = 0

def change_color():

  global color

  color = color_list[cc]
  cc = cc+1
  if cc >= len(color_list)
    cc=0

def circle():
  
  global color
  global size
  
  turtle.begin_fill()
  turtle.fillcolor(color)
  
  turtle.circle(5*size)

  turtle.end_fill()

def square():
  global size
  global color

  turtle.begin_fill()
  turtle.fillcolor(color)
  
  turtle.forward(5 * size)
  turtle.right(90)
  turtle.forward(5 * size)
  turtle.right(90)
  turtle.forward(5 * size )
  turtle.right(90)
  turtle.forward(5*  size)
  turtle.right(90)

  turtle.end_fill()

def triangle():
  
  global size
  global color

  turtle.begin_turtle()
  turtle.fillcolor(color)
  
  turtle.right(30)
  turtle.forward(5 * size)
  turtle.right(120)
  turtle.forwrad(5 * size)
  turtle.right(120)
  turtle.forward(5 * size)
  turtle.right(120)

  turtle.end_fill()

def width_square():

  global color
  global size
  
  turtle.begin_fill()
  turtle.fillcolor(color)

  turtle.penup()
  turtle.forwrad(1.25)
  turtle.pendown()
  turtle.forward(2.5)
  turtle.right(90)
  turtle.forward(5)
  turtle.right(90)
  turtle.forward(2.5)
  turtle.right(90)
  turtle.foward(5)
  turtle.right(90)

  turtle.end_fill()

def height_square():
  
  global size 
  global color
  
  turtle.begin_fill()
  turtle.fillcolor(color)

  turtle.penup()
  turtle.right(90
  turtle.forward(1.25 * size)
  turtle.left(90)
  turtle.pendown()
  turtle.forward(5 * size)
  turtle.right(90)
  turtle.forward(2.5 * size)
  turtle.right(90)
  turtle.forward(5 * size)
  turtle.right(90)
  turtle.forward(2.5)
  turtle.right(90)

  turtle.end_fill()

def star_4():
  
  global size
  global color

  turtle.penup()
  turtle.right(90)
  turtle.forward(2)
  turtle.left(60)
  tirtle.pendown()
  
  turtle.begin_fill()
  turtle.fillcolor(color)
  
  turtle.forward(2.25 * size)
  turtle.right(30)
  turtle.forward(2.25 * size)
  turtle.left(120)
  turtle.forward(2.25 * size)
  turtle.right(30)
  turtle.forward(2.25 * size)
  turtle.left(120)
  turtle.forward(2.25 * size)
  turtle.right(30)
  turtle.forward(2.25 * size)
  turtle.left(120)
  turtle.forward(2.25 * size)
  turtle.right(30)
  turtle.forward(2.25 * size)
  turtle.left(120)

  turtle.end_fill()

def star_5():
  
  global size
  global color

  turtle.penup()
  turtle.tight(9)
  turtle.forward(2)
  turtle.left(60)
  turtle.pendown()
  
  turtle.begin_fill()
  turtle.colorfill(color)
  
  turtle.forward(2 * size)
  turtle.right(120)
  turtle.forward(2 * size)
  turtle.left(120)
  turtle.forward(2)
  turtle.right(30)
  turtle.forward(2)
  turtle.left(120)
  turtle.forward(2 * size)
  turtle.right(30)
  turtle.forward(2 * size)
  turtle.left(120)
  turtle.forward(2 * size)
  turtle.right(30)
  turtle.forward(2 * size)
  turtle.left(120)
  turtle.forward(2 * size)
  turtle.right(30)
  turtle.left(120)

  turtle.end_fill()
def change_shape():

  global shape

  shape = shape_list[cs]
  cs = cs + 1
  if cs >= len(shape_list)
    cs = 0 



def make_shape():
  
  global shape
  
  if shape == "circle"
    turtle.circle()
  elif shape == "square"
    turtler.square()
  elif shape == "triangle"
    turtle.triangle
  elif shape == "square_width"
    turtle.square_width()
  elif shape== "square_height"
    turtle.square_height()
  elif shape=="star_4"
    turtle.star_4()
  elif shape=="star_5"
    turtle.star_5()
  elif shape == "nothing"
  else  print "error"

  

turtle.getscreen().onkeypress(hide/see_turtle(),"v")
turtle.getscreen().onkeypress(size_big(),"add")
turtle.getscreen().onkeypress(size_small(),"minus")
turtle.getscreen().onkeypress(change_color,"c")
turtle.getscreen().onkeypress(change_shape,"s")
turtle.onscreenclick(make_shape(),btn = 1,add = True)
turtle.ondrag(make_shape(),btn = 1,add = True)

turtle.getscreen().listen()
turtle.mainloop()