def fun1 (a):
    s = 0
    while a>0:
        s=s+a%10
        a=a//10
    print(s)
x=int(input("enter a number:"))
fun1(x)
