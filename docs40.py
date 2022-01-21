a=['S001',"S002","S003","S004"]
b=["Adina park","leyton marsh","Duncan Boyle","saim richards"]
c=[85,98,89,92]
list1=[]
list2=[]
i=0
j=0
while i<len(a) and j<len(b):
    dict1={}
    dict1[b[i]]=c[j]
    i+=1
    j+=1
    list1.append(dict1)
print(list1)
i=0
j=0
while i<len(a) and j<len(b):
    dict2={}
    dict2[a[i]]=list1[j]
    i+=1
    j+=1
    list2.append(dict2)
print(list2)
#a=['S001',"S002","S003","S004"]
# b=["Adina park","leyton marsh","Duncan Boyle","saim richards"]
# c=[85,98,89,92]
# p={}
# i=0
# while i<len(a):
#     while i<len(b):
#         while i<len(c):
#             p.update({a[i]:b[i]})
#             i=i+1
# print(p)
# f=0
# n={}
# while f<len(p):
#     print(p[f])
#     # while f<len(c):
#     #     n.update({p[f]:c[f]})
#     # # n.update({p})
#     f=f+1
#        n)
#  print(

#     while o<len(c):
#         w.update({p[o]:c[o]})
#         o=o+1
# print(w)
# a=[[2,3,4],[4,5,6],[7,8,9]]
# sum=0
# i=[]
# while i<len(a):
#     j=0
#     while j<len(a[i]):
#         sum=sum+a[i][j]
#         j=j+1
#     i=i+1
#     print(sum)