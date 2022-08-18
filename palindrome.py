#to fing palindrome
n=int(input("enter a number:"))
ans=n
sum=0
while n!=0:
    r=n%10
    sum=(sum*10)+r
    n=n//10
#print(sum)
if ans==sum:
    print("{} is a palindrome".format(sum))
else:
    print("{} is not a palindrome".format(sum))

