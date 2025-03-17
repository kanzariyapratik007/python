#Dictionary python
a={"id":2,"fast name":"radhe radhe"}
print (type(a))
print (a)
print (a["fast name"])
a.pop("id")
print (a)
print (a.get("id","no data "))
print (a.clear())
print (a)
b={"id":2,"fast name":"radhe radhe"}
print (b.keys())
print (b.values())
print (b.items())
for key,values in b.items():
    print (key,values,sep=" = ")
    b["id"]=50 #update
    print (b)
 a1=a.copy() #copy       
    
    
