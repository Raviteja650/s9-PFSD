#prime numbers 1 to 100
for i in range(1,101):
    for k in range(2,i):
        if i%k==0:
           # print("{} is not a prime number".format(i))
           break
    else:
        print("{} is  a prime number".format(i))
