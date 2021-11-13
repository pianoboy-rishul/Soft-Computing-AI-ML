##...Rishul Ghosh...##
##...N230...##
##...Logic Gates using McCulloch Pit Model...##

print("______________________________________________________")
                                ##...1. OR GATE...##
print("                    ...OR GATE...")
def OR(x1,x2,w1,w2):
    Yin=(x1*w1)+(x2*w2)
    if(Yin>=w1):
        return True
    else:
        return False
w1=int(input("Enter Weight-1 = "))
w2=int(input("Enter Weight-2 = "))
if(w1!=w2):
    print("...UNEQUAL WEIGHTS...")
else:
    print("A | B | OUTPUT")
    print("0 | 0 |", OR(0,0,w1,w2))
    print("0 | 1 |", OR(0,1,w1,w2))
    print("1 | 0 |", OR(1,0,w1,w2))
    print("1 | 1 |", OR(1,1,w1,w2))
    print("______________________________________________________")

                                ##...2. AND GATE...##
print("                    ...AND GATE...")
def AND(x1,x2,w1,w2):
    Yin=(x1*w1)+(x2*w2)
    if(Yin>=w1+w2):
        return True
    else:
        return False
w1=int(input("Enter Weight-1 = "))
w2=int(input("Enter Weight-2 = "))
if(w1!=w2):
    print("...UNEQUAL WEIGHTS...")
else:
    print("A | B | OUTPUT")
    print("0 | 0 |", AND(0,0,w1,w2))
    print("0 | 1 |", AND(0,1,w1,w2))
    print("1 | 0 |", AND(1,0,w1,w2))
    print("1 | 1 |", AND(1,1,w1,w2))
    print("______________________________________________________")
    
                                ##...3. NOR GATE...##
print("                    ...NOR GATE...")
def OR(x1,x2,w1,w2):
    Yin=(x1*w1)+(x2*w2)
    if(Yin>=w1):
        return False
    else:
        return True
w1=int(input("Enter Weight-1 = "))
w2=int(input("Enter Weight-2 = "))
if(w1!=w2):
    print("...UNEQUAL WEIGHTS...")
else:
    print("A | B | OUTPUT")
    print("0 | 0 |", OR(0,0,w1,w2))
    print("0 | 1 |", OR(0,1,w1,w2))
    print("1 | 0 |", OR(1,0,w1,w2))
    print("1 | 1 |", OR(1,1,w1,w2))
    print("______________________________________________________")
                                ##...4. NAND GATE...##
print("                    ...NAND GATE...")
def NAND(x1,x2,w1,w2):
    Yin=(x1*w1)+(x2*w2)
    if(Yin>=w1+w2):
        return False
    else:
        return True
w1=int(input("Enter Weight-1 = "))
w2=int(input("Enter Weight-2 = "))
if(w1!=w2):
    print("...UNEQUAL WEIGHTS...")
else:
    print("A | B | OUTPUT")
    print("0 | 0 |", NAND(0,0,w1,w2))
    print("0 | 1 |", NAND(0,1,w1,w2))
    print("1 | 0 |", NAND(1,0,w1,w2))
    print("1 | 1 |", NAND(1,1,w1,w2))
    print("______________________________________________________")
    
                                ##...4. NOT GATE...##
print("                    ...NOT GATE...")
def NOT(x1,w1):
    Yin=(x1*w1)
    if(Yin>=w1):
        return False
    else:
        return True
w1=int(input("Enter Weight-1 = "))
print("A | OUTPUT")
print("0 | ", NOT(0,w1))
print("1 | ", NOT(1,w1))
print("______________________________________________________")