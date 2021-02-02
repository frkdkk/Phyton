

name = "faruk"
age = 20

def hello():
    name = "mahmut"
    age = 10
    message=f"benim adım {name} ve {age} yaşındayım "
    print(message)

hello()

def hello():
    name = "mahmut"
    age = 10
    return f"benim adım {name} ve {age} yaşındayım "
    

print(hello())
print(name)
print(age)


x="global"

def myfunc():
    x="local"
    return x

print(x)
print(myfunc())


x = "global level"

def enclosing():       #LEGB  1-Local 2-Enclosing 3-Global 4-Built in
    x ="enclosing level"
    def innerfunc():
        x="local level"
        print(x)
    innerfunc()
enclosing()

