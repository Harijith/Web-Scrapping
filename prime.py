a=int(input("Ënter a number:"))
i=1
flag=0
while(i<=a/2):
    if(a%i==0):
        flag=1
    else:
        flag=0
    i=i+1
if(flag==1):
    print("not prime")
else:
    print("prime")
