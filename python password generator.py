import string
import random

s1 = string.ascii_lowercase
# print(s1)
s2 = string.ascii_uppercase
# print(s2)
s3 = string.digits
# print(s3)
s4 = string.punctuation
# print(s4)
plen = int(input("Enter password length\n")) 
s = []
s.extend(list(s1))
s.extend(list(s2))
s.extend(list(s3))
s.extend(list(s4))

random.shuffle(s)
print("".join(random.sample(s,plen)))