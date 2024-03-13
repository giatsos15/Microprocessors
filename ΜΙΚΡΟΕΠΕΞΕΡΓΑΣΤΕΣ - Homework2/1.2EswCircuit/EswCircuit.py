# Georgios Giatsos, A.M. 3202



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

def main(input1sp, input2sp, input3sp):
    print("For the inputs " , input1sp, input2sp, input3sp, "we have:")
    print("Switching Activity of e is: ", SW(sp2AND(input1sp,input2sp)))
    print("Switching Activity of f is: ", SW(spNOT(input3sp)))
    print("Switchign Activity of d is: ", SW(circuit(sp2AND(input1sp, input2sp),spNOT(input3sp))))

main(0.5, 0.5, 0.5)
