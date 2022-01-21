a={"d":100,"g":200,"h":300}
b={"s":100,"y":200,"t":300}
j={}
for i in a:
    if i not in j:
        j.update(a)
        j.update(b)
        print(j)