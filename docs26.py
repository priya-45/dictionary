my_dict={'c1':[1,2,3],'c2':[5,6,7],'c3':[9,10,11]}
for x in my_dict:
    print(x,end=' ')
print()
n=[]
for x in my_dict:
    m=(my_dict[x])
    n.append(m)
i=0
while i<len(n):
    j=0
    while j<len(n[i]):
        sum=n[j][i]
        print(sum,end=' ')
        j=j+1
    print()
    i=i+1
    #print(sum)