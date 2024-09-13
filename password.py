import random
import string
print("GENERATING PASSWORD")
length=int(input("enter length of the password:"))
password=string.ascii_letters+string.digits
print("Password:","".join(random.sample(password,length)))
