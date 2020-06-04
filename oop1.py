class Vehicle():
    positionX = 1
    positionY = 1 
    speed = 100 
    isOn = False
    def __init__(self, color_, engine_, numofWheels_):
        self.color = color_
        self.engine = engine_
        self.numofWheels = numofWheels_

    def accelerate(self):
        self.isOn = True
        if self.isOn==True:
            self.speed+=1
        else:
            print('ise sal')
    
    def moveForward(self,x,y):
        self.positionX+=x
        self.positionY+=y

    def moveBackwards(self, x, y):
        self.positionX -= x
        self.positionY -= y
    
    def ignition(self):
        if self.isOn==True:
            self.isOn=False
        else:
            self.isOn=True
    
    def getNumofWheels(self):
        return self.numofWheels

    def setNumofWheels(self, num):
        self.numofWheels = num

    def getColor(self):
        return self.color 

    def setColor(self,colorr):
        self.color= colorr 

    def __str__(self):
        return f'{self.color},{self.engine},{self.numofWheels}'
