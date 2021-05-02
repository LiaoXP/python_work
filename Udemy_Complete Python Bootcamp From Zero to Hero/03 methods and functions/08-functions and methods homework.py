from math import pi
import string
def vol(rad):
    return 4/3 * pi * rad**3

print(vol(2))



def ran_check(num, low, high):
    if num >= low and num <= high:
        return True
    else:
        return False

print(ran_check(5,2,7))



def up_low(s):
    upper = 0
    lower = 0

    original = s

    for c in original:
        if c.isupper():
            upper += 1
        elif c.islower():
            lower += 1
    
    print(f"original string : {original}")
    print(f"no. of upper case characters : {upper}")
    print(f"no. of lower case characters : {lower}")

s = 'Hello Mr. Rogers, how are you this fine Tuesday?'
up_low(s)


def unique_list(lst):
    uni_lst = list(set(lst))
    print(uni_lst)

unique_list([1,1,1,1,2,2,3,3,3,3,4,5])


def multiply(numbers):
    result = 1.0

    while len(numbers) > 0:
        result *= numbers.pop()

    print(result)

multiply([1,2,3,-4])


def palindrome(s):
    lst = list(s)

    if len(lst) == 0:
        print(False)
    elif len(lst) == 1:
        print(True)
    else:
        while len(lst) > 1:
            if lst.pop(0) != lst.pop(len(lst) - 1):
                print(False)
                return
        print(True)

palindrome('helrjleh')
palindrome('')
palindrome('u')

def ispangram(str1, alphabet=string.ascii_lowercase):
    set_str = set(str1.replace(" ", ""))
    set_alphabet = set(alphabet)

    print(f"str: {set_str}")
    print(f"alphabet: {set_alphabet}")

    print(set_alphabet.issubset(set_str))


ispangram("The quick brown fox jumps over the lazy dog")
