s=" "
z=2
for i in range(1,6,2):
    print(s*z,end="")
    z-=1
    for j in range(1,i+1):
        print(j,end="")
    print(end="\n")