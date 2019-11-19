def outer():
    count=1
    def inner():
        nonlocal count
        print("hello", count)
        count+=1
    return inner

hello=outer()
hello()
hello()
