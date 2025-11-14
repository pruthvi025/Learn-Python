# Append an element to a list without using .append().
l=[5,9,6,3,2,5,8,7,4,8,5]
l+=[85]

print(l)

l[len(l):]=[55]

print(l)