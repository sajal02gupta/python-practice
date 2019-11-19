value=int(input('Enter the value you want to get a factor of it: '))
i=1
sum=0
count=0
while i<=value:
    if value%i==0:
        print(i,"is a factor")
        count+=1
        sum+=i
    i+=1
print('total no. of factors and sum are',count, sum,'respectively')