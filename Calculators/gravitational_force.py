class Gravity:	
	@staticmethod
	def gravitational_force():
		mass1 = float(input("First mass: "))
		mass2 = float(input("Second mass: "))
		r = float(input("Distance between the objects: "))
 
		G = 6.673*(10**-11)
		force =(G*mass1*mass2)/(r**2)
 
		return f"The gravitational force is: '{force}' N"


if __name__ == "__main__":
	g = Gravity()
	print(g.gravitational_force())