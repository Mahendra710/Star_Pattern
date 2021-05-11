n=int(input("How many rows are there?\n"))
for a in range(1,n+1):
    for b in range(1,a+1):
        if b==1 or a==n or a==b:
            print("*",end=" ")
        else:
            print(" ",end=" ")
    print()
