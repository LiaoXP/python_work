# def lesser_of_two_evens(a,b):
#     if a%2 == 0 and b%2 == 0:
#         if a<b:
#             return a
#         else:
#             return b
#     else:
#         if a<b:
#             return b
#         else:
#             return a

# print(lesser_of_two_evens(7,5))

# def animal_crackers(text):
#     list_of_words = text.split(" ")
#     if list_of_words[0][0].upper() == list_of_words[1][0].upper():
#         return True
#     else:
#         return False
    

# print(animal_crackers("hello Hello"))

# def makes_twenty(n1,n2):
#     if n1 == 20 or n2 == 20:
#         return True
#     elif sum((n1, n2)) == 20:
#         return True
#     else:
#         return False

# print(makes_twenty(20,10))
# print(makes_twenty(12,8))
# print(makes_twenty(2,3))

# def old_macdonald(name):
#     converted_name = ""
#     for i in range(len(name)):
#         if i == 0 or i == 3:
#             converted_name += name[i].upper()
#         else:
#             converted_name += name[i].lower()
    
#     return converted_name

# print(old_macdonald("macdonald"))



# def master_yoda(text):
#     reversed_list = text.split(" ")
#     reversed_list.reverse()
    
#     return " ".join(reversed_list)

# print(master_yoda("i am home"))



# def almost_there(n):
#     if (n>=(100-10) and n<=(100+10)) or (n>=(200-10) and n<=(200+10)):
#         return True
#     else:
#         return False

# print(almost_there(89))


# def has_33(nums):
    
#     for i in range(len(nums)):
#         if i == len(nums) - 1:
#             return False
#         else:
#             if nums[i] == 3:
#                 if nums[i + 1] == 3:
#                     return True
#                 else:
#                     continue
#     return False

# print(has_33([1,3,3]))
# print(has_33([1, 3, 1, 3]))
# print(has_33([3, 1, 3]))



# def paper_doll(text):
#     converted_string = ""

#     for i in range(len(text)):
#         for j in range(3):
#             converted_string += text[i]
    
#     return converted_string

# print(paper_doll('Mississippi'))


# def blackjack(a,b,c):
#     input = (a,b,c)

#     if sum(input) <= 21:
#         return sum(input)
#     elif 11 in input:
#         return sum(input) - 11
#     else:
#         return "BUST"

# print(blackjack(9,9,11))


# def summer_69(arr):
#     sum = 0
#     if len(arr) == 0:
#         return sum
#     else:
#         has_met_six_but_not_nine_yet = False
#         for i in range(len(arr)):
#             if arr[i] != 6 and has_met_six_but_not_nine_yet == False:
#                 sum += arr[i]
#             else:
#                 has_met_six_but_not_nine_yet = True
#                 if arr[i] == 9:
#                     has_met_six_but_not_nine_yet = False
#                 else:
#                     continue
#     return sum            

# print(summer_69([4, 5, 6, 7, 8, 9,11, 6, 7, 8, 9]))


# def spy_game(nums):
#     james_bond = []

#     for i in range(len(nums)):
#         if nums[i] in (7, 0):
#             james_bond.append(nums[i])
#         else:
#             continue
#     print(james_bond)
#     if james_bond == [0,0,7]:
#         return True
#     else:
#         return False

# print(spy_game([1,7,2,0,4,5,0]))


# def count_primes(num):
#     print(range(num))
#     count = 4
#     for i in range(num):
#         if i in [0,1,2,3,5,7]:
#             continue
#         elif i%2 == 0 or i%3 == 0 or i%5 == 0 or i%7 == 0:
#             continue
#         else:
#             count += 1
#     return count

# print(count_primes(101))


# def print_big(letter):
#     character_mapping = {"a":"  *  \n * * \n*****\n*   *\n*   *",
#                         "b":"**** \n*   *\n****\n*   *\n**** ",
#                         "c":"  *  \n * * \n*****\n*   *\n*   *",
#                         "d":"  *  \n * * \n*****\n*   *\n*   *",
#                         "e":"  *  \n * * \n*****\n*   *\n*   *"}

#     return character_mapping[letter]

# print(print_big("b"))

# import math
# def vol(rad):
#     return rad**3*math.pi*4/3

# print(vol(2))

# def ran_check(num,low,high):
#     return num >= low and num <= high

# print(ran_check(9,2,7))


# def up_low(s):
#     low_count = 0
#     high_count = 0
#     for letter in s:
#         if letter.isupper():
#             high_count += 1
#         elif letter.islower():
#             low_count += 1
#     print("the input string is " + s + "\nlower count is " + str(low_count) + "\nupper count is " + str(high_count))

# s = 'Hello Mr. Rogers, how are you this fine Tuesday?'
# up_low(s)


# def unique_list(lst):
#     unique_list = []

#     for i in lst:
#         if i in unique_list:
#             continue
#         else:
#             unique_list.append(i)
    
#     return unique_list

# print(unique_list([1,1,1,1,2,2,3,3,3,3,4,5]))


# def multiply(numbers):
#     base = 1

#     for i in numbers:
#         base *= i

#     return base

# print(multiply([1,2,3,-4]))


# def palindrome(s):
#     after_replace_space = s.replace(" ", "")

#     for after_replace_space[0] 

#     #return after_replace_space[0:round(len(after_replace_space)/2)]

#     #return after_replace_space[::-2]



# print(palindrome('nurses run'))

import string
def ispangram(str1, alphabet=string.ascii_lowercase):
    lowercase_set = set(alphabet)
    
    str1_list = []

    for i in str1.replace(" ", ""):
        # if i.lower() not in str1_list:
        str1_list.append(i)
    
    str1_set = set(str1_list)

    print(lowercase_set)
    print(str1_set)
    print(lowercase_set == str1_set)

print(ispangram("The quick brown fox jumps over the lazy dog"))