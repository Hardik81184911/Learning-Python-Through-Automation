#use def to create a function
def hello():
    print('sup', end= ' ')
    print('sup2', end= ' ')
    print('sup3')
    print('sup4', 'sup5', 'sup6')
    print('separation1', 'separation2', sep = "-")
#function call must come after defining function
hello()
hello()
hello()
#when another function with the same name is created the original one is lost
def hello(name,var2):
    print('so methods can\'t be overloaded in python')
#strangely enough the interpreter will call the method even
#without proper parameters
hello(None, None)
