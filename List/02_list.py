# Take 5 inputs from the user and store them in a list.

list=[]
N=int(input("how many number you want to store in the list : - "))

for i in range(N):
    i=int(input())
    list.append(i)

print(list)