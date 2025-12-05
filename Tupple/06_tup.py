# Given a tuple (10, 20, 30, 40, 50), print the tuple in reverse without using reversed().

t1=(10, 20, 30, 40, 50)

print(t1[::-1])

i=len(t1)-1
while i!=-1:
    print(t1[i])
    i-=1