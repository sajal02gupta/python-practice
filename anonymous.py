'''
Anonymous function
Inline function
lambda function

Rule1: function should contain only 1 line
Rule 2: that 1 line should be return statement

def sayhi(n1,n2):
    return ("hi" +n1+" " +n2)
'''
data= (lambda n1,n2: "Hi "+n1+" "+n2)("Sachin","Ashmita")
print(data)

hello= lambda n1,n2: "Hi "+n1+" "+n2
print(type(hello))
print(hello("sajal","Saurav"))
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

ob.sort(key=lambda el:el["fname"])
print(ob)

