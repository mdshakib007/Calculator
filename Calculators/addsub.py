class Calc:
	"""here we just calculate add,sub,mul,div"""
	def __init__(self):
		pass
		
	def add(self):
		a = int(input("Enter 1st value: "))
		b = int(input("Enter 2nd value: "))
		sum = a+b
		return f"The sum is: {sum}"
		
	def sub(self):
		a = int(input("Enter 1st value: "))
		b = int(input("Enter 2nd value: "))
		sub = a-b
		return f"The subtract is: {sub}"
		
	def mul(self):
		a = int(input("Enter 1st value: "))
		b = int(input("Enter 2nd value: "))
		mul = a*b
		return f"The multiply is: {mul}"
		
	def div(self):
		a = int(input("Enter 1st value: "))
		b = int(input("Enter 2nd value: "))
		div = a/b
		return f"The division is: {div:.2f}"
		

#testing	
if __name__ == "__main__":
	cal = Calc()
	print(cal.add())
	print(cal.sub())
	print(cal.mul())
	print(cal.div())	