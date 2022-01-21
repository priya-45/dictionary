a={1:"red",2:"green",3:"black",4:"white",5:"black"}
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

