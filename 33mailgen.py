### 33mailgen.py
### Random E-mail Generator For 33mail.com

from random import randint

def random_number(n):
    range_start = 10**(n-1)
    range_end = (10**n)-1
    return randint(range_start, range_end)

mycounter = 1
usernamelength = 12 #Change this value to increase/decrease e-mail username length.
thirtythreemail = "@username.33mail.com" #Add your @username.33mail.com address here.

while (mycounter <= 10):
    randomemail = str(random_number(usernamelength)) + thirtythreemail
    print (randomemail)
    mycounter = mycounter + 1
