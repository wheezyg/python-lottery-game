print ("WELCOME TO LOTTO.COM")

import random
import time

print ("You get 8 picks\nTake your picks")


n1 = int(input("1st Pick (1-35)\n"))
n2 = int(input("2nd Pick (1-35)\n"))
n3 = int(input("3rd Pick (1-35)\n"))
n4 = int(input("4th Pick (1-35)\n"))
n5 = int(input("5th Pick (1-35)\n"))
n6 = int(input("6th Pick (1-35)\n"))
n7 = int(input("7th Pick (1-35)\n"))
n8 = int(input("8th Pick (1-35)\n"))


while n1:

    c1 = random.randint(1,35)
    c2 = random.randint(1, 35)
    c3 = random.randint(1, 35)
    c4 = random.randint(1, 35)
    c5 = random.randint(1, 35)
    c6 = random.randint(1, 35)
    c7 = random.randint(1, 35)
    c8 = random.randint(1, 35)
    count = 10

    while count != 0:
        print (count)
        count -= 1
        time.sleep(0.5)


    print ("your numbers:", n1,n2,n3,n4,n5,n6,n7,n8)
    print ("Winning numbers", c1,c2,c3,c4,c5,c6,c7,c8)
    n1 = int(input("1st Pick (1-35)\n"))
    n2 = int(input("2nd Pick (1-35)\n"))
    n3 = int(input("3rd Pick (1-35)\n"))
    n4 = int(input("4th Pick (1-35)\n"))
    n5 = int(input("5th Pick (1-35)\n"))
    n6 = int(input("6th Pick (1-35)\n"))
    n7 = int(input("7th Pick (1-35)\n"))
    n8 = int(input("8th Pick (1-35)\n"))