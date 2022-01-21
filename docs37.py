a={"x":[11,12,13,14,15,16,17,18,19],"y":[21,22,23,24,25,26,27,28,29],"z":[31,32,33,34,35,36,37,38,39]}
n=[]
for i in a:
    # print(a[i])
    n.append(a[i])
j=0
while j<len(n):
    k=0
    while k<len(n[j]):
        if n[j][k]%5==0:
            print(n[j][k])
        k=k+1
    j=j+1