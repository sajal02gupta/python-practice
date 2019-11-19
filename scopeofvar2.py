def outer():
    print("this is outer!")
    def inner():
        print("this is inner!")
    inner()

outer()