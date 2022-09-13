class ClassName:
# Fundamental Methods
    def __init__(self, ...):
        # initialize new instance's fields
        # no return
    def __repr__(self):
        return # string used by the interpreter to print instances
    def __str__(self):
        return # string used by print and str
# Predicates
    def __lt__(self, other):
        if type(self) != type(other):
            raise Exception('Incompatible argument to __lt__: ' + str(other))
        return self.somemethod() < other.somemethod()
    
    def is_some_characteristic(self):
        return # True or False
# Access Methods
    def get_something(self):
        return # value obtained by one of:
               # accessing a field
               # lookup by key
               # computation
               # filtering a collection
               # searching a collection
# Modification Methods
    def set_something(self, ...):
        # change the value of one or more fields based on
        # the parameter values supplied in the call.
        # generally no return value
# Action Methods
    def do_something(self, ...):
        # do something that has effects outside the class

# Private Support Methods
    def helper_method(self, ...):
        # something used by other methods of the class only