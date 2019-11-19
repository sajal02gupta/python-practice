dict={
    "1": "friday",
    "2": "Saturday",
    "3": "Sunday",
    "4": "Monday",
    "5": "Tuesday",
    "6": "Wednesday",
    "0": "Thursday"
}

date=int(input("Enter the date"))
val=date%7
print(dict[str(val)])