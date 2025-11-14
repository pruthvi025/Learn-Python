# Count how many even and odd numbers are in a list.


l=[50,69,54,85,9,6,5,41,5,2,56,75,50,69,54]

even=0
odd=0

for i in l:
    if i%2==0:
        even+=1
    else:
        odd+=1

print(even)
print(odd)