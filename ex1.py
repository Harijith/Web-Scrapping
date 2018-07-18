sent="I have been working on this assignment since monday"
list=sent.split()
a=""
temp=""
for a in list:
    if len(a)>len(temp):
        temp=a
print(temp)
