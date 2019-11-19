value= int(input('Enter the value to check whether it is prime or not'))
i=2
flag=1
while i<value/2:
    if value%i==0:
        print('Not prime')
        flag=0
        break
    i+=1

if flag==1:
    print('prime')