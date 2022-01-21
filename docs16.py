a=[1,3,5,4,9,7]
b=[3,5,6,7,8,9]
s={}
i=0
while i<len(a):
    while i<len(b):
        s.update({a[i]:b[i]})
        i=i+1
print(s)