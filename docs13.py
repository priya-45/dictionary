my_dict={"a":12,"b":14,"c":9}
a=[]
for i in my_dict:
    a.append(my_dict[i])
i=0
sum=0
while i<len(a):
    sum=sum+a[i]
    i=i+1
print(sum)