# Reverse a list without using slicing or reverse().

l=[65,85,96,54,25,36,8,7,89,5,8,5]

i=0
j=len(l)-1

while i<j:
    l[i],l[j]=l[j],l[i]
    i+=1
    j-=1

print(l)