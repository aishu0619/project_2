from GameEngine import GameEngine

def main():
    gameEngine = GameEngine()
    gameEngine.initializeGame()
    gameEngine.intro()
    remaining_veggie = gameEngine.remainingVeggies()
    while remaining_veggie > 0:
        print(f" The remaining number of vegetables are: {remaining_veggie}")
        gameEngine.printField()
        print(f"Score: {gameEngine.getScore()}")
        gameEngine.moveRabbit()
        gameEngine.moveCaptain()
        remaining_veggie = gameEngine.remainingVeggies()
    gameEngine.gameOver()
    gameEngine.highScore()
    
main()

