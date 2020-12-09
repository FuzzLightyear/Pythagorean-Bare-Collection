#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Thu Dec  3 13:29:10 2020

@author: medusa
"""

def game2(x,y,z):
    if y-x==x:
        print("double")
    elif y-x-x==x:
        print("triple")
    elif y-x-x-x==x:
        print("quadruple")
        
    newx=x
    newy=y-x
    newz=z-x-(2*newy)
    arr=[newx,newy,newz]
    return arr
    
def game2stub(x,y,z):
    arr=[x,y,z]
    for i in range(10):
        print(arr)
        if arr[0]==arr[1]:
            break
        else:
            arr=game2(arr[0],arr[1],arr[2])