st = 'Print only the words that start with s in this sentence'

lst_words = st.split()

print(lst_words)

for word in lst_words:
    if word.startswith("s"):
        print(word)

for x in range(11):
    if x % 2 == 0:
        print(x)

print([x for x in range(1, 51) if x % 3 == 0])

st = 'Print every word in this sentence that has an even number of letters'

lst_words = st.split()

for word in lst_words:
    if len(word) % 2 == 0:
        print(f'len of word "{word}" is even')



for integer in range(1, 101):
    if integer % 3 == 0 and integer % 5 == 0:
        print("fizz buzz")
    elif integer % 3 == 0:
        print("fizz")
    elif integer % 5 == 0:
        print("buzz")
    else:
        print(integer)


st = 'Create a list of the first letters of every word in this string'

print([word[0] for word in st.split()])