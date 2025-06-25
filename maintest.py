from manipulator import Manipulator
from conv import ConveyerLine, ConveyerMuver
import time
from lamp import Lamp
angle=Manipulator("192.168.100.47", 8888,"g")
time.sleep(2)
angle.toPoint(150,20,200,0,0)


