

#MOdify a global variable.

enemies = 1

def increase_enemies():
    #global enemies
    #enemies = 2
    print(f"enemies inside function: {enemies}")
    return enemies + 1

    
enemies = increase_enemies()
print(f"enemies outside function: {enemies}")

#Global constants are conventionally UpperCase in python.

URL = "WWW.google.com"
print(URL)
