#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Thu Dec  3 13:08:07 2020

@author: medusa
"""

def game1(x,y,z):
    newx=x
    newy=y+x
    newz=x+(2*y)+z
    arr=[newx,newy,newz]
    return arr

def game1stub(n):
    arr=[n,n,n]
    arr2=[n,n,n]
    print("[x=root, y=(root^1)*(index+1), z=y*(index+1)")
    for i in range(10):
        print("arr ",i,arr)
        #print("arr2",i,arr2, "get +",i,"and +",i+1)
        arr2=arr
        arr=game1(arr[0],arr[1],arr[2])
        #arr2=game1(arr2[2],arr2[1],arr[0])