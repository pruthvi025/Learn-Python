# Find all elements that appear more than once.

l=[50,69,54,85,9,6,5,41,5,2,56,75,50,69,54]

seen=set()
dupes=set()

for i in l:
    
    if i in seen:
        dupes.add(i)
    else:
        seen.add(i)

print(list(dupes))