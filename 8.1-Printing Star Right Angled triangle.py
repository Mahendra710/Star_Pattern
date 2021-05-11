n=int(input("How many rows are there?\n"))
for a in range(n+1):
    for b in range(a):
        print('*',end=' ')
    print()

# second type
n=int(input("How many rows are there?\n"))
for a in range(1,n+1):
    for b in range(1,a+1):
        print('*',end=' ')
    print()


n=int(input("How many rows are there?\n"))
for a in range(n,0,-1):
    for b in range(a):
        print('*',end=' ')
    print()