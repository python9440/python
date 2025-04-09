n=int(input("enter a number:"))
dup=n
sum=0
while n>0:
    rem=n%10
    sum=sum+(rem**3)
    n=n//10
    if dup==sum:
        print("the given number is armstrong")
else:
    print("the given number is not armstrong")
    
