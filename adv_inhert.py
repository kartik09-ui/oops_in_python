### The first type of inheritance

## Single or Basic inheritance

class Parent:
    def __init__(self, name):
        self.name = name

    def greet(self):
        print(f"Hello, my name is {self.name}")\
        
# Derived class
class child(Parent):
    def play(self):
        print(f"{self.name} is playing.")

# Create an instance of child
child = child("tuppu")
child.greet()
child.play()


#-------------------------------------------------------------------#


## Multilevel inheritance

class GrandParent:

    def __init__(self, name):
        self.name = name

    def tell_story(self):
        print(f"{self.name} is tells a story")


#Intermediate class
class Parent(GrandParent):
    def work(self):
        print(f"{self.name} is working")

# DErived class
class Child(Parent):
    def play(self):
        print(f"{self.name} is playing")


child = Child("Tuppu")
child.tell_story()
child.work()
child.play()


#----------------------------------------------------------------------------#


## Hierarchical Inheritance

class Parent:
    def __init__(self, name):
        self.name = name

    def greet(self):
        print(f"Hello my name is {self.name}")


# Derived class 1
class Child1(Parent):
    def play(self):
        print(f"{self.name} is playing")

# Derived class 2
class Child2(Parent):
    def study(self):
        print(f"{self.name} is studying")

# Create a instance of child1 and child2 
child1 = Child1("gunnu")
child2 = Child2("tuppu")

child1.greet()
child1.play()

child2.greet()
child2.study()


#-----------------------------------------------------------------------------------------#


## Multiple Inheritance

class A:
    def __init__(self, name):
        self.name = name

    def greet(self):
        print(f"Hello my name is {self.name}")

# Intermediate class 1

class B(A):
    def greet(self):
        print(f"Hello from B, {self.name}")
        super().greet()

# Intermediate class 2

class C(A):
    def greet(self):
        print(f"Hello from C, {self.name}")
        super().greet()

# Derived class

class D(B, C):
    def greet(self):
        print(f"Hello from D, {self.name}")
        super().greet()

# Create an instance for D 
d = D("Kartik")
d.greet()


# -----------------------------------------------------------------------------------------------#


## Hybrid Inheritance

class Animal:
    def __init__(self, name):
        self.name = name

    def sound(self):
        print(f"{self.name} make a sound")

# Intermediate class1 (Hierarchical)
class Mammal(Animal):
    def feed(self):
        print(f"{self.name} is feeding milk")

#Intermediate class2 (Multiple)

class Bird(Animal):
    def fly(self):
        print(f"{self.name} is flying")

# Derived class Multiple inheritance

class Bat(Mammal, Bird):
    def __init__(self, name):
        Mammal.__init__(self, name)


    def nocturnal(self):
        print(f"{self.name} is nocturnal")


# Create an instance for bat

bat = Bat("Bruce")
bat.sound()
bat.feed()
bat.fly()
bat.nocturnal()