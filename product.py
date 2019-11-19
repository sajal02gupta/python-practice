li=[
    {
        "pid": 1,
        "pname": "BMWCar",
        "pbrand": "BMW",
        "prating": "4",
        "pcost": "4000000",
        "pdiscount": "30"
    },
{
        "pid": 2,
        "pname": "Car",
        "pbrand": "Maruti",
        "prating": "3.5",
        "pcost": "400000",
        "pdiscount": "20"
    },
{
        "pid": 3,
        "pname": "Car",
        "pbrand": "Toyota",
        "prating": "4",
        "pcost": "1000000",
        "pdiscount": "50"
    },
{
        "pid": 4,
        "pname": "Car",
        "pbrand": "Ford",
        "prating": "4",
        "pcost": "1500000",
        "pdiscount": "25"
    }
]
dict={
    "1": ["pcost", True],
    "2": ["pdiscount", True],
    "3": ["prating", True],
    "4": ["pcost", True],
    "5": ["pdiscount", True],
    "6": ["prating", True]

}

choice= input("Enter 1 for cost in ascending order and 5 in descending order, 2 for discount in ascending order and 6 in descending order, 3 for rating in ascending order and 7 in descending order")

li.sort(key=lambda el: float(el[dict[choice]]), reverse=True)
print(li)

