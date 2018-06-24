def spam():
    eggs = 99
    bacon()
    print(eggs)
def bacon():
    ham = 101
    eggs = 0
spam()
eggs = 'after first call'
def spam():
    print(eggs)
spam()
def spam():
    global eggs
    eggs = 10
    print(str(eggs))
spam()