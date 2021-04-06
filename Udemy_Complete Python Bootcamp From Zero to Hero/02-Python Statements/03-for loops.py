list1 = [1,2,3,4,5,6,7,8,9,10]

for num in list1:
    print(num)


for num in list1:
    if num % 2 == 0:
        print(num)
    else:
        print("odd")

list_sum = 0

for num in list1:
    list_sum = list_sum + num

print(list_sum)

d = {'k1':1,'k2':2,'k3':3}

for item in d:
    print(item)

print(d.items())

for k,v in d.items():
    print(k)
    print(v)

print(list(d.keys()))

print(list(d.values()))