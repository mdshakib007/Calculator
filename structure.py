class Structure:
    def head(self):
        msg = """
  ______________________________
 |  _______   _______   _______ |
 | |_______| |_______| |_______||
 | | +   - | | ×   ÷ | | More! ||
 | |_______| |_______| |_______||
 | if you want to contribute--  |
 | this simple project, or need |
 |      any improvement         |
 | please 'Fork' the repository |
 |______________________________|

 please wait for a moment!
        """
        
        return msg
    
    
    def body1(self):
        msg = """
        What you want to do___
        
        1. Simple Calculation
        2. Convert Currency
        3. Convert Distance
        4. Generate Password
        5. Calculate interest
        6. More
        7. Exit
        """
        return msg
    
    def body2(self):
        msg = """
        You want___
            
        1. Calculate Temperature
        2. Calculate Area
        3. Calculate Average
        4. Gravitational Force
        5. Decimal to Binary
        6. Factorial
        7. Exit
        """
        return msg
    
    def addsub(self):
        msg = """
        You want___      
        1. Addition
        2. Subtraction
        3. Multiplication
        4. Division
        5. Exit
        """
        return msg
    
    def curr(self):
        msg = """
        You want___     
        1. BDT to USD
        2. USD to BDT
        3. Exit
        """
        return msg
    
    def km(self):
        msg = """
        You want___     
        1. Kilometer to Mile
        2. Mile to Kilometer
        3. Exit
        """
        return msg
    
    def cal_arr(self):
        msg = """
        You want___           
        1. Square
        2. Circle
        3. Triangle
        4. Cube
        5. Exit
        """
        return msg
    



if __name__ == '__main__':
    s = Structure()
    print(s.head())
    print(s.body1())
    print(s.body2())
    print(s.addsub())
    print(s.curr())
    print(s.km())
    print(s.cal_arr())