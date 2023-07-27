import time
import sys
import select
import keyboard
import os
import random 
class fruit:
    def __init__(self, status, xCoordinate, yCoordinate):
        self.consumed = status
        self.xCoordinate = xCoordinate
        self.yCoordinate = yCoordinate
        

    def changeCoordinates(self,coordinatesList):
        self.xCoordinate = coordinatesList[0]
        self.yCoordinate = coordinatesList[1]

class player:
    def __init__(self, score, xCoordinate, yCoordinate):
        self.score = 1
        self.xCoordinate = xCoordinate
        self.yCoordinate = yCoordinate
        self.xPrev = [xCoordinate];
        self.yPrev = [yCoordinate];
        self.lastKey = 'Down'
        self.snakeBiteFlag = False;

    def incrementScore(self):
        self.score+=1

    def incrementCoordinate(self,keyPressed = "None"): 
        self.incrementHelper(keyPressed)
        self.xPrev = [self.xCoordinate] + self.xPrev
        self.yPrev = [self.yCoordinate] + self.yPrev
        

    def incrementHelper(self, keyPressed):
        if (keyPressed == "None"):
            if(self.lastKey == 'Right'):
                self.xCoordinate +=1
            elif(self.lastKey == 'Left'):
                self.xCoordinate -=1
            elif(self.lastKey == 'Up'):
                self.yCoordinate -=1
            elif(self.lastKey == 'Down'):
                self.yCoordinate +=1
        else:
            if(keyPressed == "Right"):
                if (self.lastKey == "Right"):
                    self.xCoordinate +=1
                    self.lastKey = keyPressed
                elif (self.lastKey == "Left"):
                    self.xCoordinate -=1
                elif(self.lastKey == "Up"):
                    self.xCoordinate +=1
                    self.lastKey = keyPressed
                elif(self.lastKey) == "Down":
                    self.xCoordinate +=1
                    self.lastKey = keyPressed

            elif(keyPressed == "Left"):
                if (self.lastKey == "Right"):
                    self.xCoordinate +=1
                elif (self.lastKey == "Left"):
                    self.xCoordinate -=1
                    self.lastKey = keyPressed
                elif(self.lastKey == "Up"):
                    self.xCoordinate -=1
                    self.lastKey = keyPressed
                elif(self.lastKey) == "Down":
                    self.xCoordinate -=1
                    self.lastKey = keyPressed

            elif(keyPressed == "Up"):
                if (self.lastKey == "Right"):
                    self.yCoordinate -=1
                    self.lastKey = keyPressed
                elif (self.lastKey == "Left"):
                    self.yCoordinate -=1
                    self.lastKey = keyPressed
                elif(self.lastKey == "Up"):
                    self.yCoordinate -=1
                    self.lastKey = keyPressed
                elif(self.lastKey) == "Down":
                    self.yCoordinate +=1

            elif(keyPressed == "Down"):
                if (self.lastKey == "Right"):
                    self.yCoordinate +=1
                    self.lastKey = keyPressed
                elif (self.lastKey == "Left"):
                    self.yCoordinate +=1
                    self.lastKey = keyPressed
                elif(self.lastKey == "Up"):
                    self.yCoordinate -=1
                    self.lastKey = keyPressed
                elif(self.lastKey) == "Down":
                    self.yCoordinate +=1
                    self.lastKey = keyPressed
        return

    def gameOver(self, gridInstance):
        if((self.xCoordinate == gridInstance.width) or (self.yCoordinate == gridInstance.length) or (self.xCoordinate == -1) or (self.yCoordinate == -1)):
            print("Game Over!")
            quit()
        elif(self.snakeBiteFlag):
            print("\nSnake Bite! Game Over!")
            quit()
        

    def getUserInput(self, start_time,timeout=2):
            
            while True:
                if time.time() - start_time >= timeout:
                    return "None"
                if keyboard.is_pressed("up"):
                        return "Up"
                elif keyboard.is_pressed("down"):
                        return "Down"
                elif keyboard.is_pressed("left"):
                        return "Left"
                elif keyboard.is_pressed("right"):
                        return "Right"

#up -> -
#down -> +
#right -> +
#left -> -

class grid:
    def __init__(self, length, width):
        self.length = length
        self.width = width
        self.array = [[0 for _ in range(width)] for _ in range(length)]
        self.check = False
    def fruitCoordinates(self):
        xCoordinate =random.randint(0, self.width-1)
        yCoordinate =random.randint(0, self.length-1)
        return [xCoordinate,yCoordinate]


def main():
    gridInstance = grid (10,10)
    playerInstance = player(1,5,5)
    fruitInstance = fruit(False, 2,2)

    while (True):
        print()
        #length -> playerInstance.yCoordinate
        for i in range(gridInstance.length):
            #width -> playerInstance.xCoordinate
            for j in range(gridInstance.width):
                for k in range(0,playerInstance.score):
                    if(((playerInstance.xPrev[k] == j) and (playerInstance.yPrev[k] == i))):    
                        if(((fruitInstance.xCoordinate == j) and (fruitInstance.yCoordinate == i))):
                            playerInstance.incrementScore()
                            print("O ", end = "")
                            fruitCoordinates=gridInstance.fruitCoordinates()
                            fruitInstance.changeCoordinates(fruitCoordinates)
                            gridInstance.check=True
                        else:
                            print("O ", end = "")
                            gridInstance.check=True
                        for l in range(1,playerInstance.score):
                            if(((playerInstance.xPrev[l] == playerInstance.xPrev[0]) and (playerInstance.yPrev[l] == playerInstance.yPrev[0]))):
                                playerInstance.snakeBiteFlag = True
                                gridInstance.check=True
                                break
                        if(playerInstance.snakeBiteFlag):
                            break

                if((fruitInstance.xCoordinate == j) and (fruitInstance.yCoordinate == i)):
                    print("$ ", end ="")
                    gridInstance.check=True
                elif (gridInstance.check==False):
                    print(". ", end="")
                gridInstance.check=False
            print("") 
    
        playerInstance.gameOver(gridInstance)    
        timeout = .25
        start_time = time.time()
        userInput = playerInstance.getUserInput(start_time,timeout)
        while(time.time() - start_time < timeout):
            pass
        #print(playerInstance.xCoordinate,playerInstance.yCoordinate)
        #print(fruitInstance.xCoordinate,fruitInstance.yCoordinate)
        playerInstance.incrementCoordinate(userInput)
        os.system("cls" if os.name == "nt" else "clear")
        
        
        
main()

