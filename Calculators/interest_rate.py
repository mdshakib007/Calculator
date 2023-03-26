class Interest:
	"""compound interest rate"""
	def __init__(self):
		pass
		
		
	def get_interest(self):
		#user input
		principle = int(input("Money of Borrowed: "))
		rate = int(input("Interest rate: "))
		time = int(input("Overall duration: "))
		
		interest = principle * ((1 + rate / 100) ** time)
		
		return f"The total amount is: ${interest:.2f}"
		


if __name__ == "__main__":
	#process input
	total_due = Interest()
	print(total_due.get_interest())
