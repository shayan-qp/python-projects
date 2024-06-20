while True:
    a = int(input("enter a number:"))
    if  a>3 and a%a==0 and a%1==0 and a%2!=0 and a%3!=0 and a%5!=0 and a%7!=0:
        print("yes")
    elif a ==2 or a==3 or a==5 or a == 7:
        print("yes")
    elif a==1:
        print("no")
    else:
        print("no")