dict={"a":3,"b":4,"c":5}
a=[]
for i in dict:
    a.append(dict[i])
i=0
mul=1
while i<len(a):
    mul=mul*a[i]
    i=i+1
print(mul)