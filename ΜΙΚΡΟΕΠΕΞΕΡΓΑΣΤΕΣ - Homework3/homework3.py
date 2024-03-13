import os
import glob
import array as np
import sys

ElementTypes = []
ElementsTable = []
SignalsTable = [0.5,0.5,0.5] #a,b,c,d,e,f
outputs = []

def sp2AND(a, b):
    e = a*b
    return e

def spNOT(c):
    f = 1-c
    return f

def circuit(e, f):
    d = e*f
    return d

def SW(check):
    Esw = 2*check*(1-check)
    return Esw


class element(object):
    def __init__(self, type, input, output):
        self.type = type
        self.input = input
        self.output = output

    def __repr__(self):
        return (str(self.type)) + (str(self.input)) + (str(self.output))


def proccess(E):
    if(E.type == "AND"):
        E.output = sp2AND(E.input[0], E.input[1])
        outputs.append(E.output)
    elif(E.type == "NOT"):
        E.output = spNOT(E.input[0])
        outputs.append(E.output)
    SignalsTable.append(E.output)


def getData():
    filename = input("Please enter the file: ")
    readfile = open(filename, "r")
    list_of_lists = [(line.strip()).split() for line in readfile]
    readfile.close()
    print(list_of_lists)
    z=[]
    i = 0
    x = list_of_lists[i][0]
    if (x=="top_inputs"):
        list_of_lists.pop(0)
        for i in range(len(list_of_lists)):
            ElementTypes.append(x)
            x = list_of_lists[i][0]
            y = list_of_lists[i][1]
            z = list_of_lists[i][len(list_of_lists)-1:]
            E = element(x,z,y)
            ElementsTable.append(E) 
            inputs = []
            for i in range(len(z)):
                if (len(outputs)>1):
                    for i in range(len(outputs)):
                        inputs.append(outputs[i])
                else:
                    inputs.append(float(SignalsTable[0]))
            E = element(x, inputs, y)
            proccess(E)
            
                
    else:
        for i in range(len(list_of_lists)):
            x = list_of_lists[i][0]
            y = list_of_lists[i][1]
            z = list_of_lists[i][len(list_of_lists)-1:]
            E = element(x,z,y)
            ElementTypes.append(x)
            ElementsTable.append(E) 
            inputs = []
            for i in range(len(z)):
                if (z[i] == "a"):
                    inputs.append(float(SignalsTable[0]))
                if (z[i] == "b"):
                    inputs.append(float(SignalsTable[1]))
                    E = element(x, inputs, y)
                    proccess(E)
                if (z[i] == "c"):
                    inputs.append(float(SignalsTable[2]))
                    E = element(x, inputs, y)
                    proccess(E)
                if (z[i] == "e"):
                    inputs.append(float(SignalsTable[3]))
                if (z[i] == "f"):
                    inputs.append(float(SignalsTable[4]))
                    E = element(x, inputs, y)
                    proccess(E)
    
getData()

print("Signal Probability of circuit is: ", SignalsTable[-1])
print("Switching Activity of circuit is: ", SW(SignalsTable[-1]))
