#if you want to contribute this project, or think need any improvement, please 'Fork' the repository!
#import all module we need
import time #just need to get every output 1s delay
import math #to get factorial
from dtime import Clock #to get clock
from structure import Structure #this is initial style

#import files from subdirectory 
from Calculators.addsub import Calc #to calculate the simple calculation (add,sub,mul,div)
from Calculators.currency_converter import CurrencyConverter
from Calculators.distance_converter import Distance
from Calculators.password_generator import Password
from Calculators.temperature_converter import Temperature
from Calculators.cal_area import Area
from Calculators.gravitational_force import Gravity
from Calculators.average import Average 
from Calculators.interest_rate import Interest
from Calculators.decimal_to_binary import Binary


#now create instances of imported all files
clock = Clock() #instance of Clock class
s = Structure() #instance of Structure class
#all executiable body
head = s.head() #this is initial head
body1 = s.body1() 
body2 = s.body2()
one = s.addsub()
two = s.curr()
three = s.km()
four = s.cal_arr()

#all calculation's instance
addsub = Calc() 
currency_converter = CurrencyConverter()
distance_converter = Distance()
pass_gen = Password()
grav_force = Gravity()
interest_rate = Interest()
temp_conv = Temperature()
calc_area = Area()
avg = Average()
dec_to_binary = Binary()


print(head) #we cannot want to print head everytime
time.sleep(1) #initial sleep 
while True:
    time.sleep(1) #just because ue take a break, after every calculation. 
    print(body1)
    need = input("        |")
    
    if need == '1':
        print(one)
        want = input("        |")
        if want == '1':
            try:
                print(addsub.add())
            except Exception as e:
                print("Invalid input! Please enter number.")
                
        elif want == '2':
            try:
                print(addsub.sub())
            except Exception as e:
                print("Invalid input! Please enter number.")
                
        elif want == '3':
            try:
                print(addsub.mul())
            except Exception as e:
                print("Invalid input! Please enter number.")
                
        elif want == '4':
            try:
                print(addsub.div())
            except Exception as e:
                print("Invalid input! Please enter number.")
                
        elif want == '5':
            print(' Exiting...')
            time.sleep(1)
            print('       [Exited]')
            exit()
            
        else:
            print("Invalid input! Please enter number.")
            
    elif need == '2':
        print(two)
        want = input("        |")
        if want == '1':
            try:
                print(currency_converter.bdt_to_usd())
            except Exception as e:
                print("Invalid input! Please enter amount.")
                
        elif want == '2':
            try:
                print(currency_converter.usd_to_bdt())
            except Exception as e:
                print("Invalid input! Please enter amount.")
            
        elif want == '3':
            print(' Exiting...')
            time.sleep(1)
            print('       [Exited]')
            exit()
            
        else:
            print("Invalid input! Please enter number.")
            
    elif need == '3':
        print(three)
        want = input("        |")
        
        if want == '1':
            try:
                print(distance_converter.k_to_m())
            except:
                print("Invalid input! Please enter distance.")
                
        elif want == '2':
            try:
                print(distance_converter.m_to_k())
            except:
                print("Invalid input! Please enter distance.")
                
        elif want == '3':
            print(' Exiting...')
            time.sleep(1)
            print('       [Exited]')
            exit()
            
        else:
            print("Invalid input! Please enter number.")
            
    elif need == '4':
        try:
            print(pass_gen.gen_pass())
        except:
            print("Invalid input! Please enter the length of password.")
            
    elif need == '5':
        try:
            print(interest_rate.get_interest())
        except:
            print("Invalid input! Please enter number.")
            
    elif need == '6':
        print('\n   Please wait...')
        time.sleep(1)
        print(body2)
        want = input("        |")
        
        if want == '1':
            try:
                print(temp_conv.convert())
            except:
                print("Invalid input! Please enter temperature.")
                
        elif want == '2':
            print(four)
            what = input("        |")
            
            if what == '1':
                try:
                    print(calc_area.square())
                except:
                    print("Invalid input! Please enter number.")
            
            elif what == '2':
                try:
                    print(calc_area.circle())
                except:
                    print("Invalid input! Please enter number.")
                    
            elif what == '3':
                try:
                    print(calc_area.triangle())
                except:
                    print("Invalid input! Please enter number.")
                    
            elif what == '4':
                try:
                    print(calc_area.cube())
                except:
                    print("Invalid input! Please enter number.")
                    
            elif what == '5':
                print(' Exiting...')
                time.sleep(1)
                print('       [Exited]')
                exit()
                    
        elif want == '3':
            try:
                avg = avg.from_input()
                print(avg.calculate())
            except:
                print("Invalid input! Please enter a number of list.")
                
        elif want == '4':
            try:
                print(grav_force.gravitational_force())
            except:
                print("Invalid input!")
                
        elif want == '5':
            try:
                print(dec_to_binary.dec_to_binary())
            except:
                print("Invalid input! Please enter decimal number.")
                
        elif want == '6':
            try:
                num = int(input('Enter a number: '))
                fact = math.factorial(num)
                print(f"The factorial is: {fact}")
            except:
                print("Invalid input! Please enter valid number.")
                
        elif want == '7':
                print(' Exiting...')
                time.sleep(1)
                print('       [Exited]')
                exit()
                
        else:
            print("Invalid input!")
            
    elif need == '7':
                print(' Exiting...')
                time.sleep(1)
                print('       [Exited]')
                exit()
    
    else:
            print("Invalid input!")
            
print("if you want to contribute this project, or think need any improvement, please 'Fork' the repository!")