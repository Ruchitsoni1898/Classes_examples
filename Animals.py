import pdb
class Animal:
    def __init__(self,color,food_type):
        self.color = color
        self.food_type = food_type
        print("I am init")

    def move(self):
        print("Animal moves")
    def eat(self):
        print("Animal eats")
        print("This animal eats {}".format(self.food_type))
    def breath(self):
        print("Animal breaths")
my_animal1 = Animal("blue","Non-veg")
print(f"color of animal1:{my_animal1.color}")
print(my_animal1.move())
print(my_animal1.eat)
my_animal2 = Animal("Yellow","Vegan")
my_animal2.eat()
print(f"color of animal2:{my_animal2.color}")
print(my_animal1)
print(my_animal2)

pdb.set_trace()