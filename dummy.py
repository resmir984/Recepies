#apps divided into layout html,data: models,functionality  logic/business logic:views


# list=[]
# dict={}
# lst=[10,20,30,40,50]
# lst.append(40)
#
# #
# append()

#object oriented programming
# list
# dict
# tuple
# set
#
# class list:
#     append()
#     insert()
#     pop()
#
# ls=list()
# ls.append
# ls.pop
#
# class dict:
#
# class tuple:
#
# class set:



# from builtins import *
# ls=list()   ==>constructor initialize

#
# functions:--
# print()  input()  sum()
# max()  min()  len()
#sorted()
# classes:--
#dict
#tuple
#set
#string

#lst=[]==>parent class

# class Person:
#     name:str
#     age:int
#     place:str
#     gender:str
#
#     def set_person(self,**kwargs):
#         self.name=kwargs.get("name")
#         self.age=kwargs.get("age")
#         self.place=kwargs.get("place")
#         self.gender=kwargs.get("gender")
#
#     def print_person(self):
#         print("personname=",self.name,"age=",self.age,"place=",self.place,"gender=",self.gender)
#
# p=Person()
# p.set_person(name="ram",age=23,place="tsr",gender="male")
# p.print_person()


#constructor==>for instance variable initialize

#all class's parent class==>object(all contents on obj can get into classes too)

class Person:
    name:str
    age:int
    place:str
    gender:str

    def __init__(self,**kwargs):
        self.name=kwargs.get("name")
        self.age=kwargs.get("age")
        self.place=kwargs.get("place")
        self.gender=kwargs.get("gender")

    def print_person(self):
        print("personname=",self.name,"age=",self.age,"place=",self.place,"gender=",self.gender)


    def __str__(self):
        return self.name

p=Person(name="ram",age=23,place="tsr",gender="male")

#p.print_person()

print(p)


#reference  __str__()
