# class Person:
#     age=32
#     name="Liza"

#     def get_name(self):
#         print(f'my name is (self.name)')

# p=person()      #object person
# p2=person(34,"ABC")

# p.get_name()
# print(p.age)

# p2.age

class Person:
    def __init__(self,name="ABC",age=32):
        self.age=age
        self.name=name 


    def get(self):
        print("calling here",self.name,self.age)

    def __str__(self):
        return ("My name is")


p=Person(age=22)      #object Person
p2=Person(age=34,name="Liza")
p3=Person(50,"Alina")

print(p.age)

print(p2.age)

print("Person",p.name)
print("Person num 2",p2.name)
print("Person num 3",p3.name,p3.age)


print(p.get())
print(Person.get(p2))







