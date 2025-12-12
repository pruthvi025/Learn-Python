# Concatenate two tuples without using loops.
t1=(5,8,96,5,4,5,8,9)
t2=("df",52,2.5,'gff')
t3=t1+t2

print(t3)

# using the forloop

result=()
for i in t1:
    result+=(i,)
for i in t2:
    result+=(i,)

print( f"using loop result is :{result}")