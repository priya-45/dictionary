a={"V":[1,4,6,10],"Vi":[1,4,12],"VII":[1,3,8]}
c={}
for i in a:
    b=[]
    for j in a[i]:
        if j%2==0:
            b.append(j)
    c[i]=b
print(c)
# m=[]
# for x in a: 
#     t=(a[x])
#     m.append(t)
# print(m)
# i=0
# while i<len(m):
#     j=0
#     n=[]
#     while j<len(m[i]):
#         if m[i][j]%2==0:
#             l=(m[i][j])
#             print(l)
#             n.append(l)
#         # print(n)
#         j=j+1
#     print()
#     i=i+1
# n.append(l)
# print(n)
