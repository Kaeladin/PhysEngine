class PointMass:
	def __init__(self, mass):
		self.m=mass
		
class KinematicMass(PointMass):
	def  __init__(self, mass, posx, posy, velx, vely, accx, accy):
		self.x=posx
		self.vx=velx
		self.ax=accx
		self.m=mass
def main():
	bot1=KinematicMass(10, 5, 5, 4, 4, 0, -2);
	print bot1.m
main()
