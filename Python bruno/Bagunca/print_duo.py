import turtle

t = turtle.Turtle()
enemy = turtle.Turtle()


t.shape("turtle")
t.color("green")
enemy.shape("circle")
enemy.color("red")
enemy.penup()
enemy.goto(100, 0)
t.right(15)
t.forward(100)

if t.distance(enemy) < 10:
    print("Tartaruga encontrou o inimigo!")
    
else:
    print("A tartaruga não encontrou o inimigo")
    
    
print(".___. \n{O,O}\n|)__)\n-'--'-")