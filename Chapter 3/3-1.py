names = ["jack", "tao", "yinxi"]

names

print(names[0].title() + ", " + names[1].title() + " and " + names[2].title() + " are my friends.")


names.append("liao")

names.insert(1, "felix")


print(sorted(names))


#names.sort(reverse = True)

names.reverse()

print(names)

names.reverse()

print(names[len(names) - 1])




for name in names:
	print(name)
