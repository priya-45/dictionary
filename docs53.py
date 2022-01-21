l=[[1,"jean castro","v"],[2,"lula powell","v"],[3,"brian howell","vi"],[4,"lynne foster","vi"],[5,"zachary simon","vii"]]
d={}
for i in l:
    j=0
    while j<len(i):
        d[i[0]]=[i[1],i[2]]
        j+=1
print(d)
# i=0
# while i<len(a):
#     j=0
#     while j<len(a[i]):
#         print(a[i][j])
#         j=j+1
#         break
#     i=i+1
# m={}
# for i in range(len(a)):
#     for j in range(len(a[i])):
#         t=(a[i][j])
        
#         del a[i][j]
#         print(t)
#         for k in range(len(a)):
#             l=t
#             m.update({l:a})
#         break
# print(m)