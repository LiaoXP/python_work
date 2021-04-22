import string

def lesser_of_two_evens(num1, num2):
    if num1 % 2 == 0 and num2 % 2 == 0:
        if num1 < num2:
            return num1
        else:
            return num2
    else:
        if num1 < num2:
            return num2
        else:
            return num1

print(lesser_of_two_evens(2,4))

print(lesser_of_two_evens(2,5))

def animal_crackers(text):
    wordlist = text.split()

def makes_twenty(num1, num2):
    if num1 == 20 or num2 == 20:
        return True
    elif num2 + num1 == 20:
        return True
    else:
        return False

print(makes_twenty(20,10))

print(makes_twenty(12,8))



def old_macdonald(name):
    first = name[0].upper()
    fourth = name[3].upper()
    return name[0].upper() + name[1:3] + name[3].upper() + name[4:]

print(old_macdonald('macdonald'))


def master_yoga(text):
    words = text.split()
    reverse = list.reverse((words))
    return reverse

print(master_yoga("We are ready"))


def almost_there(n):
    if abs(n - 200) <= 10:
        return True
    elif abs(n - 100) <= 10:
        return True
    else:
        return False

print(almost_there(90))
print(almost_there(104))
print(almost_there(150))
print(almost_there(209))


def has_33(nums):
    has_first_3 = False
    for num in nums:
        if num == 3:
            if has_first_3:
                return True
            else:
                has_first_3 = True
                continue
        else:
            has_first_3 = False
    
    return False


print(has_33([1, 3, 3]))
print(has_33([1, 3, 1, 3]))
print(has_33([3, 1, 3]))



def paper_doll(text):
    return [c*3 in text]

print(paper_doll("text"))


def blackjack(a,b,c):
    total = 0
    got_11 = False
    for i in a,b,c:
        if i <= 11:
            total += i
            if i == 11:
                got_11 = True
        else:
            return "wrong input"

    if total > 21:
        if got_11:
            total -= 10
            if total > 21:
                return "BUST"
            else:
                return total
        else:
            return "BUST"
    else:
        return total
        

print(blackjack(5,6,7))
print(blackjack(9,9,9))
print(blackjack(9,9,11))



def summer_69(arr):
    if len(arr) == 0:
        return 0
    else:
        total = 0
        hit_6 = False
        hit_9 = False
        for num in arr:
            if num == 6:
                hit_6 = True
                continue
            elif num == 9:
                if hit_6 == True:
                    hit_6 = False
                    continue
                else:
                    total += num
            else:
                if hit_6 == True:
                    continue
                else:
                    total += num

        return total

print(summer_69([1, 3, 5]))
print(summer_69([4, 5, 6, 7, 8, 9]))
print(summer_69([2, 1, 6, 9, 11]))
    

def spy_game(nums):
    count_0 = 0

    for num in nums:
        if num == 7:
            if count_0 == 2:
                return True
            else:
                count_0 = 0
                continue
        elif num == 0:
            if count_0 < 2:
                count_0 += 1

    return False

print(spy_game([1,2,4,0,0,0,0,7,5]))
print(spy_game([1,0,2,4,0,5,7]))
print(spy_game([1,0,7,2,0,4,5,0,2,3,7]))


def count_primes(num):
    count_prime = 1
    current_num = 3

    while current_num <= num:
        divider = 2
        is_prime = True

        while divider <= (current_num/2):
            if current_num % divider == 0:
                is_prime = False
                break
            else:
                divider += 1
        if is_prime:
            count_prime += 1
        
        current_num += 1

    return count_prime

print(count_primes(1000))