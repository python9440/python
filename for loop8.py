n=input("enter some numbers:").split
i=0
j=0
for x in n:
    x=int(x)
    if x%2==0:
        i=i+1
else:
    j=j+1
    print("even numbers count is",i)
    print("odd numbers count is",j)
            
