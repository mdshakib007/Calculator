class CurrencyConverter:
    """simple class to convert currency"""
    @staticmethod
    def bdt_to_usd():
        bdt = int(input("Enter amount of BDT: ৳"))
        usd = bdt / 106
        return (f"{bdt}৳ is equal to {usd:.3f}$")
    
    @staticmethod    
    def usd_to_bdt():
        usd = int(input("Enter amount of USD: $"))
        bdt = usd * 106
        return (f"{usd}$ is equal to {bdt}৳")
    
if __name__ == '__main__':
    c = CurrencyConverter()
    print(c.bdt_to_usd())
    print(c.usd_to_bdt())