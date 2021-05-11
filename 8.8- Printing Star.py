n=int(input("How many rows are there?\n"))
k=2
for a in range(1,n+1):
    for b in range(1,2*n):
        if a+b==n+1 or b-a==n-1:
           print("*",end=" ")
        elif a==n and b!=k:
            print("*",end=" ")
            k=k+2
        else:
            print(" ",end=" ")
    print()
