from manipulator import Manipulator
from conv import ConveyerLine, ConveyerMuver
import time
from lamp import Lamp
angle1=Manipulator("192.168.10.11", 8888,"g")
angle2=Manipulator("192.168.10.12", 8888,"g")
pp1=Manipulator("192.168.10.13", 8888,"p")
angle3=Manipulator("192.168.10.14", 8888,"g")
pp2=Manipulator("192.168.10.15", 8888,"p")
angle4=Manipulator("192.168.10.16", 8888,"g")
time.sleep(2)
while True:
    angle1.toPoint(200,20,200,180,0)
    angle2.toPoint(200,20,200,180,0)
    pp1.toPoint(200,20,200,0,0)
    angle3.toPoint(200,20,200,180,0)
    pp2.toPoint(200,20,200,0,0)
    angle4.toPoint(200,20,200,180,0)
    time.sleep(2)
    angle1.toPoint(200,100,150,180,1)
    angle2.toPoint(200,100,150,180,1)
    pp1.toPoint(200,100,200,0,0)
    angle3.toPoint(200,100,150,180,1)
    pp2.toPoint(200,100,200,0,0)
    angle4.toPoint(200,100,150,180,1)
    time.sleep(2)
    input()



