def palin(n):
    n=str(n)
    return n == n[::-1]

n=int(input())
while True:
    n=n+1
    if palin(n):
        break
print(n)
