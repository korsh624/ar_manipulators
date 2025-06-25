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
pp1.toPoint(200,150,200,1,0)
    



