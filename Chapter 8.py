# def hello():
#     print("hello")

# hello() 

# def make_album(singerName, albumName, songCount = 0):
#     album = {}

#     album[singerName] = albumName

#     if songCount != 0:
#         album[""]


#     return album

# singerName = input("Input singer name:")

# albumName = input("Input album name:")

# print(make_album(singerName, albumName))


# def ingredients(*ingredients):
#     print("ingredients:")

#     for ingredient in ingredients:
#         print(ingredient)


# ingredients("beef", "tomato", "vege")


def build_profile(given_name, family_name, **otherDetails):
    profile = {}

    profile["given_name"] = given_name

    profile["family_name"] = family_name

    for key, value in otherDetails.items():
        profile[key] = value

    print(profile)

build_profile("xp", "liao", age = 30, gender = "male", how = "good")