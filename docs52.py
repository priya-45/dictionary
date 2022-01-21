a={"a":5,"b":14,"c":32,"d":35,"e":24,"f":100,"g":57,"h":8,'i':100}
max=0
for i in a:
    if a[i]>max:
        max=a[i]
print(max)
m=[]
for y in a:
    if max==a[y]:
        m.append(y)
        print(m)
m=[]
for i in a:
        if a[i]>30:
            p=i
            m.append(p)
print(m)