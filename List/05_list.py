# Check if a number exists in a list. Print True/False.

list=['h',"sdd",'ddd','pilu',' rahul',8]
for i in list:
    if isinstance(i,int) or isinstance(i,float):
        print("true")
        break
else:
     print("false")