def sayhi(**kwargs):
    print(type(kwargs), kwargs)

sayhi(name1="sachin")
sayhi(name1="sajal", name2="saurav")
sayhi(name1="sajal", name2="sachin", name3="saurav")

#generic function
def sayhii(*args, **kwargs):
    print(args, kwargs)


sayhii("Sajal", "Akhil", name1="Rachit")

def sayhi1(n1,n2,n3):
    print("HI "+n1+" "+n2+" "+n3)

li=["Sajal","Akhil", "Vinayak"]
sayhi1(*li)
sayhi1(*set(li))

li3={
    "n1" : "Sajal",
    "n2" : "Akhil",
    "n3" : "Lakshit"
}

sayhi1(**li3)