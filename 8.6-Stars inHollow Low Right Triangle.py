n=int(input("How many rows are there?\n"))
for a in range(n,0,-1):
    for s in range(a,n):
        print(" ",end=" ")
    for b in range(a,0,-1):
        if a==n or b==1 or a==b:
            print("*",end=" ")
        else:
            print(" ",end=" ")
    print()
