# COMMENTED OUT - PREVIOUS SOLUTION WITH FUNCTIONS BUT WITHOUT CLASSES

#def main_menu():  
#    global water_1
#    global money_1
#    global milk_1
#    global coffee_beans_1
#    global cups_1
#    global a  
#    a = input("""Write action (buy, fill, take, remaining, exit):
#    """)
#    if a == "buy":
#        buy()
#    elif a == "fill":
#        fill()
#    elif a == "take":
#        print("I gave you $" + str(money_1))
#        take()
#    elif a == "remaining":
#        remaining()
#    elif a == "exit":
#        exit()
    
        
        

#def buy():
#    global water_1
#    global money_1
#    global milk_1
#    global coffee_beans_1
#    global cups_1
#    num = input("""What do you want to buy? 1 - espresso, 2 - latte, 3 - cappuccino, back - to main menu:
#    """)
#    if num == "1":
#        if water_1 < 250:
#            print("Sorry, not enough water!")
#            main_menu()
#        elif coffee_beans_1 < 16:
#            print("Sorry, not enough coffee beans!")
#            main_menu()
#        elif cups_1 < 1:
#            print("Sorry, not enough cups!")
#            main_menu()
#        else:
#            print("I have enough resources, making you a coffee!")
#            water_1 -= 250
#            coffee_beans_1 -= 16
#            money_1 += 4
#            cups_1 -= 1
#            main_menu()
#            return (water_1, coffee_beans_1, money_1, cups_1)
#            main_menu()
#    elif num == "2":
#        if water_1 < 350:
#            print("Sorry, not enough water!")
#            main_menu()
#        elif coffee_beans_1 < 20:
#            print("Sorry, not enough coffee beans!")
#            main_menu()
#        elif milk_1 <75:
#            print("Sorry, not enough milk!")
#            main_menu()
#        elif cups_1 < 1:
#            print("Sorry, not enough cups!")
#            main_menu()
#        else:
#            print("I have enough resources, making you a coffee!")
#            water_1 -= 350
#            coffee_beans_1 -= 20
#            milk_1 -= 75
#            money_1 += 7
#            cups_1 -= 1
#            main_menu()
#            return (water_1, coffee_beans_1, milk_1, money_1, cups_1)
#            
#    elif num == "3":
#        if water_1 < 200:
#            print("Sorry, not enough water!")
#            main_menu()
#        elif milk_1 < 100:
#            print("Sorry, not enough milk!")
#            main_menu()
#        elif coffee_beans_1 < 12:
#            print("Sorry, not enough coffe beans!")
#            main_menu()
#        elif cups_1 < 1:
#            print("Sorry, not enough cups!")
#            main_menu()
#        else:
#            print("I have enough resources, making you a coffee!")
#            water_1 -= 200
#            coffee_beans_1 -= 12
#            milk_1 -= 100
#            money_1 += 6
#            cups_1 -= 1
#            main_menu()
#            return (water_1, coffee_beans_1, milk_1, money_1, cups_1)
#            main_menu()
#    elif num == "back":
#        main_menu()
#    main_menu()
        
#def fill():
#    global water_1
#    global money_1
#    global milk_1
#    global coffee_beans_1
#    global cups_1
#    global water
#    water = int(input("""Write how many ml of water do you want to add:
#    """))
#    global milk    
#    milk = int(input("""Write how many ml of milk do you want to add:
#    """))
#    global coffee_beans
#    coffee_beans = int(input("""Write how many grams of coffee beans do you want to add:
#    """))
#    global cups
#    cups = int(input("""Write how many disposable cups of coffee do you want to add:
#    """))
#    water_1 += water
#    milk_1 += milk
#    coffee_beans_1 += coffee_beans
#    cups_1 += cups
#    main_menu()
#    return (water_1, milk_1, coffee_beans_1, cups_1)
    
    
#def take():
#    global water_1
#    global money_1
#    global milk_1
#    global coffee_beans_1
#    global cups_1
#    money_1 = 0
#    main_menu()
#    return money_1
    
    
#def remaining():
#    global water_1
#    global money_1
#    global milk_1
#    global coffee_beans_1
#    global cups_1
#    print("The coffee machine has:")
#    print(water_1, "of water")
#    print(milk_1, "of milk")
#    print(coffee_beans_1, "of coffee beans")
#    print(cups_1, "of disposable cups")
#    print(money_1, "of money")
#    main_menu()
    

    

#global water_1
#global money_1
#global milk_1
#global coffee_beans_1
#global cups_1
#global a
#water_1 = 400
#money_1 = 550
#milk_1 = 540
#coffee_beans_1 = 120
#cups_1 = 9
#main_menu()



#######################################################


class CoffeeMachine:
    def __init__(self, water, milk, coffee, cups, money):
        self.water = 400
        self.milk = 540
        self.coffee = 120
        self.cups = 9
        self.money = 550

    def __str__(self):
        return f"""
        The coffee machine has:
        {self.water} of water
        {self.milk} of milk
        {self.coffee} of coffee beans
        {self.cups} of disposable cups
        ${self.money} of money"""

    def buy(self):
        self.coffee_var = input("What do you want to buy? 1 - espresso, 2 - latte, 3 - cappuccino, back - to main menu:")
        if self.coffee_var == "1":
            if self.water < 250:
                print("Sorry, not enough water!")
                return CoffeeMachine.main_func(self)
            if self.coffee < 16:
                print("Sorry, not enough coffee")
                return CoffeeMachine.main_func(self)
            if self.cups < 1:
                print("Sorry, not enough cups")
                return CoffeeMachine.main_func(self)
            else:
                print("I have enough resources, making you a coffee!")
                self.water -= 250
                self.coffee -= 16
                self.cups -= 1
                self.money += 4
                return CoffeeMachine.main_func(self)

        if self.coffee_var == "2":
            if self.water < 350:
                print("Sorry, not enough water!")
                return CoffeeMachine.main_func(self)
            if self.milk < 75:
                print("Sorry, not enough milk!")
                return CoffeeMachine.main_func(self)
            if self.coffee < 20:
                print("Sorry, not enough coffee")
                return CoffeeMachine.main_func(self)
            if self.cups < 1:
                print("Sorry, not enough cups")
                return CoffeeMachine.main_func(self)
            else:
                print("I have enough resources, making you a coffee!")
                self.water -= 350
                self.milk -= 75
                self.coffee -= 20
                self.cups -= 1
                self.money += 7
                return CoffeeMachine.main_func(self)

        if self.coffee_var == "3":
            if self.water < 200:
                print("Sorry, not enough water!")
                return CoffeeMachine.main_func(self)
            if self.milk < 100:
                print("Sorry, not enough milk!")
                return CoffeeMachine.main_func(self)
            if self.coffee < 12:
                print("Sorry, not enough coffee")
                return CoffeeMachine.main_func(self)
            if self.cups < 1:
                print("Sorry, not enough cups")
                return CoffeeMachine.main_func(self)
            else:
                print("I have enough resources, making you a coffee!")
                self.water -= 200
                self.milk -= 100
                self.coffee -= 12
                self.cups -= 1
                self.money += 6
                return CoffeeMachine.main_func(self)
        if self.coffee_var == "back":
            return CoffeeMachine.main_func(self)

    def fill(self):
        fill_water = int(input("Write how many ml of water do you want to add:"))
        self.water += fill_water
        fill_milk = int(input("Write how many ml of milk do you want to add:"))
        self.milk += fill_milk
        fill_coffee = int(input("Write how many grams of coffee beans do you want to add:"))
        self.coffee += fill_coffee
        fill_cups = int(input("Write how many disposable cups of coffee do you want to add:"))
        self.cups += fill_cups
        return CoffeeMachine.main_func(self)

    def take(self):
        print(f'I gave you ${self.money}')
        self.money = 0
        return CoffeeMachine.main_func(self)

    def remaining(self):
        print(f"""The coffee machine has:
        {self.water} of water
        {self.milk} of milk
        {self.coffee} of coffee beans
        {self.cups} of disposable cups
        {self.money} of money""")
        return CoffeeMachine.main_func(self)

    def main_func(self):
        while True:
            self.option = input("Write action (buy, fill, take, remaining, exit):")
            if self.option == "buy":
                return CoffeeMachine.buy(self)
            if self.option == "fill":
                return CoffeeMachine.fill(self)
            if self.option == "take":
                return CoffeeMachine.take(self)
            if self.option == "remaining":
                return CoffeeMachine.remaining(self)
            if self.option == "exit":
                break

x = CoffeeMachine(400, 540, 120, 9, 550)
x.main_func()


