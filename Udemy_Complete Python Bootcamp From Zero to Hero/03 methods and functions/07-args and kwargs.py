def myfunc(*args):
    return sum(args)*5

print(myfunc(40,60,30))


def myfunc2(**kwargs):
    if "fruit" in kwargs:
        print(f"my favorite fruit is {kwargs['fruit']}")
    else:
        print("no fruit")

print(myfunc2(fruit = "apple"))


def myfunc3(*args, **kwargs):
    if "fruit" and "juice" in kwargs:
        print(f"i like {' and '.join(args)} and my favorite fruit is {kwargs['fruit']}")
        print(f"may i have some {kwargs['juice']} juice?")
    else:
        pass

myfunc3("eggs", "spam", fruit="cherries", juice="orange")