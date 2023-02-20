class Person:
    def set_name(self, name):
        self.name = name

    def set_age(self, age):
        self.age = age

    def set_gender(self, gender):
        self.gender = gender

    def get_name(self):
        return self.name

    def get_age(self):
        return self.age

    def get_gender(self):
        return self.gender

    def print_info(self):
        print("name", self.name, "age:",self.age, "gender:",self.gender)






person1= Person()
person1.set_name("Enock")
person1.set_age("17")
person1.set_gender("Male")

person2= Person()
person2.set_name("Alice")
person2.set_age("30")
person2.set_gender("Female")

person1.print_info()
person2.print_info()



voter1= Person()
voter1.set_name("Alice")
voter1.set_age(30)
voter1.set_gender("Female")

try:
    voter1.get_age() >= 18
    print("Eligible to vote")
except:
    print("Not eligible to vote")
finally:
    print("Thanks for visiting IEBC")





