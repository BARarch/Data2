import numpy as np
import pandas as pd
import random as rand

def initGame(M, N):
    game = []
    for m in range(M):
        if m == 0:
            l = list(range(N,0,-1))
        else:
            l = []
        game.append(l)
    return game

def topPlate(tower):
    try:
        return tower[-1]
    except IndexError:
        return "No Plate"

def isPossibleMove(depTower, arrTower):
    '''Returns true if plate on the top of depTower can be move to the top of arrTower
       Assumtions: DepTower and arrTower are adjacent.
                   DepTower has a plate on it.
    '''
    if topPlate(arrTower) == 'No Plate':
        return True
    return topPlate(depTower) < topPlate(arrTower)

def findPossibleMoves(stage):
    '''Returns a list of all possibles moves of a stage of the Towers game.  Each move is a tupple of indexies of the 
       stage list (i,j) where i is the index of the departing tower and j is the index of the arrivale tower
    
    '''
    moves = []
    for i in range(len(stage)):
        if not stage[i]:
            continue
        if i == 0:
            if isPossibleMove(stage[i],stage[i+1]):
                moves.append((stage[i],stage[i+1]))
        elif i == len(stage) - 1:
            if isPossibleMove(stage[i],stage[i-1]):
                moves.append((stage[i],stage[i-1]))
        else:
            if isPossibleMove(stage[i],stage[i+1]):
                moves.append((stage[i],stage[i+1]))
            if isPossibleMove(stage[i],stage[i-1]):
                moves.append((stage[i],stage[i-1]))
    
    return moves

def movePlate(move):
    move[1].append(move[0].pop())

def centerOfMass(game):
    moment = 0
    towerNo = 0
    mass = 0
    for tower in game:
        tot2 = 0
        for plate in tower:
            tot2 += plate
            mass += plate
        moment += tot2 * towerNo
        towerNo += 1
    return moment/mass

def playGame(game, rounds):
    for i in range(rounds):
        movePlate(rand.choice(findPossibleMoves(game)))
        #print(game)
    return centerOfMass(game)

def playNGames(N,size,rounds):
    cms = []
    for i in range(N):
        cms.append(playGame(initGame(size, size),rounds))
    return cms

if __name__ == '__main__':
    N = 10000
    
    print("3 X 3, T = 16")
    data = playNGames(N,3,16)
    print("mean: " + str(np.mean(data)))
    print("std: " + str(np.std(data)))
    
    print("---------------------------------------------")
    print("6 X 6, T = 256")
    data2 = playNGames(N,6,256)
    print("mean: " + str(np.mean(data2)))
    print("std: " + str(np.std(data2)))