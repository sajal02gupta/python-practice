t=([1,2],[3,4],[5,6],4)
print(t[0])
print(t[0][0])
t[0][0]=100
t[1][1]=4
print(t[0])
print(t)

t1=(2,4,6,7,(2,3,4))
print(t1)
li=set(t1)
print(li)

dict1={
        'fname' : 'Sajal',
        'lname' : 'Gupta'
        }
dict2={
        'fname' : 'Shishir',
        'lname' : 'Bro',
        'tname' : dict1
}

print(dict2)
linew=[dict1,dict2]
print(linew)
print(type(dict1))
list2=list(dict1)
print(dict1.keys())
set1=set(dict1)
print(set1)
print(list(li))
li4=[(34,5),(5,6)]
print(li4)
li4=[1,3,5,6,[2,3]]
k1={2,3}
print(type(k1))
li=[["a",1],["d",5]]
print(dict(li))
print(li4)


       