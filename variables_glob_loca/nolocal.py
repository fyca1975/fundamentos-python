def outer_function():
    x = 'enclosing'
    def inner_function():
        nonlocal x
        x = 'modified'
        print('inner_function:', x)
    inner_function()
    print('outer_function afuera:', x)

outer_function()
# inner_function: modified