marks= float(input('Enter the marks'))

if marks>=0 and marks <= 100:
    if marks>=0 and marks<=39:
        print('Fail')
    elif marks>=40 and marks<= 59:
        print('Third')
    elif marks>=60 and marks<= 79:
        print('Second')
    elif marks>=80 and marks<= 100:
        print('first')
else:
    print('Invalid marks')

data='Hello Python'
for d in data:
    print(d, end=" ")
print()
data=[1,23,56,'Rahul']
for d in data:
    print(d, end=" ")
print()
dict={'fname': 'Rahul', 'lname': 'Yadav'}
for d in dict.values():
    print(d)

data= range(30,100,10)
print(type(data))
for d in data:
    print(d, end=" ")

