# The ability to take user input
# The ability for the user to earn money
# The ability to buy tools and use the new tool
# The ability to win the game and end it
# Hint: Try setting the win amount to $10 first, then $50, and etc. 
# until you get to the end to allow for easier testing!

## list of tools

tools = [
    {"name": "Teeth", "income": 1, "price": 0},
    {"name": "Rusty Scissors", "income": 5, "price": 5},
    {"name": "Push Lawnmower", "income": 50, "price": 25},
    {"name": "Battery Powered Lawnmower", "income": 100, "price": 250},
    {"name": "Starving Students", "income": 250, "price": 500}
]

mowing_tool=0
money=0

def getInput():
    result = input("do you want to [c]ut the lawn, [u]pgrade your tool or [q]uit? ")
    
    if(result == "c"):
        cutLawn()
    elif(result == "u"):
        upgradeTool()
    elif(result == "q"):
        quitGame()

def cutLawn():
    print("You Cut the Lawn!")
def upgradeTool():  
    print("You Upgraded Your Tool")                  
def quitGame():
    print("You Quit The Game!")
    
    
    

getInput()