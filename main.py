#import all from subdirectory 

from dtime import Clock
from Calculators.addsub import Calc
from Calculators.currency_converter import CurrencyConverter
from Calculators.distance_converter import Distance
from Calculators.password_generator import Password
from Calculators.gravitational_force import Gravity
from Calculators.interest_rate import Interest
from Calculators.temperature_converter import Temperature
from Calculators.cal_area import Area
from Calculators.average import Average 
from Calculators.decimal_to_binary import Binary


#import structure
from structure import Structure

"""all are done.now give logic,
before that we need to create 
an instance for every class"""

c = Clock()
calc = Calc()
cc = CurrencyConverter()
dis_conv = Distance()
pass_gen = Password()
gr_force = Gravity()
intress = Interest()
temp_conv = Temperature()
cal_area = Area()
average = Average()

#create variable to head, body
head = Structure()
body = """
    What do you want____
    
    1. 'Simple Calculation'
    2. 'Convert Currency'
    3. 'Convert Distance'
    4. 'Generate Password'
    5. 'Calculate Interest'
    6. 'Calculate Temperature'
    7. 'Calculate Area'
    8. 'Calculate Average'
    9. 'Gravitational force'
    10.'Decimal to Binary'
    11.'Exit'
"""

addsub = """
    Need___
    1. 'Addition'
    2. 'Subtraction'
    3. 'Multiplication'
    4. 'Division'
    5. 'Exit'
"""

curr = """
    Need___
    1. 'BDT' to 'USD'
    2. 'USD' to 'BDT'
    3. 'Exit'
"""

km = """
    Need___
    1. 'Kilometer' to 'Mile'
    2. 'Mile' to 'Kilometer'
    3. 'Exit'
"""

cal_ar = """
    Need___
    1. 'Square'
    2. 'Circle'
    3. 'Triangle'
    4. 'Cube'
    5. 'Exit'
"""

#we shows head for first time
print(head)

#create an infinite loop
while True:
	c.clock()
	print(body)
	want = input("    |")
	
	if want == "1":
		print(addsub)
		need = input("    |")
		
		if need == "1":
			print(calc.add())
			
		elif need == "2":
			print(calc.sub())
			
		elif need == "3":
			print(calc.mul())
			
		elif need == "4":
			print(calc.div())
			
		elif need == "5":
			print("   Exiting...")
			print("    [Exited]")
			exit()
			
		else:
			print("Please enter 1,2,3,.... what you want!")
			
			
	elif want == "2":
		print(curr)
		need = input("    |")
		
		if need == "1":
			print(cc.bdt_to_usd())
			
		elif need == "2":
			print(cc.usd_to_bdt())
			
		elif need == "3":
			print("   Exiting...")
			print("    [Exited]")
			exit()
			
		else:
			print("Please enter 1,2,3,.... what you want!")
			
	
	elif want == "3":
		print(km)
		need = input("    |")
		
		if need == "1":
			print(dis_conv.k_to_m())
			
		elif need == "2":
			print(dis_conv.m_to_k())
			
		elif need == "3":
			print("   Exiting...")
			print("    [Exited]")
			exit()
			
		else:
			print("Please enter 1,2,3,.... what you want!")
			
			
			
	elif want == "4":
		print(pass_gen.gen_pass())
		
	
	elif want == "5":
		print(intress.get_interest())
		
	
	elif want == "6":
		print(temp_conv.what())
		
		
	elif want == "7":
		print(cal_ar)
		need = input("    |")
		
		if need == "1":
			print(cal_area.square())
			
		elif need == "2":
			print(cal_area.circle())
			
		elif need == "3":
			print(cal_area.triangle())
		
		elif need == "4":
			print(cal_area.cube())
			
		elif need == "5":
			print("   Exiting...")
			print("    [Exited]")
			exit()
			
		else:
			print("Please enter 1,2,3,.... what you want!")
		
	elif want == "8":
	    avg = Average.from_input()
	    print(avg.calculate()) 
			
			
	
	elif want == "9":
		print(gr_force.gravitational_force())
		
		
	
	elif want == "10":
		b = Binary()
		print(b.dec_to_binary())
		
	elif want == "11":
		print("   Exiting...")
		print("    [Exited]")
		exit()
		
	else:
		print("Please enter 1,2,3,.... what you want!")
		
