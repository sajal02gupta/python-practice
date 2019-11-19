astring = "Hello World"
print(len(astring))
print(astring.index("o"))
print(astring.index('o',5))
print(astring.index('o',5,8))
print(astring.count("l"))
print(astring.upper())
print(astring.lower())
print(astring.startswith("Hello"))
print(astring.endswith("d"))
words = astring.split(" ")
print(words)
print(astring.find('o'))
print(astring.find('o',5))
print(astring.find('o',5,7))
print(astring.replace("World","Python"))

temp='''Hello {fname} {lname}, Welcome to {city}'''
dataString = temp.format(fname="Sachin", lname="Tendulkar", city="Gwalior")
print(dataString)

ob=[
{
    "fname": "Rahul",
    "lname": "Dravid",
    "city": "Kolkata"
},
{
    "fname": "Sachin",
    "lname": "Tendulkar",
    "city": "Mumbai"
},
{
    "fname": "Saurav",
    "lname": "Ganguly",
    "city": "Delhi"
},
{
    "fname": "V V S",
    "lname": "Laxman",
    "city": "Hyderabad"
}
]
for d in ob:
    dataString1= temp.format(**d)
    print(dataString1)
