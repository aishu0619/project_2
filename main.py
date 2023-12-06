#Author: Aishwarya Shastry, Joel Simeon, 
#Date: 5 December 2023

from GameEngine import GameEngine

def main():
    gameEngine = GameEngine()
    gameEngine.initializeGame()
    gameEngine.intro()
    remaining_veggie = gameEngine.remainingVeggies()
    while remaining_veggie > 0:
        #iterating through the steps
        print(f" The remaining number of vegetables are: {remaining_veggie}")
        gameEngine.printField()
        print(f"Score: {gameEngine.getScore()}")
        gameEngine.moveRabbit()
        gameEngine.moveCaptain()
        remaining_veggie = gameEngine.remainingVeggies()
    gameEngine.gameOver()
    gameEngine.highScore()
    
main()

