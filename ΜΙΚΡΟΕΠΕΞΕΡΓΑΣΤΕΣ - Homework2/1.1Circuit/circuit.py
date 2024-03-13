# Georgios Giatsos, A.M. 3202
                
Array = [[0, 0, 0], [0, 0, 1],  [0, 1, 0], [0, 1, 1], [1, 0, 0], [1, 0, 1], [1, 1, 0], [1, 1, 1], [0.5, 0.5, 0.5]]


def sp2AND(a, b):
    e = a*b
    return e


def spNOT(c):
    f = 1-c
    return f


def circuit(e, f):
    d = e*f
    return d
    

for i in range(len(Array)):
    print("For the inputs " , Array[i][0], Array[i][1], Array[i][2], "we have:")
    print("Signal probability of e is: " ,sp2AND(Array[i][0], Array[i][1])) 
    print("Signal probability of f is: " ,spNOT(Array[i][2]))
    print("Signal probability of d is: " ,circuit(sp2AND(Array[i][0], Array[i][1]), spNOT(Array[i][2])))



    
