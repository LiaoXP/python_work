class Restaurant():

    def __init__(self, restaurant_name, cuisine_type):
        self.restaurant_name = restaurant_name

        self.cuisine_type = cuisine_type

        self.number_served = 0

    def describe_restaurant(self):
        print("restaurant name is " + self.restaurant_name)

        print("cuisine type is " + self.cuisine_type)

    def open_restaurant(self):
        print(self.restaurant_name + " is open")

    def set_number_served(self, number_served):
        self.number_served = number_served
         
    

restaurant = Restaurant("beef noodle", "noodle")

print(str(restaurant.number_served) + " people have been served here")

restaurant.number_served = 5

print(str(restaurant.number_served) + " people have been served here")

restaurant.set_number_served(77)

print(str(restaurant.number_served) + " people have been served here")
# print(restaurant.restaurant_name)

# print(restaurant.cuisine_type)

# restaurant.describe_restaurant()

# restaurant.open_restaurant()