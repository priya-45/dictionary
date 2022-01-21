a={"item1":45.50,"item2":35,"item3":41.30,"item4":55,"item5":24}
m=[]
for i in  a:
    m.append(a[i])
print(m)
i=0
max=0
l=[]
while i<len(m):
    if m[i]>max:
        max=m[i]
    i=i+1
j=0
nmax=0
while j<len(m):
    if m[j]>nmax:
        if m[j]<max:
            nmax=m[j]
    
    j=j+1
k=0
mmax=0
while k<len(m):
    if m[k]>mmax:
        if m[k]<nmax:
            mmax=m[k]
    k=k+1
l.append(max)
l.append(nmax)
l.append(mmax)
print(l)
for y in a:
    if max==a[y]:
        print(y,max)
    if nmax==a[y]:
        print(y,nmax)
    if mmax==a[y]:
        print(y,mmax)
