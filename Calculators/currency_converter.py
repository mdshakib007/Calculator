class CurrencyConverter:
    def __init__(self):
        pass
        
    def bdt_to_usd(self):
    	bdt = int(input("Enter BDT amount: "))
    	usd = bdt / 106
    	return f"'{bdt}' BDT is equal to '{usd:.2f}' USD"
    	
    def usd_to_bdt(self):
    	usd = int(input("Enter USD amount: "))
    	bdt = usd * 106
    	return f"'{usd}' USD is equal to '{bdt}' BDT" 
    	

if __name__ == "__main__":
	c = CurrencyConverter()
	print(c.bdt_to_usd())
	print(c.usd_to_bdt())