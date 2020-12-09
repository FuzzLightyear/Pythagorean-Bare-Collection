#we know first of each scale together is root octave

# """ noteNames = ['C', 'D', 'E', 'F', 'G', 'A', 'B']
# noteRatios = [1, 8/9, 4/5, 3/4, 2/3, 3/5, 8/15] """
import turtle
from turtle import Screen

class note():
    def __init__(self, label, maxoct, ratio):
        self.label=label
        self.value = maxoct * ratio
    def setValue(self, value):
        self.value = value
    def getValue(self):
        return self.value
    def getLabel(self):
        return self.label
    

class octave():
    noteNames = list(['C', 'D', 'E', 'F', 'G', 'A', 'B'])
    noteRatios = list([1, 8/9, 4/5, 3/4, 2/3, 3/5, 8/15])
    def __init__(self, maxvalue):
        self.maxvalue = maxvalue
        #self.minvalue = 0
        self.c = note(octave.noteNames[0], self.maxvalue, octave.noteRatios[0])
        self.d = note(octave.noteNames[1], self.maxvalue, octave.noteRatios[1])
        self.e = note(octave.noteNames[2], self.maxvalue, octave.noteRatios[2])
        self.f = note(octave.noteNames[3], self.maxvalue, octave.noteRatios[3])
        self.g = note(octave.noteNames[4], self.maxvalue, octave.noteRatios[4])
        self.a = note(octave.noteNames[5], self.maxvalue, octave.noteRatios[5])
        self.b = note(octave.noteNames[6], self.maxvalue, octave.noteRatios[6])
        self.whole = list([self.c, self.d, self.e, self.f, self.g, self.a, self.b])
    
    def getMax(self):
        return self.maxvalue
    def printOctave(self):
        for i in range(7):
            print(self.whole[i].getLabel(), ': ', self.whole[i].getValue())
    def getValues(self):
        templist = list()
        for j in range(7):
            templist.append(self.whole[j].getValue())
        return templist

initialmax = 120 * 2.6
numoctaves = 4
octaves = list([])
maxitr = initialmax
for i in range(numoctaves):
    octaves.append(octave(maxitr))
    maxitr=maxitr/2

vals = list()
for j in range(numoctaves):
    print("Octave ",j+1,": {maximum=", octaves[j].getMax(),"}")
    octaves[j].printOctave()
    vals.append(octaves[j].getValues())
screen = Screen()
screen.setup(1000, 1200)
my_pen=turtle.Turtle()
for x in range(numoctaves):
    for y in octaves[x].getValues():
        my_pen.circle(y, steps=x+3)
        print(y)
        #print(my_pen.position())
        
my_pen.circle(64, steps=4)
        #my_pen.circle(y)
