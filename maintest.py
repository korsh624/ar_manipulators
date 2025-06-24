from manipulator import Manipulator
from conv import ConveyerLine, ConveyerMuver
import time
from lamp import Lamp
angle=Manipulator("192.168.100.47", 8888)
time.sleep(3)
angle.toPoint(200,0,200,180,0)
time.sleep(5)
angle.toPoint(200,50,200,0,1)
time.sleep(3)
angle.toPoint(200,0,200,180,0)
time.sleep(5)
angle.toPoint(200,50,200,0,1)

