=list(a)
i=0
a={}
while i<len(d):
	count=0
	# b={}
	j=0
	while j<len(d):
		if d[i]==d[j]:
			count+=1
		j=j+1
	a.update({d[i]:count})
	i+=1
print(a)
#a="w3resource"
d
#i=0
#b={}
#while i<len(a):
#	count=0
#	j=0
#	while j<len(a):
#		if a[i]==a[j]:
#			count+=1
#		j=j+1
#	b.update({a[i]:count})
#	i+=1
#print(b)
