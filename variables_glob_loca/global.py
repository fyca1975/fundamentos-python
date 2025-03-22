x = 5 #variable global
def modify_global():
    global x
    x += 10
    print(x)
modify_global()
print(x)