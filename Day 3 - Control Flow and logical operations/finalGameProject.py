

#Game project...

'''dtion = input("left or right? ").lower()
if(dtion=='left'):
    print("game over")
if(dtion=='right'):
    dti=input("swim or walk?").lower()
    if(dti=='swim'):
        print("game over")
    if(dti=='walk'):
        dt=input("drink or eat?").lower()
        if(dt=='drink'):
            print("game over")
        if(dt=='eat'):
            d=input("choose between red, blue or black?").lower()
            if(d=='black'):
                print("game over")
            if(d=='blue'):
                print("game over")
            if(d=='red'):
                print("Game won")
'''
#Alternative way with first word capital...
dtion = input("left or right? ")
v = dtion[0].upper()+dtion[1:len(dtion)].lower()
print(v)
if(v=='Left'):
    print("game over")
if(v=='Right'):
    dti=input("swim or walk?")
    c = dti[0].upper()+dti[1:len(dti)].lower()
    if(c=='Swim'):
        print("game over")
    if(c=='Walk'):
        dt=input("drink or eat?")
        a = dt[0].upper()+dt[1:len(dt)].lower()
        if(a=='Drink'):
            print("game over")
        if(a=='Eat'):
            d=input("choose between red, blue or black?")
            z = d[0].upper()+d[1:len(d)].lower()
            if(z=='Black'):
                print("game over")
            if(z=='Blue'):
                print("game over")
            if(z=='Red'):
                print("Game won")

