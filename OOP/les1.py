



class Pet:
    def __init__(self, name, age):
            self.name = name 
            self.age = age
    def show(self):
        return f"Name: {self.name}, Age: {self.age} years old"



class Dog(Pet):
    
    def bark(self):
        return f"{self.name} says Woof!"    


class Cat(Pet):
    def __init__(self, name, age, color):
        self.color = color
        super().__init__(name, age)

        

    def meow(self):
        return f"{self.name} says Meow!"
    def paks(self):
        return self.color
    def show(self):
        return f"Name: {self.name}, Age: {self.age} years old, {self.color}"
    


s = Dog("pibu", 23)
s1 = Cat("rumal", 23, "red")
print(s.show())
print(s.bark())
print(s1.paks())
