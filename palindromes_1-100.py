#display palindromes no from 1-100
"""def palindrome(i):
    ans=i
    sum=0
    while i!=0:
        r=i%10
        sum=(sum*10)+r
        i=i//10
#print(sum)
if ans==sum:
    #print("{} is a palindrome".format(sum))
    print(ans)
else:
    pass


for i in range(1,101):
    palindrome(i)"""

for i in range(1,101):
    n=i
    sum=0
    while(i>0):
        r=i%10
        sum=sum*10+r
        i=i//10
    if(n==sum):
        print(sum)
    
