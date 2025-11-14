# Find the largest and smallest number in a list without using max/min.

l=[2,8,9,6,5,4,2,5,7,8,9,6,54]
maxnum=l[0]
minnum=l[0]
for i in l:
    if i>maxnum:
        maxnum=i
    if i< minnum:
        minnum=i
    
print(maxnum)
print(minnum)