class Computer:
    # no need to declare static variables with static keyword before
    # variables inside class and outside __init__ are considered static
    no_of_cpus = 1  # static variable

    # no need to declare instance variables like in java
    # variables assigned inside __init__ are instance variables
    def __init__(self, cpu, ram):
        self.cpu = cpu
        self.ram = ram

    def config(self):
        print(self.cpu, self.ram)

    # instance method types
    # accessor methods - only fetch value (getter)
    # mutator methods - changes values (setter)

    # class method - can only access class variables (i.e static variables)
    # you have to pass cls instead of self to class methods
    @classmethod  # decorator
    def print_class_vars(cls):
        print('classmethod: ', cls.no_of_cpus)

    # static method - not related to instance or class variables
    # so no need to pass self or cls as parameter while declaring
    # it generally is a utility or library function
    @staticmethod
    def do_something():
        print('staticmethod: I am a utility')


# main execution

# create instance
comp1 = Computer('intel', '8')

# valid ways to call instance methods
# using class and pass obj
Computer.config(comp1)
# using object
comp1.config()

# valid ways to call static variables
# using instance
print('class var by instance: ', comp1.no_of_cpus)
# using class
print('class var by class: ', Computer.no_of_cpus)

# calling a class method
# if a class method doesn't have decorator @classmethod while declaring
# calling it with class name or instance raises an error
Computer.print_class_vars()
comp1.print_class_vars()

# calling a static method
# if a class method doesn't have decorator @staticmethod while declaring
# calling it with class name or instance raises an error
Computer.do_something()
comp1.do_something()
