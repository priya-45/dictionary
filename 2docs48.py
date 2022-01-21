a={"1":"austin little","2":"natasha howard","3":"alfred mullins","4":"jamie rowe"}
m=[]
for i in a:
    for j in a[i]:
        pass
    m.append(a[i])
n={}
j=0
while j<len(m):
    k=0
    c=0
    while k<len(m[j]):
        c=c+1
        k=k+1
    n.update({m[j]:c}) 
    j=j+1
print(n)
