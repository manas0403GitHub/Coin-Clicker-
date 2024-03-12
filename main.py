import os, time

i = ""
score = 0
Costs_of_Auto = {"Auto Money x1": 15, "Auto Money x5": 25, "Auto Money x10": 30, "Auto Money x20": 40, "Auto Money x50": 70, "Auto Money x70": 100, "Auto Money x90": 150, "Auto Money x100": 170}
buyed_of_Auto = []
AutoAmount = 0

Costs_of_Click = {"Click Amount +1": 10, "Click Amount +5": 15, "Click Amount +10": 25, "Click Amount +15": 30, "Click Amount +25": 45, "Click Amount +40": 60, "Click Amount +70": 80, "Click Amount +90": 100, "Click Amount +100": 150}
buyed_of_Click = []
ClickAmount = 1

SrNo = 0

os.system('cls' if os.name == 'nt' else 'clear')

def menu():
    print(f"{i: ^125}💰Coin Clicker!💰")
    print("""What do you want to Enter?
        C(Click)👆, S(Shop)🛒, E(Exit)❌""")
    
    global Enter
    Enter = ""
    Enter = input("Enter: ")
menu()

if Enter == 'C':
    while True:
        os.system('cls' if os.name == 'nt' else 'clear')
        print("Score: ", score)
    
        EnterClick = input("CL(Click)👆,E(Exit)❌, Buyed Powerups(BP)👍")
        score += AutoAmount

        if EnterClick == 'CL':
            score += ClickAmount
            time.sleep(0.3)
            continue

        elif EnterClick == 'E':
            print("Back to Menu...")
            time.sleep(0.5)
            os.system('cls' if os.name == 'nt' else 'clear') 
            menu()

        elif EnterClick == 'BP':
            print("Opening....")
            time.sleep(0.5)
            os.system('cls' if os.name == 'nt' else 'clear') 
            for index in buyed_of_Auto:
                SrNo += 1
                print("AUTO CLICKS")
                print(f" {SrNo}: " + index)

            print("""
""")    

            for index in buyed_of_Click:
                SrNo += 1
                print("CLICKS")
                print(f" {SrNo}: " + index)


elif Enter == 'S':
    while True:
        print(f"""Welcome to the Shop!
            Score: {score}

            AUTO CLICKS:
                1. Auto Money x1: Cost- {Costs_of_Auto['Auto Money x1']}
                2. Auto Money x5: Cost- {Costs_of_Auto['Auto Money x5']}
                3. Auto Money x10: Cost- {Costs_of_Auto['Auto Money x10']}
                4. Auto Money x20: Cost- {Costs_of_Auto['Auto Money x20']}
                5. Auto Money x50: Cost- {Costs_of_Auto['Auto Money x50']}
                6. Auto Money x70: Cost- {Costs_of_Auto['Auto Money x70']}
                7. Auto Money x90: Cost- {Costs_of_Auto['Auto Money x90']}
                8. Auto Money x100: Cost- {Costs_of_Auto['Auto Money x100']}
                
            CLICKS:
                1. Click Amount +1: Cost- {Costs_of_Click['Click Amount +1']}
                2. Click Amount +5: Cost- {Costs_of_Click['Click Amount +5']}
                3. Click Amount +10: Cost- {Costs_of_Click['Click Amount +10']}
                4. Click Amount +15: Cost- {Costs_of_Click['Click Amount +15']}
                5. Click Amount +25: Cost- {Costs_of_Click['Click Amount +25']}
                6. Click Amount +40: Cost- {Costs_of_Click['Click Amount +40']}
                7. Click Amount +70: Cost- {Costs_of_Click['Click Amount +70']}
                8. Click Amount +90: Cost- {Costs_of_Click['Click Amount +90']}
                9. Click Amount +100: Cost- {Costs_of_Click['Click Amount +100']}
                """)
        
        EnterShop = input("N(Exit)> ")

        if not min(Costs_of_Auto.values()) >= score:
            if EnterShop == Costs_of_Auto.keys():
                print("You dont have the amount of points")
        
        elif EnterShop == 'N':
            menu()

        elif min(Costs_of_Auto.values()) >= score or min(Costs_of_Click.values()) >= score:
            if EnterShop == Costs_of_Auto.keys() or EnterShop == Costs_of_Click.keys():
                print("Buyed!")
                continuing = input("Continue?(Y/N)> ")
                if continuing == 'Y':
                    continue
                elif continuing == 'N':
                    menu()

        elif not min(Costs_of_Click.values()) >= score:
            if EnterShop == Costs_of_Click.keys():
                print("You dont have the amount of points")


        elif min(Costs_of_Auto['Auto Money x1']) >= score:
            if EnterShop == 'Auto Money x1':
                AutoAmount += 1
                buyed_of_Auto.append('Auto Money x1')

        elif min(Costs_of_Auto['Auto Money x5']) >= score:
            if EnterShop == 'Auto Money x5':
                AutoAmount += 5
                buyed_of_Auto.append('Auto Money x5')

        elif min(Costs_of_Auto['Auto Money x10']) >= score:
            if EnterShop == 'Auto Money x10':
                AutoAmount += 10
                buyed_of_Auto.append('Auto Money x10')

        elif min(Costs_of_Auto['Auto Money x20']) >= score:
            if EnterShop == 'Auto Money x20':
                AutoAmount += 20
                buyed_of_Auto.append('Auto Money x20')

        elif min(Costs_of_Auto['Auto Money x50']) >= score:
            if EnterShop == 'Auto Money x50':
                AutoAmount += 50
                buyed_of_Auto.append('Auto Money x50')

        elif min(Costs_of_Auto['Auto Money x70']) >= score:
            if EnterShop == 'Auto Money x70':
                AutoAmount += 70
                buyed_of_Auto.append('Auto Money x70')

        elif min(Costs_of_Auto['Auto Money x90']) >= score:
            if EnterShop == 'Auto Money x90':
                AutoAmount += 90
                buyed_of_Auto.append('Auto Money x90')

        elif min(Costs_of_Auto['Auto Money x100']) >= score:
            if EnterShop == 'Auto Money x100':
                AutoAmount += 100
                buyed_of_Auto.append('Auto Money x100')



        elif min(Costs_of_Click['Click Amount +1']) >= score:
            if EnterShop == 'Click Amount +1':
                ClickAmount += 1
                buyed_of_Click.append('Click Amount +1')

        elif min(Costs_of_Click['Click Amount +5']) >= score:
            if EnterShop == 'Click Amount +5':
                ClickAmount += 5
                buyed_of_Click.append('Click Amount +5')

        elif min(Costs_of_Click['Click Amount +10']) >= score:
            if EnterShop == 'Click Amount +10':
                ClickAmount += 10
                buyed_of_Click.append('Click Amount +10')

        elif min(Costs_of_Click['Click Amount +15']) >= score:
            if EnterShop == 'Click Amount +15':
                ClickAmount += 15
                buyed_of_Click.append('Click Amount +15')

        elif min(Costs_of_Click['Click Amount +25']) >= score:
            if EnterShop == 'Click Amount +25':
                ClickAmount += 25
                buyed_of_Click.append('Click Amount +25')

        elif min(Costs_of_Click['Click Amount +40']) >= score:
            if EnterShop == 'Click Amount +40':
                ClickAmount += 40
                buyed_of_Click.append('Click Amount +40')

        elif min(Costs_of_Click['Click Amount +70']) >= score:
            if EnterShop == 'Click Amount +70':
                ClickAmount += 70
                buyed_of_Click.append('Click Amount +70')

        elif min(Costs_of_Click['Click Amount +90']) >= score:
            if EnterShop == 'Click Amount +90':
                ClickAmount += 90
                buyed_of_Click.append('Click Amount +90')

        elif min(Costs_of_Click['Click Amount +100']) >= score:
            if EnterShop == 'Click Amount +100':
                ClickAmount += 100
                buyed_of_Click.append('Click Amount +100')