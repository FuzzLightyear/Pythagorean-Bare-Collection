# -*- coding: utf-8 -*-

#import turtlepy
import game1 
import game2
#import musicratioimproved

def main():
    print("Coding Inspired By 'Theoretic Arithmetic' by Thomas Taylor")
    print("Input 1 for getting the tuple valies of input n")
    print("Type 2 for inputting sequence such that [x,y,z] z is y * y")
    print("Type 3 for Tetractys inspired turtle patterns")
    print("Type 4 for cooler Tetractys inspired turtle patterns")

    promptans = int(input())
    if promptans == 1:
        print("Innput n")
        n=int(input())
        game1.game1stub(n)
    elif promptans == 2:
        print("Innput x y and z")
        x=int(input())
        y=int(input())
        z=int(input())
        game2.game2stub(x,y,z)
    elif promptans == 3:
        import turtlepy
    elif promptans == 4:
        import musicratioimproved

        

if __name__ == "__main__":
    main()