a={"cierra vega":175,"alden cantrell":180,"kierra gentry":165,"pierre cox":190}
m={}
for i in a:
    if a[i]>170:
        m.update({i:a[i]})
print(m)

