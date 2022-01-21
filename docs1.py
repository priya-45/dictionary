d1={"a":100,'b':200,'c':300}
d2={'a':300,'b':200,'d':400}
k={}
for x in d1:
    for y in d2:
        if x==y:
            p=(d1[x]+d2[y])
            k.update({x:p})
k.update({'d':400})
k.update({'c':300})
print(k)