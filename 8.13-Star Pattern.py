for i in range(9):
    for j in range(13):
        if i==2 or i==6 or i+j==6 or j-i==6 or i-j==2 or i+j==14:
            print("*",end="")
        else:
            print(" ",end="")
    print()


n=int(input("Enter the rows(>5):"))
col=n+n-5
mid=col//2
for i in range(n):
    for j in range(col):
        if i==2 or i==(n-3) or i+j==mid or j-i==mid or i-j==2 or i+j==col+1:
            print("*",end="")
        else:
            print(" ",end="")
    print()