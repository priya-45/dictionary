data=[{'item':'item1','amount':400},{'item':'item2','amount':300},{'item':'item1','amount':750}]
m=[]
for i in range(len(data)):
    for j in data[i]:
        p=(data[i][j])
        m.append(data[i][j])
print(m)
i=0
j=1
n={}
while i<len(m):
    while j<len(m):
        n.update({m[i]:m[j]})
        i=i+2
        j=j+2
        print("a=",n)

        # for k in n:
        #     if k==k:
        #         p=n[k]+n[k]
        #         print(p)
    
# print(d)
        
    
#     for j in data[k]:
#         #a=data[k][j]
#         #b=data[k][j]
#         p=(data[k][j])
#         dict[p]=j
# print(dict)

   