a="my name is priya and you"
i=0
k=1
c=" "
c1=0
b=a.split()
print(b)
m={}
while i<len(b):
    j=0
    while j<len(b[i]):
        t=b[i]
        v=b[i]
        print(v)
        m.update({t:k})
        if c==" ":
            c1=c1+1
            print(c1)
        if c1==1:
            m.update({"space1":k})
            # m.update({t:j})
        if c1==2:
            m.update({"space2":k})
            # m.update({t:j})
        j=j+1
    i=i+1
    k=k+1
print(m)
# a="my name is priya and you"
# 2	i=0
# 3	j=1
# 4	c=" "
# 5	c1=0
# 6	b=a.split()
# 7	print(b)
# 8	m={}
# 9	while i<len(b):
# 10	    if c==" ":
# 11	        c1=c1+1
# 12	        t=(b[i])
# 13	    if c1==1:
# 14	        m.update({"space1":j})
# 15	    if c1==2:
# 16	        m.update({"space2":j})
# 17	    m.update({t:i})
# 18	    i=i+1
# 19	    j=j+1
# 20	    # m.update({"space1":i})
# 21  print(m)


