from random import choice


# def print_hi():
#     print("Test")
#
# # print(print_hi())
#
#
# def t():
#     print("Tes2")


def paper_rock_scissors(user_choice="Paper"):
    choices = choice(["Paper", "Rock", "Scissors"])
    print(f"Computer: {choices} User: {user_choice}")

    if user_choice == choices:
        print("Draw")
    elif (user_choice == "Paper" and choices == "Scissors") \
            or (user_choice == "Rock" and choices == "Paper") \
            or (user_choice == "Scissors" and choices == "Rock"):
        print("User Lost")
    else:
        print("User won")


# choice1 = choice(["Paper", "Rock", "Scissors"])
# paper_rock_scissors(choice1)


def luckynumber():
    for number in range(1, 21):
        if number == 4 or number == 13:
            print(f"{number} Unlucky")
        elif number % 2 == 0:
            print(f"{number} Even")
        else:
            print(f"{number} Odd")


def forloop():
    for emoji in range(9):
        print("\U0001f600" * emoji)


def whileloop():
    x = 0
    while x < 9:
        print("\U0001f600" * x)
        x += 1


def draw_pyramid():
    rows = 10
    count_char = 0
    for x in range(rows, 0, -1):
        letter = "\U0001f600 "
        spaces = ""
        spaces += " " * x
        letter += letter * count_char
        print(spaces + letter)
        count_char += 1


# raw_pyramid()
def last_element(l):
    l.insertAtPosition(0, 7)
    print(l)


# last_element([2, 4])


def list_manipulation(collection, command, location, value=None):
    if (command == "remove" and location == "end"):
        return collection.pop()
    elif (command == "remove" and location == "beginning"):
        return collection.pop(0)
    elif (command == "add" and location == "beginning"):
        collection.insertAtPosition(0, value)
        return collection
    elif (command == "add" and location == "end"):
        collection.append(value)
        return collection


def concatenate2(**words):
    result = ""
    for k, v in words.items():
        if type(v) == dict:
            print(list(v.keys())[1] + " " + list(v.values())[0])
        else:
            print(v)

    return result


# print(concatenate(test="fde", bleu="fdfdfe", les={"B": "afdddd", "C": "Rambo"}))

def concatenate(*args):
    word = list(map(lambda x: str(x) + " !", filter(lambda b: str(b) == "t", args)))
    print(word)
    word = list(map(lambda x: str(x) + " 454", filter(lambda b: not b, args)))
    print(word)


# concatenate2(test="t",bles="B", he=2,cat={"B":"2","C":"234"})

# concatenate(234,34,5,45,"t",0)

def is_all_strings(*args):
    value = False
    for x in args:
        if type(x) == str:
            value = True
        elif type(x) == tuple:
            value = all((type(v) == str for v in x))

    return value


# print(is_all_strings("test",("adf","dfdf","dfdf",22)))

def sum_even_values(*args):
    v = sum(list(k for k in args if k % 2 == 0))
    print(v)


# print(sum_even_values(1,2,3,4,5,6))

def interleave(string1, string2):
    first = [k for k in string1]
    second = [k for k in string2]
    print(first)
    print(second)

    l = ''.join(''.join(x) for x in zip(first, second))
    print(str(l))

    # l= str([map(lambda x, y: chr(x) + chr(y),  first,second)])
    #
    # print(l)


# interleave("hi","ha")

def extract_full_name(lst):
    print(list(map(lambda x: f"{x['first']} {x['last']}", lst)))


names = [{'first': 'Elie', 'last': 'Schoppik'}, {'first': 'Colt', 'last': 'Steele'}]
#extract_full_name(names)


def test():
    names = [{"first": "bro", "last": "shmoe"}, {"first": "bro1", "last": "shmoe2"}]
    # print(list(map(lambda x: x['first'],names)))
    print(list(map(lambda x: x['last'], filter(lambda u: u['first'] == 'bro', names))))


# test()

class Train:
    def __init__(self, cars):
        self.num_cars = cars

    def __repr__(self):
        return str(self.num_cars) + " car train"

    def __print__(self):
        print(self.__repr__())

    def __len__(self):
       return self.num_cars

a_train = Train(4)
a_train.__print__()
print(len(a_train))
print(a_train.__len__())