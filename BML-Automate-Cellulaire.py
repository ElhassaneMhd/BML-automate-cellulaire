
import numpy as np
import random

def init():
    global carsNumber, sortedCarsNumber, totalIterations, blueCar, redCar, initMatrice, matrice, iterations, availablePositions
    carsNumber=10
    sortedCarsNumber=0
    totalIterations=0
    blueCar=1
    redCar=2
    initMatrice = np.zeros((N, N)) 
    matrice = np.zeros((N, N)) 
    iterations=[]
    availablePositions = set()

def randomPositions():
    count = carsNumber
    while count > 0:
        x = random.randint(0, N - 1)
        y = random.randint(0, N - 1)
        if (x, y) not in availablePositions:
            availablePositions.append((x, y))
            count -= 1  
                 
def addCars():
    blueCarsNumber, redCarsNumber = int(carsNumber/2), int(carsNumber/2)
    for j in availablePositions:
        if blueCarsNumber>0:
            blueCarsNumber-=1
            initMatrice[j[0]][j[1]] = int(blueCar)
        elif redCarsNumber>0 and initMatrice[j[0]][j[1]]==0:
            redCarsNumber-=1
            initMatrice[j[0]][j[1]] = int(redCar)

def moveCars():
    blockedCars = {
        'blue':[],
        'red':[]
    }
    sortedCars = {
        'blue':[],
        'red':[]
    }
    for i in range(N): 
        for j in range(N):
            if initMatrice[i][j]==2 :
                if j+1>=N :
                    matrice[i][j]=0
                    sortedCars['red'].append((i, j))
                elif initMatrice[i][j+1]==0 and matrice[i][j+1]==0:
                    matrice[i][j+1]=2
                    matrice[i][j]=-1 
                else :
                    blockedCars['red'].append((i, j))
                    matrice[i][j]=2

    for i in range(N):        
        for j in range(N):
            if initMatrice[i][j]==1:
                if i+1>=N:
                    matrice[i][j]=0 
                    sortedCars['blue'].append((i, j))
                elif initMatrice[i+1][j]==0 and matrice[i+1][j]==0:
                    matrice[i+1][j]=1
                    matrice[i][j]=0
                else:
                    matrice[i][j]=1
                    blockedCars['blue'].append((i, j))

    for i in range(N):        
        for j in range(N):
            if matrice[i][j]==-1:
                matrice[i][j]=0
    
    iterations.append({
        'blocke':blockedCars,
        'sorted':sortedCars,
    })
  
    
def showStats():
    for i in iterations:
        count = iterations.index(i)
        print('-------------------------------------------------')
        print(f"iteration {count+1} , blocked : {i.get('blocke')}")
        print(f"iteration {count+1} , sorted : {i.get('sorted')}")
        print('-------------------------------------------------')
            
showStats()

def main():
    init()
    randomPositions()
    addCars()
    moveCars()
    initMatrice = matrice
    print(matrice)
    matrice = np.zeros((N, N))
    showStats()


if __name__ == "__main__":
    main()
