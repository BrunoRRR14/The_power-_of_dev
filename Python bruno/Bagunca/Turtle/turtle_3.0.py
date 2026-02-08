import turtle
from time import sleep
import pyautogui as py

t = turtle.Turtle()
t.shape("turtle")
t.color("green")


for i in range(1000000):
    sleep(2)
    x,y = py.position()
    t.goto(x, y)
    sleep(2)
    
    