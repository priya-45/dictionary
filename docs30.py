dic={"s  001":["math","science"],"s  002":["math","english"]}
str=""
n={}
m=[]
for a in dic:
    b=dic[a]
    i=0
    l=""
    while i <len (a):
        if " " not in a[i]:
            l=l+a[i]
        else:
            pass
        i=i+1
    n.update({l:b})
print(n)