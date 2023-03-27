class Temperature:
	def __init__(self):
		pass
		
	def convert(self):
		print("        Your Temperature is___\n        1. 'Celcious'\n        2. 'Fahrenheit'\n        3. 'Kelvin'\n")
		want = input("        |")
		
		if want == "1":
			C = int(input("Enter temperature in 'Celsius': "))
			
			F = (C * 9/5) + 32
			K = C + 273.15
			
			return f"{C}°C is equal to {F:.2f}°F\n{C}°C is equal to {K:.2f}K"
		
		elif want == "2":
			F = int(input("Enter temperature in 'Fahrenheit': "))
			
			C = (F - 32) * 5/9
			K = (F - 32) * 5/9 + 373.15
			return f"{F}°F is equal to {C:.2f}°C\n{F}°F is equal to {K:.2f}K"	
		elif want == "3":
			K = int(input("Enter temperature in 'Kelvin': "))
			
			C = K - 273
			F = (K - 273.15) * 9/5 + 32
			return f"{K}K is equal to {C:.2f}°C\n{K}K is equal to {F:.2f}°F"
								
		else:
			return "Please inter temperature."
			


if __name__ == "__main__":
	t = Temperature()
	print(t.convert())
		