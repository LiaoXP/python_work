def even_check(number):
    return number % 2 == 0

print(even_check(20))

print(even_check(15))

def check_even_list(num_list):
    for number in num_list:
        if number % 2 == 0:
            return True
        else:
            pass

print(check_even_list([1,2,3]))

print(check_even_list([1,1,1]))

work_hours = [('Abby',100),('Billy',400),('Cassie',800)]

def employee_check(work_hours):
    current_max = 0

    employee_of_month = ""

    for employee, hours in work_hours:
        if hours > current_max:
            current_max = hours
            employee_of_month = employee
        else:
            pass

    return (employee_of_month, current_max)

print(employee_check(work_hours))






example = [1,2,3,4,5]

from random import shuffle

shuffle(example)

print(example)




mylist = [' ','O',' ']

def shuffle_list(mylist):
    shuffle(mylist)

    return mylist

print()


def player_guess():

    guess = ""

    while guess not in ['0','1','2']:

        guess = input("pick a number: 0, 1, 2: ")

    return int(guess)

def check_guess(mylist, guess):
    if mylist[guess] == "0":
        print("correct guess")
    else:
        print("wrong")
        print(mylist)

mylist = [' ','O',' ']

mixedup_list = shuffle_list(mylist)

guess = player_guess()

check_guess(mixedup_list, guess)