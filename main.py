from manipulator import Manipulator
from lamp import Lamp


angle=Manipulator("192.168.42.241", 8888)
led=Lamp("192.168.42.15", 8888)

led.setColor(g=1)
angle.toPoint(200, 0, 180, 0, 1)
led.setColor(r=1)