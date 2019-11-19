data=[1,2,3,True, None, "Hello"]

gig=1,2,3
print(type(gig))


data[1]=1000
print(data)
print(type(data))
print(data[0])

print(data[-1])

print(data[::-1])

print(type(data))

print(data[-1][::-1])

data=1,2,3
print(data)
s1={True,1,2,3,3,None, 2}
print(s1)
print(type(s1))

s11={1,2,34,4}
s12={4,5,6,3}
print(s11|s12)
print(s11-s12)
print(s12-s11)
print(s11&s12)
print(s12<s11)

"""data={s11,s12}
"""
print(data)

snew={
    'fname': "Sachin",
    'lname': "Tendulkar"
}
snew['team']="India"

print(snew)

str1="Hello"
list1=list(str1)
print(type(list1))
print(list1)

