a={"a":34,"b":56,"c":78,"d":29,"e":90}
i=0
m=[]
for l in a:
    m.append(a[l])
max=0
min=m[i]
while i<len(m):
    if m[i]>max:
        max=m[i]
    if m[i]<min:
        min=m[i]
    i=i+1
print(min)
print(max)