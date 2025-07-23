vava = 30
punch = 1
knife = 5
gun = 10

condi_1 = int(input("Do you want to attack the monster (1)Fight (2)Run : "))

if condi_1 == 1:
    round = int(input("How many round do you want to attack : "))

    for i in range(round):
        condi_2 = int(input("Do you want to attack the monster (1)Punch (2)Knife (3)Gun : "))

        if condi_2 == 1:
            vava -= punch
        elif condi_2 == 2:
            vava -= knife
        elif condi_2 == 3:
            vava -= gun

        if i+1 <= round and vava < 0:
            print("Health Is Minus!! || Vava Health Reset!  ")
            vava = 20
        if vava == 0:
            print("You win!!") 
            break
        elif i+1 == round and vava > 0:
            print("You lose!!")
            
        print("Boss health remaining :", vava)
else:
    print("You run away")

