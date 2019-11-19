i=1
val=int(input('Enter the number'))
while i<val+1:
    j=0
    while j<i:
        print("*", end="")
        j+=1
    print()
    i+=1