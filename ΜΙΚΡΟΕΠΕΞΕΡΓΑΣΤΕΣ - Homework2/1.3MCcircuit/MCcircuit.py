# Georgios Giatsos, A.M. 3202

import random

inputs = []
n = int(input("Enter how many more inputs you want: "))

def SwitchingActivity():
    MonteCarloSize = n
    Array = []
    for i in range (MonteCarloSize):
        Workload = [random.randrange(0,2), random.randrange(0,2), random.randrange(0,2)]
        Array.append(Workload)
    vectorsNumber=len(Array)
    gateOutput=0
    gateOutput1=0
    gateOutput2=0
    switchesNumber=0
    switchesNumber1=0
    switchesNumber2=0
    for i in range(vectorsNumber): 
        NewGateOutput = Array[i][0] &  Array[i][1]
        NewGateOutput1 = 1 - Array[i][2]
        NewGateOutput2 = NewGateOutput & NewGateOutput1
        if (gateOutput!=NewGateOutput):
            gateOutput=NewGateOutput
            switchesNumber=switchesNumber+1
        if (gateOutput1!=NewGateOutput1):
            gateOutput1=NewGateOutput1
            switchesNumber1=switchesNumber1+1
        if (gateOutput2!=NewGateOutput2):
            gateOutput2=NewGateOutput2
            switchesNumber2=switchesNumber2+1

    Esw=switchesNumber/vectorsNumber
    Esw1=switchesNumber1/vectorsNumber
    Esw2=switchesNumber2/vectorsNumber
    print(vectorsNumber)
    print("Esw =  " , Esw)
    print("Esw1 =  " , Esw1)
    print("Esw2 =  " , Esw2)

SwitchingActivity()
