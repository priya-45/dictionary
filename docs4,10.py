# i=1
# j={}
# while i<=15:
#     j[i]=i*i
#     i=i+1
# print(j)
n=int(input("enter number"))
d={}
for x in range(1,n+1):
    d[x]=x*x
print(d)