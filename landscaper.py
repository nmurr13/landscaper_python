# The ability for the user to earn money
# The ability to buy tools and use the new tool
# The ability to win the game and end it
# Hint: Try setting the win amount to $10 first, then $50, and etc. 
# until you get to the end to allow for easier testing!


class Tool:
    def __init__(self, name, income, price):
        self.name = name
        self.income=income
        self.price=price
    def myfunc(self):
        print("You cut the lawn with " + self.name + " and made $ " self.income)   
    def update(self):
        print("You updated your tool to " + self.name + " and it cost " + self.price)
t1 = Tool("Teeth", 1, 0)
t2 = Tool("Rusty Scissors", 5, 5)
t3 = Tool("Push Lawnmower", 50, 25)
t4 = Tool("Battery Powered Lawnmower", 100,250)
t5 = Tool("Starving Students",250,500)

player = {
    "money": 0
}

x = player.get("money")

def win_conditions():
    if (x >= 10):
        return True
    else: return False

while(True):
    result = input("Do you want to [c]ut the lawn, [u]pgrade your tool or [q]uit? ")
    if(result == "c"):
        t1.myfunc()
    elif(result == "u" and x >= 5):
        t2.myfunc()

    elif(result == "q"):
        print("Game Over!")
        break
    else:
        print("Enter a Valid Option!")
    if(win_conditions()):
        break
    
