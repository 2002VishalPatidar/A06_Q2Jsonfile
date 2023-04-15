
class Dog():
    def __init__(self,name,age,coatcolor):
        self.name=name
        self.age=age
        self.coatcolor=coatcolor

    def description(self):
        print("name:",self.name)
        print("age:",self.age)

    def  get_info(self):
        print("Colour:",self.coatcolor)

class  JackRussellTerrier(Dog):
    def MoodFun(self):
        print("Dancing")
    def woof(self):
        print("woof woof......")


class BullDog(Dog):
    def Hungry(self):
        print("Eating...")
    def  Rest(self) :
        print("Sleeping....")

    
a=input("Enter a obj1 name:")
b=eval(input("Enter a obj1 age:"))
c=input("Enter a  obj1 coatcolor:")
obj1=Dog(a,b,c)
obj1.description()
obj1.get_info()
print()
a=input("Enter a obj2 name:")
b=eval(input("Enter a obj2 age:"))
c=input("Enter a  obj2 coatcolor:")
obj2=JackRussellTerrier(a,b,c)
obj2.description()
obj2.get_info()
obj2.MoodFun()
obj2.woof()
print()
a=input("Enter a obj3 name:")
b=eval(input("Enter a obj3 age:"))
c=input("Enter a  obj3 coatcolor:")
obj3=BullDog(a,b,c)
obj3.description()
obj3.get_info()
obj3.Hungry()
obj3.Rest()