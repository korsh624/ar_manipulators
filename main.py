from manipulator import Manipulator
from conv import Conveyer
import time
from lamp import Lamp
angle=Manipulator("192.168.42.241", 8888)
conveyer=Conveyer("192.168.42.49", 8888)
led=Lamp("192.168.42.16", 8888)
led.setColor(g=1)
