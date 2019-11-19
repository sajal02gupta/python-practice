str="Python"
i=0
j=len(str)
while j>i:
    while j>0:
        print(" ", end="")
        j-=1
    for i in range(0,j):
        print(str[0,i+1], end="")
    j-=1