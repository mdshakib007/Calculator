import string
import random

class Password:
    """class for generate pass"""
    def __init__(self):
        pass
    
    @staticmethod    
    def gen_pass():
        size = int(input('Your password length: '))
        
        all_chars = string.ascii_letters + string.digits + string.punctuation
        password = ''
        
        for char in range(size):
            rand_char = random.choice(all_chars)
            password = password + rand_char
        return f"Your Generated password: {password}"
 


if __name__ == "__main__":
	
	new_pass = Password()

	print(new_pass.gen_pass())
