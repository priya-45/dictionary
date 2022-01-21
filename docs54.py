a={1:["jean castro"],2:["lula po print(m)well"],3:["brian howell"],4:["lynne foster"],5:["zachary simon"]}
m={}
n=[]
for i in a:
    for j in a[i]:
        m.update({i:j})
n.append(m)
print(n)