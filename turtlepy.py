#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sat Dec  5 14:02:47 2020

@author: medusa
"""

import turtle 
from turtle import Screen
#my_window = turtle.Screen()
#my_window.bgcolor("white")
screen = Screen()
screen.setup(1000, 1200)
my_pen=turtle.Turtle()

my_pen.forward(100)
carryx=20
px=10
x=20
for i in range(6):
    my_pen.circle(x)
    my_pen.circle(x,steps=3)
    my_pen.circle(x,steps=4)
    my_pen.circle(x,steps=5)
    x=x+px
    px=carryx
    carryx=x
    print(px,x)
turtle.done()