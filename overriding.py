class Parent:

    def phone(self):
        print("nokia 6.1plus")
    def bike(self):
        print("passion pro")

class Child(Parent):
    def phone(self):
        print("iphone 13 promax")

ch=Child()
ch.bike()
ch.phone()