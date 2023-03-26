# Conversion factors

class Distance:
	"""class for calculate distance"""
	def __init__(self):
		pass		
		
	
	def k_to_m(self):
		km = int(input("Enter kilometers: "))
		k2m = km * 0.621371
		return f"{km} km is equal to {k2m:.2f} miles."
		
	def m_to_k(self):
		m = int(input("Enter miles: "))
		m2k = m * 1.60934
		return f"{m} miles is equal to {m2k:.2f} kilometers."
				



if __name__ == "__main__":
	distance = Distance()
	print(distance.k_to_m())
	print(distance.m_to_k())