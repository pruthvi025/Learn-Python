# Check if a user-input value exists inside a tuple.

t1=(1,2,3,4,5,6,7,8)

val=int(input("enter a value : "))

for i in t1:
    if i==val:
        print("yes")
        break
else:
    print("no")




if val in t1:
    print("yes")
else:
    print("no")