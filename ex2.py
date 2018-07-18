with open("E:/Semester V/IP/abc.txt","r") as f:
    x=f.read().split()
    temp=""
    for var in x:
        if len(var) > len(temp):
            temp=var
print(temp)
print("success")
