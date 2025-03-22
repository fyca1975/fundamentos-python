x = 100 

def local_function():
    x = 10  # local variable
    print(f'local {x}')

def global_function():
    print(f'Global variable x: {x}')

local_function()
# Output: 10
global_function()
# Output: 100
