import time
sadoms=0
dahoms=0
s=0
m=0
h=0
while True:
    sadoms=sadoms+1
    if sadoms==10:
        dahoms=dahoms+1
        sadoms=0
    if dahoms==10:
        s=s+1
        dahoms=0
    if s==60:
        m=m+1
        s=0
    if m==60:
        h=h+1
        m=0
    print(h,":",m,":",s,":",dahoms,":",sadoms)
    time.sleep(0.01)