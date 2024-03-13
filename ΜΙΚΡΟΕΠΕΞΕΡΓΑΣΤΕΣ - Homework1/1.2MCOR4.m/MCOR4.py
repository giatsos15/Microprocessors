import random


def SwitchingActivity():
    MonteCarloSize = 3202
    Array = []
    for i in range (MonteCarloSize):
        Workload = [random.randrange(0,2), random.randrange(0,2), random.randrange(0,2),random.randrange(0,2), random.randrange(0,2), random.randrange(0,2)]
        Array.append(Workload)
    vectorsNumber=len(Array)
    gateOutput=0&0&0&0
    switchesNumber=0
    for i in range(vectorsNumber): 
        NewGateOutput = Array[i][0] |  Array[i][1] | Array[i][2] |  Array[i][3]
        if (gateOutput==NewGateOutput):
            continue
        else:
            gateOutput=NewGateOutput
    
        switchesNumber=switchesNumber+1

    Esw=switchesNumber/vectorsNumber
    print(vectorsNumber)
    print("Esw =  " , Esw)

SwitchingActivity()
