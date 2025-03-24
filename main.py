from manipulator import Manipulator
from conv import ConveyerLine, ConveyerMuver
import time
from lamp import Lamp
angle=Manipulator("192.168.42.241", 8888)
conveyerl=ConveyerLine("192.168.42.49", 8888)
# conveyerm=ConveyerMuver("192.168.42.49", 8888)
led=Lamp("192.168.42.16", 8888)
led.setColor(g=1)
conveyerl.setSpeed(0)
# conveyerm.setPosition(2000)
