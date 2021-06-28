

def this_is_a_wrapper(func):


    def prints(age:int):
        print(f"Called with {age}")
        return func(age)


    return prints