def decorator_do_it_twice(func):
    def run_twice(*args):
        return func(func(*args))

    return run_twice


def decocator_detect_output(func):
    def raise_error(*args):
        result = func(*args)
        if result > 2:
            raise ValueError
        return result
    return raise_error


def decorator_detect_input(func):
    def raise_error(*args):
        if args[0] >= args[1]:
            raise AssertionError()
        return func(*args)

    return raise_error


@decorator_do_it_twice
def add_one(number: int) -> int:
    return number + 1


def decorator_with_arg(*name, **kw):


    range = kw.get("is_in_range", [])
    print(f"Has been called with{name}")
    def inner_func(func):
        return func

    return inner_func



@decorator_detect_input
@decocator_detect_output
@decorator_with_arg(is_in_range="Input")
def add_one_up_until(input: int, max: int) -> int:
    if input < max:
        return input + 1
    return input


if __name__ == '__main__':
    print(add_one(6))
    for i in range(0, 10):
        print(add_one_up_until(i, 5))

"""
def pretty_sumab(func):
    def inner(a, b):
        print(str(a) + " + " + str(b) + " is ", end="")
        return func(a, b)

    return inner


@pretty_sumab
def sumab(a, b):
    summed = a + b
    print(summed)


#if __name__ == "__main__":
#    sumab(5, 3)



from src.input_validator import this_is_a_wrapper


@this_is_a_wrapper
def basic_func(age:int)->int:
    return age +10


if __name__ == '__main__':
    basic_func(10)
    """
