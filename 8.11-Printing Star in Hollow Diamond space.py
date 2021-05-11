# n=int(input("How many rows are there?\n"))
for a in range(5):
    for b in range(5):
        if a+b==2 or b-a==2 or a-b==2 or a+b==6:
            print("*",end=" ")
        else:
            print(" ",end=" ")
    print()