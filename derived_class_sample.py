class Person(object):
        """docstring for ClassName"""  
        def __init__(self, first_name, second_name, pay):
                self.first_name = first_name
                self.second_name = second_name
                self.pay = pay
                self.rise = 1.3
 
        def give_rise(self):
                self.pay = self.pay * self.rise
                return self.pay
 
class Manager(Person):
        def __init__(self, first_name, second_name, pay):
                Person.__init__(self, first_name, second_name, pay)
                self.rise = 1.5
 
 
eng1 = Person(first_name='Serg', second_name='Lee', pay=100)
eng2 = Person(first_name='Bill', second_name='Ross', pay=100)
 
man1 = Manager(first_name='Sam', second_name='Dou', pay=100)
man2 = Manager(first_name='Fran', second_name='Dou', pay=100)
 
print (eng1.pay)
print (eng1.give_rise())
print (eng1.pay)
 
print (man1.pay)
print (man1.give_rise())
print (man1.pay)
