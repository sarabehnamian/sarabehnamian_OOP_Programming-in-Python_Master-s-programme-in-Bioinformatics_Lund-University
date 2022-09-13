class HelloWorld : # Convention to start with capital letter
    
    def __init__ (self , attribute = "" ): #"" is default value of attribute
        self . instance_var = attribute
    
    def get_name ( self ): # We can retrieve information from the objects
        return f'Hello World {self . instance_var}'

my_first_instance = HelloWorld()
my_second_instance = HelloWorld('Sara')

print ( my_first_instance . get_name())
print ( my_second_instance . get_name())
