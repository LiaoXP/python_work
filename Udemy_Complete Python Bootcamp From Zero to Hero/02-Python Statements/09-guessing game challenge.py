from random import randint

answer_to_the_riddle = randint(1, 101)
count = 1
diff = 0

while True:
    user_input = int(input("pls guess and input: "))

    if user_input < 1 or user_input > 100:
        print("out of bound")
    else:
        if user_input == answer_to_the_riddle:
            print(f"BINGO! You've taken {count} guess(es) to get it.")
            break
        else:
            if count == 1:
                diff = abs(user_input - answer_to_the_riddle)
                if diff <= 10:
                    print("warm")
                else:
                    print("cold")
            else:
                new_diff = abs(user_input - answer_to_the_riddle)
                if new_diff < diff:
                    print("warmer")
                else:
                    print("colder")
                diff = new_diff

        count += 1


