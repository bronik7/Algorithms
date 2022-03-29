from pyfiglet import Figlet
from termcolor import colored


# def combine_words(first,second):
#      b = filter(lambda x: x> 10, first)
#      print(list(b))
#      print(list(zip(max(first),max(second))))
#
# combine_words([1,2,3,4,5,6,7,8,9,10,14,44,665],["a","b","c"])

# def interleave(str1,str2):
#     return "".join(''.join(x) for x in zip(str1,str2))
#
# print(interleave("hi","ha"))
#
#
# def extract_fullnames():
#     names = [{'first': 'Elie', 'last': 'Schoppik'}, {'first': 'Colt', 'last': 'Steele'}]
#     full_name=list(filter(lambda b: b[8:-2] == "e", list(map(lambda x: x["first"] + " " + x["last"],names))))
#     str1 = list(map(lambda x: x["first"] + " " + x["last"],names))
#     print(str1[1][8:-2])
#     print(full_name)
#
# extract_fullnames()


def divide(num1, num2):
    try:

        return round(num1 / num2, 2)
    except NameError as err:

        return "Please provide two integers or floats"
    except TypeError as err:
        return "Please provide two integers or floats"
    except ZeroDivisionError as err:
        return "Please do not divide by zero"


# print(colored(divide(4, 3),color="red", on_color="on_blue",attrs=["blink"]))


f = Figlet(font='standard')


# print(colored(f.renderText('Hello World'),
#    color="red", on_color=None, attrs=["blink"]))


def test1():
    with open("test.txt") as f:
        c = f.readlines()
    print(c)
    dictionary = {"lines": len(c)}
    # print( sum(len(k) for k in c))

    # print("words " + str(words))
    dictionary["words"] = sum(len(k.split()) for k in c)
    dictionary["characters"] = sum(len(k) for k in c)
    #
    print(dictionary)


# test1()



