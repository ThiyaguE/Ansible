#!/usr/bin/python

class Point():
    #This is python constructor - this invokes automatically
    #when an object of point is created

    #self represent current object(this)
    def __init__(self):
        print ('constructor got invoked...')
        self.x = 0
        self.y = 0
    def setValues(self, x,y):
        self.x = x
        self.y = y

    def printValues(self):
        print ('Value of x is ',self.x)
        print ('Value of y is ',self.y)

def main():
    point1 = Point();
    point1.setValues (10,20);
    point1.printValues();

    point2 = Point();
    point2.setValues (30,40);
    point2.printValues();

main()
