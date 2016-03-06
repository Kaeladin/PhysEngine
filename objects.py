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
	return (self.x, self.y, self.vx, self.vy, self.ax, self.ay)

    def display(self):
        print "Posx: %.3f, Posy: %.3f, Velx: %.3f, Vely: %.3f, Accx: %.3f, Accy: %.3f" % self.kinematics()


class Robot(KinematicMass):
    def push(self, x, y):
        self.ax+=x/self.m
        self.ay+=y/self.m


def main():
    ts = 0.015
    bot1 = Robot(10, 5, 5, 4, 4, 1, -2)

    xmax=100
    ymax=100
    xmin=0
    ymin=0

    for j in range(5000):
        if j%500==0:
            bot1.push(j,-j)

        bot1.vx +=  bot1.ax * ts
        bot1.x  +=  bot1.vx * ts
        bot1.vy +=  bot1.ay * ts
        bot1.y  +=  bot1.vy * ts
        
        if(bot1.x < xmin) or (bot1.x > xmax):
            bot1.vx = bot1.vx * -0.9
        if(bot1.y < ymin) or (bot1.y > ymax):
            bot1.vy = bot1.vy * -0.9
        bot1.display()   
        time.sleep(ts)
main()
