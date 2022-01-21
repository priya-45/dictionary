a=[{"V":"S001"},{"V":"S002"},{"VI":"S001"},{"VI":"S005"},{"VII":"S005"},{"V":"S009"},{"VIII":"S007"}]
p=[]
for i in range(len(a)):
    for j in a[i]:
        p.append(a[i][j])
print(p)
o=[]
i=0
while i<len(p):
    if p[i] not in o:
        o.append(p[i])
    i=i+1
print(o)