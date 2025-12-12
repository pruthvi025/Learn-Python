# Given a tuple, count how many times a specific value appears.
t1=(52,56,5,258,65,65,32,59,65,65,89)

x=int(input("enter a specific value : "))
count=0

for i in t1:
    if x==i:
        count=count+1

print(f"the value {x} is Appear {count } times")