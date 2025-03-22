x = 'global' # global variable

#funcion externa
def outer_function():
    x = 'enclosing' # enclosing variable

    #funcion interna
    def inner_function():
        x = 'local' # local variable
        print(f'inner {x}')

    inner_function()
    print(f'outer {x}') 

outer_function()
# Output: inner local
print(f'global {x}')
# Output: global