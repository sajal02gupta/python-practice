a = input('Enter 1st number: ')
b = input('Enter 2nd number: ')
c = input('Enter 3rd number')


if a>b:
    if a>c:
        print('1st is greater')
elif b>c:
    print('2nd is greater')
else:
    print("3rd is greater")
    
    
marks=float(input('Enter the marks'))

if marks>=0 and marks<=100:
    print("Valid")
else:
    print('Invalid')
    
    
    
    
    
year= int(input('Enter the year'))

if year%400==0:
    print('Leap year')
elif year%100==0:
    print('Not leap')
elif year%4==0:
    print('Leap')
    
    
    
    
i=0

while i<=10:
    print(i)
    i+=1
else:
    print("Loop exhausted")
