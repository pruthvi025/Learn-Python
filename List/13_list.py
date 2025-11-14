# Remove element 50 from a list without using .remove().

l=[54,89,5,489,5,8,9,50,9,68,98,48]

# l.remove(50)
l1=[]

for i in l:
    if i==50:
        continue
    l1.append(i)

print(l1)

