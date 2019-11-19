l=['a','a', 'b','c','d']
print(len(l))
print(max(l))
print(min(l))
l.append('g')
print(l)
l2=['h','i','j','k']
l.extend(l2)
print(l)
l.insert(2,'z')
print(l)
print(l.pop(2))
print(l)
print(l.pop())
l.remove('a')
print(l)
l.reverse()
print(l)

ob=[
{
    "team": "KKR",
    "fname": "Rahul",
    "lname": "Dravid",
    "city": "Kolkata"
},
{
    "team": "KKR",
    "fname": "Sachin",
    "lname": "Tendulkar",
    "city": "Mumbai"
},
{
    "team": "RR",
    "fname": "Saurav",
    "lname": "Ganguly",
    "city": "Delhi"
},
{
    "team": "MI",
    "fname": "V V S",
    "lname": "Laxman",
    "city": "Hyderabad"
}
]
def mysort(el):
    print("inside mysort"+el["fname"])
    return el["fname"]
ob.sort(key=mysort)
print(ob)
def myfilter(el):
    return el["team"]=="KKR"
newobj= filter(myfilter, ob)
print(type(newobj))
for i in newobj:
    print('{fname} {lname}'.format(**i) )

def myfilter1(el):
    return el["fname"].startswith("S")
newobj= filter(myfilter1, ob)
print(type(newobj))
for i in newobj:
    print('{fname} {lname}'.format(**i) )