a=[{"id":1,"success":True,"name":"lary"},{"id":2,"success":False,"name":"rabi"},{"id":3,"success":True,"name":"alex"}]
sum=0
for i in range(len(a)):
    for j in a[i]:
        if "id"==j:
            sum=sum+(a[i][j])
print(sum)