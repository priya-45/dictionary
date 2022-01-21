dic1={1:10,2:20}
dic2={3:30,4:40}
dic3={5:50,6:60}
dict={}
for i in dic1:
    if i not in dict:
        dict.update(dic1)
        dict.update(dic2)
        dict.update(dic3)
        print(dict)