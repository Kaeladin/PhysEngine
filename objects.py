import time


class PointMass:
    def __init__(self, mass):
        self.m=mass


class KinematicMass(PointMass):
    def  __init__(self, mass, posx, posy, velx, vely, accx, accy):
        self.x=posx
    	self.vx=velx
    	self.ax=accx
        self.y=posy
        self.vy=vely
        self.ay=accy
	self.m=mass

    def kinematics(self):
	return (self.x, self.vx, self.ax, self.y, self.vy, self.ay)

    def display(self):
        print "Posx: %.3f, Velx: %.3f, Accx: %.3f, Posy: %.3f, Vely: %.3f, Accy: %.3f" % self.kinematics()


def main():
    ts = 0.015
    bot1 = KinematicMass(10, 5, 5, 4, 4, 1, -2)
    for j in range(5000):
        bot1.vx +=  bot1.ax * ts
        bot1.x  +=  bot1.vx * ts
        bot1.vy +=  bot1.ay * ts
        bot1.y  +=  bot1.vy * ts
        bot1.display()   
        time.sleep(ts)
main()
