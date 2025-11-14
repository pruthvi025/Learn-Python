# Remove duplicates from a list.

l=[50,69,54,85,9,6,5,41,5,2,56,75,50,69,54]
print(l)

l1=[]

for i in l:
    if i in l1:
        continue
    l1.append(i)
print(l1)