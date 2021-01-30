import random as rnd


testing = False

def main():
    if testing:
        rnd.seed(10)        # the parameter inside the seed function can be a random interger, it is for reproducible behaviour during testing
    printIntro()
    proA, proB, n = getInputs()
    winsA, winsB = simNGames(n, proA, proB)
    printSummary(winsA, winsB)
    

def printIntro():
    
    # Print an introduction to the program
    
    print("This program simulates a game of racquetball vetween two")
    print('Players called "A" and "B". The ability of each player')     # use '' to distinguish ""
    print("is indicated by a probability (a number between 0 and 1)")
    print("thta the player wins the point when saving. Player A")
    print("always has the first serve.\n")
    

def getInputs():
    
    # returns proA, proB, number of games to simulate
    
    a = float(input("What is the prob.player A wins a serve? "))
    b = float(input("What is the prob.player B wins a serve? "))
    n = int(input("How many games to simulate?"))
    
    return a, b, n      # make sure they have the right order in other function


# "Simulate n games" sounds like a counted loop -> games -> one game
def simNGames(n, proA, proB):
    
    # Simulates n games of racquetball between players A, B
    # returns number of wins for A, number of wins for B
    
    winsA = 0
    winsB = 0
    
    for i in range(n):
        
        # The nect thing we need to do is simulate one game of racquetball.
        # we are not sure how to do that, so let's put it off until later
        
        scoreA, scoreB = simOneGame(proA, proB)
        
        if scoreA > scoreB:
            winsA += 1
        else:
            winsB += 1
            
    return winsA, winsB
            
        
def simOneGame(proA, proB):
    
    serving = "A"
    scoreA = 0
    scoreB = 0
    
    while not gameOver(scoreA, scoreB):
        
        if serving == "A":
            
            if rnd.random() < proA:
                scoreA += 1
            else:
                serving = "B"
        else:
            
            if rnd.random() < proB:
                scoreB += 1
            else:
                serving = "A"
                
    return scoreA, scoreB


def gameOver(a, b):
    
    return a == 15 or b == 15    # a vert clever way


def printSummary(winsA, winsB):

    # print a summary of wins of each other
    
    n = winsA + winsB
    
    print("\nGames simulated:", n)
    print("Wins for A: {0} ( {1: 0.1%} )". format(winsA, winsA / n))
    print("Wins for B: {0} ( {1: 0.1%} )". format(winsB, winsB / n))


# The reason why we keep dividing the function is make it easy to solve.
# Beside, when it come up with some error, you can try every small function to find out where is the error.
        