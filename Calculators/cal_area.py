import math

class Area:
	def __init__(self):
		pass
		
	@staticmethod #not necessary yet
	def square():
		a = int(input("Enter a value: "))
		sq = a*a
		return f"The square is: {sq}"		
	
	@staticmethod	
	def circle():
		r = int(input("Enter radious: "))
		c = math.pi * r * r
		return f"The area of circle is: {c:.2f}"
	
	@staticmethod	
	def triangle():
		a = int(input("Enter base: "))
		b = int(input("Enter height: "))
		tr = 0.5 * a * b
		return f"Area of Triangle: {tr}"
	
	@staticmethod	
	def cube():
		a = int(input("Enter a value: "))
		cu = a*a*a
		return f"The cube is: {cu}"
		

if __name__ == "__main__":
	ar = Area()
	print(ar.triangle())
	
	