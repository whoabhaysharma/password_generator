import string
import random
def password_generator(size):
    password = []
    while len(password) < size:
        a = random.choice(list(string.ascii_uppercase))
        b = random.choice(list(string.ascii_lowercase))
        c = random.choice(list(string.punctuation))
        d = random.choice(list(string.digits))
        val = random.choice([a,b,c,d])
        password.append(val)
    print("".join(password))
    
password_generator(5)
