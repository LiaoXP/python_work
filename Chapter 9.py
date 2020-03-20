class Restaurant():

    def __init__(self, restaurant_name, cuisine_type):
        self.restaurant_name = restaurant_name

        self.cuisine_type = cuisine_type

    def describe_restaurant(self):
        print("restaurant name is " + self.restaurant_name)

        print("cuisine type is " + self.cuisine_type)

    def open_restaurant(self):
        print(self.restaurant_name + " is open")


restaurant = Restaurant("beef noodle", "noodle")

print(restaurant.restaurant_name)

print(restaurant.cuisine_type)

restaurant.describe_restaurant()

restaurant.open_restaurant()