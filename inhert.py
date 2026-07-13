# # simple inheritance

# # Base class 

# class Animal:
#     def __init__(self, name):
#         self.name = name

#     def speak(self):
#         print(f"{self.name} makes a sound")

# # Derived class
# class Dog(Animal):
    
#     # def __init__(self):
#     #     self.behaviour = 'Friendly'
#     def speak1(self):
#         print(f"{self.name} barks.")


# #  Create an inheritance of Animal
# animal = Animal("Generic Animal")
# animal.speak() # output generic animal speaks a sound  

# # Create an instance os Dog
# dog = Dog("Buddy")
# dog.speak()



## Super keyword


class Animal:
    def __init__(self):
        self.name = "Buddy"
    
    def speak(self):
        print(f"{self.name} makes a sound")

# Derived class 

class Dog(Animal):
    def __init__(self , bread):
        super().__init__()
        self.bread = bread

    def speak(self):
        super().speak()
        print(f"{self.name} barks. It is a {self.bread}")

dog = Dog("Golden Retriever")
dog.speak()