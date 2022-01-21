a={"c1":[10,20,30],"c2":[20,30,40],"c3":[12,34]}
for i in a:
    for j in a[i]:
        a[i].clear()
print(a)