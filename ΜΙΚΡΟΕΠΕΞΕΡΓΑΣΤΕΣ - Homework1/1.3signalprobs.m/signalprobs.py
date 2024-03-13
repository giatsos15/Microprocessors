# Georgios Giatsos, A.M. 3202

input1sp = float(input("Select input1sp value from 0.0 to 1.0: "))
input2sp = float(input("Select input2sp value from 0.0 to 1.0: "))
input3sp = float(input("Select input3sp value from 0.0 to 1.0: "))

inputs = []
n = int(input("Enter how many more inputs you want: "))
for i in range(0, n): 
    element = float(input("Select range of probability from 0.0 to 1.0: ")) 
  
    inputs.append(element) # adding the inputs 
  
print(inputs) 

#a erwthma

def sp2AND(input1sp, input2sp):
    sp2AND = input1sp*input2sp
    return sp2AND



def sp2OR(input1sp, input2sp):
    sp2OR = 1-(1-input1sp)*(1-input2sp)
    return sp2OR



def sp2NAND(input1sp, input2sp):
    sp2NAND = 1-(sp2AND(input1sp, input2sp))
    return sp2NAND



def sp2XOR(input1sp, input2sp):
    sp2XOR = sp2NAND(input1sp, input2sp)*sp2OR(input1sp, input2sp)
    return sp2XOR


def sp2NOR(input1sp, input2sp):
    sp2NOR = 1-(sp2OR(input1sp, input2sp))
    return sp2NOR



#b erwthma

def sp3AND(input1sp, input2sp, input3sp):
    sp3AND = sp2AND(input1sp, input2sp)*input3sp
    return sp3AND



def sp3OR(input1sp, input2sp, input3sp):
    sp3OR = sp2OR(sp2OR(input1sp, input2sp), input3sp)
    return sp3OR



def sp3NAND(input1sp, input2sp, input3sp):
    sp3NAND = sp2NAND(sp2NAND(input1sp, input2sp), input3sp)
    return sp3NAND



def sp3XOR(input1sp, input2sp, input3sp):
    sp3XOR = sp2XOR(sp2XOR(input1sp, input2sp), input3sp)
    return sp3XOR



def sp3NOR(input1sp, input2sp, input3sp):
    sp3NOR = sp2NOR(sp2NOR(input1sp, input2sp), input3sp)
    return sp3NOR



#c erwthma

def spnAND():
    spnAND = sp3AND(input1sp, input2sp, input3sp)
    for i in range(n):
        spnAND = spnAND * element
    return spnAND


def spnOR():
    spnOR = sp3OR(input1sp, input2sp, input3sp)
    for i in range(n):
        spnOR = 1-(1-spnOR)*(1-element)
    return spnOR


def spnNAND():
    spnNAND = sp3NAND(input1sp, input2sp, input3sp)
    for i in range(n):
        spnNAND = sp2NAND(spnNAND, element)
    return spnNAND


def spnXOR():
    spnXOR = sp3XOR(input1sp, input2sp, input3sp)
    for i in range(n):
        spnXOR = sp2XOR(spnXOR, element)
    return spnXOR


def spnNOR():
    spnNOR = sp3NOR(input1sp, input2sp, input3sp)
    for i in range(n):
        spnNOR = sp2NOR(spnNOR, element)
    return spnNOR


#d erwthma

def SW(check):
    Esw = 2*check*(1-check)
    return Esw


print("Signal probability of 2AND is:  " ,sp2AND(input1sp, input2sp), "   and Switching activity is: " , SW(sp2AND(input1sp, input2sp)))
print("Signal probability of 2OR is:   " ,sp2OR(input1sp, input2sp), "    and Switching activity is: " , SW(sp2OR(input1sp, input2sp)))
print("Signal probability of 2NAND is: " ,sp2NAND(input1sp, input2sp), "  and Switching activity is: " , SW(sp2NAND(input1sp, input2sp)))
print("Signal probability of 2XOR is:  " ,sp2XOR(input1sp, input2sp), "   and Switching activity is: " , SW(sp2XOR(input1sp, input2sp)))
print("Signal probability of 2NOR is:  " ,sp2NOR(input1sp, input2sp), "   and Switching activity is: " , SW(sp2NOR(input1sp, input2sp)))
print("Signal probability of 3AND is:  " ,sp3AND(input1sp, input2sp, input3sp), "  and Switching activity is: " , SW(sp3AND(input1sp, input2sp, input3sp)))
print("Signal probability of 3OR is:   " ,sp3OR(input1sp, input2sp, input3sp), "   and Switching activity is: " , SW(sp3OR(input1sp, input2sp, input3sp)))
print("Signal probability of 3NAND is: " ,sp3NAND(input1sp, input2sp, input3sp), " and Switching activity is: " , SW(sp3NAND(input1sp, input2sp, input3sp)))
print("Signal probability of 3XOR is:  " ,sp3XOR(input1sp, input2sp, input3sp), "  and Switching activity is: " , SW(sp3XOR(input1sp, input2sp, input3sp)))
print("Signal probability of 3NOR is:  " ,sp3NOR(input1sp, input2sp, input3sp), "  and Switching activity is: " , SW(sp3NOR(input1sp, input2sp, input3sp)))
if (n!=0):
    print("Signal probability of nAND is:  " ,spnAND(), "   and Switching activity is: " , SW(spnAND()))
    print("Signal probability of nOR is:   " ,spnOR(), "    and Switching activity is: " , SW(spnOR()))
    print("Signal probability of nNAND is: " ,spnNAND(), "  and Switching activity is: " , SW(spnNAND()))
    print("Signal probability of nXOR is:  " ,spnXOR(), "   and Switching activity is: " , SW(spnXOR()))
    print("Signal probability of nNOR is:  " ,spnNOR(), "   and Switching activity is: " , SW(spnNOR()))
else:
    pass





