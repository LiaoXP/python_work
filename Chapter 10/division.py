# try:
#     print(5/0)
# except ZeroDivisionError:
#     print("you cannot divide by zero")



print("give me two numbers, and i will divide them")

print("enter 'q' to quit")

while True:
    first_number = input("\nfirst number: ")
    if first_number == "q":
        break
    second_number = input("second number: ")
    if second_number == "q":
        break
    try:
        answer = int(first_number) / int(second_number)
    except:
        print("you cannot divide by zero")
    else:
        print(answer)
    
