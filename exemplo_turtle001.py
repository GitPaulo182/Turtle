import turtle

colors = ["blue", "orange", "red",  "cyan",  "#ff05ca",  "yellow",  'purple', 'green', 'grey', "white",  "black"]

bob = turtle.Turtle()
turtle.bgcolor(colors[10])

bob.speed(15)
bob.pensize(10)

bob.penup()
bob.setpos(270, 0)
bob.pendown()

# Cria um polígono 
def polygon(t, n, length):
    bob.pencolor(colors[0])
    angle = 360 / n
    for i in range(n):
        t.fd(length)
        t.lt(angle)
polygon (bob, n=8, length=85)

bob.penup()
bob.setpos(200, 0)
bob.pendown()

# Cria um quadrado
for i in range(4):
    bob.pencolor(colors[1])
    bob.fd(-200)
    bob.lt(-90)

bob.penup()
bob.fd(-100)
bob.lt(90)

# Cria 2 linhas retas em 90 graus
bob.pencolor(colors[2])
bob.pendown()
bob.fd(100)
bob.lt(90)
bob.fd(135)
bob.lt(90)

bob.penup()
bob.home()

# Cria um círculo incompleto
bob.pendown()        
bob.pencolor(colors[3])
bob.circle(100, 240)

bob.penup()
bob.setpos(-40, 100)

# Cria um losango
bob.pencolor(colors[4])
bob.pendown()
bob.setpos (-140, 200)
bob.setpos(-240, 100)
bob.setpos(-140, 0)
bob.setpos (-40, 100)

bob.speed(100)
bob.penup()
bob.home()
bob.setpos(-140, 100)

# Cria 2 círculos (um acima do outro)
bob.speed(15)
bob.pencolor(colors[5])
bob.pendown()
bob.circle(25, 360)
bob.circle(-25, 360)

bob.penup()
bob.setpos(-350, 100)
bob.pendown()

# Cria 6 hexágonos em 360 graus
for i in range(6):
	bob.color(colors[i%10])
	bob.circle(60, steps=6)
	bob.right(60)

bob.penup()
bob.setpos(-450, 400)
bob.pendown()

# Cria uma estrela de 7 pontas e 7 cores
for i in range(7):
    bob.pencolor(colors[i%10])
    bob.fd(200)
    bob.rt(154.1)
    
bob.penup()
bob.setpos(-165, 440)
bob.pendown()

a=60
d1=60
d2=-60

# Cria uma estrela de 6 pontas preenchida
bob.fillcolor(colors[1])
bob.begin_fill()

for i in range(3):
    bob.pencolor(colors[7])
    bob.pos()
    bob.lt(a)
    bob.fd(d1)
    bob.pos()
    bob.lt(a)
    bob.fd(d2)
    bob.pos()
    bob.lt(a)
    bob.fd(d2)
    bob.pos()
    bob.lt(a)
    bob.fd(d1)
    
bob.end_fill()
 
bob.penup()
bob.setpos(0, 420)
bob.pendown()

# Cria uma estrela de 5 pontas
for i in range(5):
    bob.pencolor(colors[i%5])
    bob.fd(200)
    bob.rt(144)
    
bob.penup()
bob.setpos(300, 430)
bob.pendown()

a=45
d1=80
d2=-80

# Cria uma estrela de 4 pontas preenchida
bob.fillcolor(colors[2])
bob.begin_fill()

for i in range(3):
    bob.pencolor(colors[5])
    bob.pos()
    bob.lt(a)
    bob.fd(d1)
    bob.pos()
    bob.lt(a)
    bob.fd(d2)
    bob.pos()
    bob.lt(a)
    bob.fd(d2)
    bob.pos()
    bob.lt(a)
    bob.fd(d1)
    
bob.end_fill()

bob.penup()
bob.setpos(-350, -250)
bob.pendown()

# Cria uma figura aleatória de 2 cores
for i in range (7):
    for i in range (2):
        bob.pensize(5)
        bob.goto(-350, -240)
        bob.color(colors[2])
        bob.forward(100)
        bob.right(60)
        bob.color(colors[3])
        bob.forward(50)
        bob.right(120)
    bob.right(30)
    
bob.penup()
bob.home()
bob.setpos(100, -350)
bob.pendown()

# Escreve Turtle na tela
bob.pencolor(colors[9])
fonte = ("Comic Sans", 40, "bold")
bob.write("Turtle", False, "center", fonte)

bob.penup()
bob.setpos(-200, -350)

# Estampa várias tartarugas na tela
bob.shape("turtle")
bob.fillcolor(colors[7])
bob.pendown()
bob.speed(5)
bob.pensize(1)
x = -200
while x <= 400:
	bob.setpos(x, -350)
	bob.stamp()
	x += 100

# Cria uma tela piscante colorida
for x in range (2):
    for i in range(len(colors)):
        turtle.bgcolor(colors[i])
     

turtle.mainloop()
