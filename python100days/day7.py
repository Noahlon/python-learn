import random
import string

ALL_CHARACTERS = string.ascii_letters + string.digits 

def generate_random_string(length):
    """Generate a random string of fixed length """
    return ''.join(random.choice(ALL_CHARACTERS) for _ in range(length))    
print(ALL_CHARACTERS)
print(generate_random_string(10))