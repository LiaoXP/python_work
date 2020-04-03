



while True:
    first_number = input("input first integer: ")
    second_number = input("input second integer: ")

    try:
        first_number = int(first_number)
        second_number = int(second_number)
    except ValueError:
        print("one of both ur input number(s) is/are not a valid integer")
    else:
        sum = first_number + second_number
        print(sum)
        break