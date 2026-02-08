import turtle

t = turtle.Turtle()
ok = t.position()
t.shape("turtle")
t.color("green")
t.pencolor("blue")

#levanta a caneta e desce
t.penup()
t.right(90)
t.forward(100)

#desse a caneta e faz a porta e o chão
t.pendown()
t.left(180)
t.forward(40)
t.circle(5)
t.forward(40)
t.left(90)
t.forward(40)
t.left(90)
t.forward(80)
t.left(90)
t.forward(100)
t.left(180)
t.forward(160)

# parede da esquerda
t.right(90)
t.forward(160)

# faz o teto
t.right(90)
t.forward(160)

# faz a parede da direita
t.right(90)
t.forward(160)

# volta pro teto
t.right(180)
t.forward(160)

# começa o telhado
t.left(60)
t.forward(92)
t.left(60)
t.forward(92)

# volta pra ponta do telhado 
t.left(180)
t.forward(92)

#faz o poste
t.pencolor("black")
t.left(60)
t.left(180)

t.penup()

# ir para baixo
t.forward(290)

t.right(90)
t.forward(27)

# começa o letreiro

#faz o T
t.left(90)
t.pendown()
t.forward(30)
t.left(180)
t.forward(30)
t.left(90)
t.forward(10)
t.left(180)
t.forward(20)
t.penup()

# fas o O
t.forward(15)
t.pendown()
t.right(90)
t.forward(30)
t.left(90)
t.forward(15)
t.left(90)
t.forward(30)
t.left(90)
t.forward(15)
t.penup()

#faz o P
t.left(180)
t.forward(30)
t.pendown()
t.right(90)
t.forward(30)
t.left(180)
t.forward(30)
t.right(90)
t.forward(20)
t.right(90)
t.forward(15)
t.right(90)
t.forward(20)



#vai fazer duolingo
#ok:
t.penup()
t.forward(30)
t.right(90)
t.forward(400)


