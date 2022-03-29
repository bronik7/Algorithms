from functools import wraps


def test(fn):
    @wraps(fn)
    def wrapper():
        print("TESTING")
        print(f"I am calling {fn.__name__}")
        fn()
        print("Done Testing")

    return wrapper


@test
def printing():
    """Printing function """
    print("Hello Bro")


@test
def printing2():
    """Printing 2 function """
    print("Hello Bro2")


# printing()

# printing2()


def authorize(fn: object) -> object:
    def wrapper(*args, **kwargs):
        if kwargs.get("role") == "admin":
            return fn(*args, **kwargs)
        else:
            return "Unauthorized"

    return wrapper


@authorize
def authorized_user(name, lastname, role="nobody"):
    return f"{name} {lastname} role is {role}"


# authorize(authorized_user("bronik", "novak", role="admin"))


# print(authorized_user("broni2k", "novak",))


from time import sleep


def delay(t):
        print("Waiting " + str(t) + "s before running say_hi")
        sleep(t)
        def inner(f):
           def wrapper(*args,**kwargs):
               print("calling inner")
               return f(*args,**kwargs)
           return wrapper
        return inner


@delay(3)
def say_hi(*args,**kwargs):
    print("Hello " + args[0])


say_hi("blah")
