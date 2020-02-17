row = int(input("Please input a number of row"))

for i in range (row):
    print(" "*(row-i),"^"*i,"^","^"*i," "*(row-i),sep="")
print(" "*row,"^"," "*row,sep="")
print(" "*row,"^"," "*row,sep="")