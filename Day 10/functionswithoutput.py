

#functions with outputs.

'''def my_function():
    result = 3*2
    return result
output = my_function()
print(output)
'''
#using no function. title case.
'''
def format_name(f_name, l_name):
    formated_name = ""
    formated_name = f_name[0].upper() + f_name[1:].lower()
    formated_name += " " + l_name[0].upper() + l_name[1:].lower()
    return formated_name


f_name = input("Enter your first name: ")
l_name = input("Enter your last name: ")
output = format_name(f_name, l_name)
print(output)
'''
#using title() function. title case.
def format_name(f_name, l_name):
    #formated_name = f_name.title() + " " + l_name.title()
    #return formated_name

    
    formated_f_name = f_name.title()
    formated_l_name = l_name.title()
    
    
    return f"{formated_f_name} {formated_l_name}"


f_name = input("Enter your first name: ")
l_name = input("Enter your last name: ")
output = format_name(f_name, l_name)
print(output)

