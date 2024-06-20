a=int(input("enter a num:"))
x=a
i=-1
while x>0:
    x//=10
    i+=1
for b in range(i+1):
    s=a//(10**i)
    a%=(10**i)
    i-=1
    print(s)