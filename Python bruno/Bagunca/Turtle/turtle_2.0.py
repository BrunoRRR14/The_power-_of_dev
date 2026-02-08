import turtle
import keyboard
import threading
import time

t = turtle.Turtle()

def escutar_teclas():
    while True:
        if keyboard.is_pressed("up"):
            t.forward(10)
        elif keyboard.is_pressed("down"):
            t.backward(10)
        elif keyboard.is_pressed("left"):
            t.left(5)
        elif keyboard.is_pressed("right"):
            t.right(5)
        time.sleep(0.05)

threading.Thread(target=escutar_teclas, daemon=True).start()


turtle.done()