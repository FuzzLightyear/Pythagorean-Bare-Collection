#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Fri Dec  4 16:57:15 2020

@author: medusa
"""
class node():
    def __init__(self, label, lchild, rchild):
        self.label=label
        self.lchild=lchild
        self.rchild=rchild
        
        
C=["C"]
Df=["BD"]
D=["D"]
Ef=["Eb"]
E=["E"]
F=["F"]
Gf=["Gb"]
G=["G"]
Af=["Ab"]
A=["A"]
Bf=["Ab"]
B=["B"]
notes=[C,Df,D,Ef,E,F,Gf,G,Af,A,Bf,B]


monad=node("C")
dyad=node("Df",monad,triad)
pentad=node("E")
Quad=node("Ef",triad,pentad)

triad=node("D",dyad,Quad)

hexad=node("F")
octad=node("G")
septad=node("Gb",hexad,octad)


twelvetad=("B")
tentad=node("A",ninetad,eleventad)
eleventad=("Bb",tentad,twelvetad)

ninetad=node("Ab",septad,eleventad)




#A->[Ab,Bb]     1 iteration/level
#Gb->[F,G]      2 iterations/levels
#Bb->[A,B]


five=


