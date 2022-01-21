a={"v":[1,3,5],"vi":[1,5],"vii":[2,7,9]}
for i in a:
    for j in a[i]:
        a[i].clear()
print(a)