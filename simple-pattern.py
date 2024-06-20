x="*"

for a in range(5):
    print(x)
    y=len(x)
    x="*"
    z=y+1
    x=x*z

# or

s="*"
for i in range(1,6):
    for j in range(i):
        print(s,end="")
    print(end="\n")
