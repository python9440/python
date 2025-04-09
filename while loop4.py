n=int(input("enter a number:"))
dup=n
sum=0
while n>=10:
    rem=n%10
    sum=(sum*10)+rem
    n=n//10
    if dup==sum:
        print("the given number is palindrome")
else:
    print("the given number is not palindrome")
