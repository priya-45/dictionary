a=[{"x":"10","y":"20","z":"30"},{"p":"40","q":"50","r":"60"}]
m={}
n={}
for i in range(len(a)):
    t=(a[i])
    for k in t:
        d=int(t[k])
        l=float(t[k])
        m.update({k:l})
        n.update({k:d})
print(n)
print(m)


    