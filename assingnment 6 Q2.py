
class Dog:

    def __init__(self, name, age, coat_colour):
        self.name = name
        self.age = age
        self.coat_colour = coat_colour

    def description(self):
       print("Dog Name is :",self.name)
       print("Dog Age is :",self.age,end="")
       return ""

    def get_info(self):
       print("Dog Colour is :",self.coat_colour)
       return ""

class JackrusselTerrier(Dog): 
    def __init__(self, name, age, coat_colour):  
        super().__init__(name, age, coat_colour)
    
    def description(self):
        return super().description()

    def get_info(self):
        return super().get_info()

class BullDog(Dog):
    def __init__(self, name, age, coat_colour):  
        super().__init__(name, age, coat_colour)

    def description(self):
       return super().description()   

    def get_info(self):
        return super().get_info()

H = JackrusselTerrier("Micky",5,"White")
print(H.description())
print(H.get_info())

S = BullDog("Leo",3,"Black")
print(S.description()) 
print(S.get_info())

