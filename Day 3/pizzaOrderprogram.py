

#Pizza order program...
order = input("What size of pizza you want? S, M or L ")
add = input("Do you want pepperani? ")
cheese = input("Do you want cheese? ")
bill = 0
if(order == 'S'):
    bill = 15
    print(f"price for small size pizza is: ${bill}")
    
    if(add == 'Y'):
        bill +=2
        print(f"price for pizza with pepperani is: {bill}")
elif(order == 'M'):
    bill = 20
    print(f"price for medium size pizza is: ${bill}")
    
    if(add == 'Y'):
        bill +=3
        print(f"price for pizza with pepperani is: {bill}")
elif(order == 'L'):
    bill = 25
    print(f"price for large size pizza is: ${bill}")
    
    if(add == 'Y'):
        bill +=3
        print(f"price for pizza with pepperani is: {bill}")
        
if(cheese == 'Y'):
    bill+=1

print(f"final price is: ${bill}")

    
