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

class Dog(Animal):
    def __init__(self,breed,name,food_type,color):
        super().__init__(food_type,color)
        self.dog_breed = breed
        self.dog_name = name

    def bark(self):
        print("wooofff....")
    def security(self):
        print("My dog is my home security")

mydog = Dog("Brown","Jian","Bulldog", "Meat")
 # Accessing attributes of the instance
print(mydog.dog_breed)
print(mydog.dog_name)
    # Calling methods of the instance
mydog.eat()

class Cat(Animal):
    def __init__(self,breed,name):
        self.cat_breed = breed
        self.cat_name = name
    def Meaw(self):
        print("meawwwww...")

#mycat = Cat("abc","xyz")
#mycat.eat()
#mycat.Meaw()
