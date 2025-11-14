# Count how many times 10 appears in a list

l=[5,6,10,59,25,10,78,65,10,25,10,45,1,2,3,6,10,85]
count=0
for i in l:
     if i==10:count+=1
print(count)
print(l.count(10))