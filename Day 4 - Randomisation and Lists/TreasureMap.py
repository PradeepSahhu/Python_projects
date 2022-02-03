
#Treasure map
# 🚨 Don't change the code below 👇
row1 = ["⬜️","⬜️","⬜️"]
row2 = ["⬜️","⬜️","⬜️"]
row3 = ["⬜️","⬜️","⬜️"]
map = [row1, row2, row3]
print(f"{row1}\n{row2}\n{row3}")
position = input("Where do you want to put the treasure? ")
# 🚨 Don't change the code above 👆

#Write your code below this row 👇

position_of_list = int(position[1]) - 1
position_of_element = int(position[0]) - 1
#print(f"{position_of_list} and {position_of_element}")

'''if(position_of_list == 0):
    row1[position_of_element] = 'X'
elif(position_of_list == 1):
    row2[position_of_element] = 'X'
elif(position_of_list == 2):
    row3[position_of_element] = 'X'
else:
    print(f"Errow please enter between 11 to 33")
'''
#Alternative way...
map[position_of_list][position_of_element] = "X"



#Write your code above this row 👆

# 🚨 Don't change the code below 👇
print(f"{row1}\n{row2}\n{row3}")
