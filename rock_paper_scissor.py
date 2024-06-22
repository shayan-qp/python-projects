import random

rps=["rock","paper","scissor"]

x=random.choice(rps)

y=input("choose yours : ")


if y=="rock":
    if x=="rock":
        print("tie")
    elif x=="paper":
        print("lose")
    elif x=="scissor":
        print("win")


elif y=="paper":
    if x=="rock":
        print("win")
    elif x=="paper":
        print("tie")
    elif x=="scissor":
        print("lose")


elif y=="scissor":
    if x=="rock":
        print("lose")
    elif x=="paper":
        print("win")
    elif x=="scissor":
        print("tie")


else:
    print("error")


print("\n,your opp choose",x)