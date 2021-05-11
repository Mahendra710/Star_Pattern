n=int(input("How many rows are there?\n"))
for a in range(1,n+1):
    for s in range(a,n):
        print(" ",end=" ")
    for b in range(2*a-1):
        if b%2==1:
            print("*",end=" ")
        else:
            print(" ",end=" ")
    print()
