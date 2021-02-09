


# userNames = ["admin", "xp", "rx", "sr", "so"]

# userNames = []


# if userNames:
#     for userName in userNames:
#         if userName == "admin":
#             print("hello " + userName + ", would you like to see admin")
#         else:
#             print("hello " + userName + ", would you like to log in")
# else:
#     print("user needed!")
    
numbers = list(range(1,10))

for number in numbers:
    if number == 1:
        print(str(number) + "st")
    elif number == 2:
        print(str(number) + "nd")
    elif number == 3:
        print(str(number) + "rd")
    else:
        print(str(number) + "th")