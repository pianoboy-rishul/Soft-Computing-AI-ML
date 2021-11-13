##...Rishul Ghosh...##
##...N230...##
##...Logic Gates Using Python...##

                                ##...1. OR GATE...##
def OR(a,b):
    if a==1:
        return True
    elif b==1:
        return True
    else:
        return False
print("                    ...OR GATE...")
print("A=FALSE, B=FALSE | A OR B = ",OR(0,0),"|")
print("A=FALSE, B=TRUE  | A OR B = ",OR(0,1)," |")
print("A=TRUE, B=FALSE  | A OR B = ",OR(1,0)," |")
print("A=TRUE, B=TRUE   | A OR B = ",OR(1,1)," |")

print("______________________________________________________")

                                ##...2. NOR GATE...##
def NOR(a,b):
    if a==1:
        return False
    elif b==1:
        return False
    else:
        return True
print("                   ...NOR GATE...")
print("A=FALSE, B=FALSE | A NOR B = ",NOR(0,0)," |")
print("A=FALSE, B=TRUE  | A NOR B = ",NOR(0,1),"|")
print("A=TRUE, B=FALSE  | A NOR B = ",NOR(1,0),"|")
print("A=TRUE, B=TRUE   | A NOR B = ",NOR(1,1),"|")

print("______________________________________________________")

                                ##...3. NAND GATE...##
def NAND(a,b):
    if a==1 and b==1:
        return False
    else:
        return True
    
print("                  ...NAND GATE...")
print("A=FALSE, B=FALSE | A NAND B = ",NAND(0,0)," |")
print("A=FALSE, B=TRUE  | A NAND B = ",NAND(0,1)," |")
print("A=TRUE, B=FALSE  | A NAND B = ",NAND(1,0)," |")
print("A=TRUE, B=TRUE   | A NAND B = ",NAND(1,1),"|")

print("______________________________________________________")

                                ##...3. AND GATE...##
def AND(a,b):
    if a==1 and b==1:
        return True
    else:
        return False
    
print("                   ...AND GATE...")
print("A=FALSE, B=FALSE | A AND B = ",AND(0,0)," |")
print("A=FALSE, B=TRUE  | A AND B = ",AND(0,1)," |")
print("A=TRUE, B=FALSE  | A AND B = ",AND(1,0)," |")
print("A=TRUE, B=TRUE   | A AND B = ",AND(1,1),"  |")

print("______________________________________________________")

                                ##...3. XOR GATE...##
def XOR(a,b):
    if a==0:
        if b==0:
            return False
        else:
            return True
    elif a==1:
        if b==0:
            return True
        else:
            return False

print("                   ...XOR GATE...")
print("A=FALSE, B=FALSE | A XOR B = ",XOR(0,0),"|")
print("A=FALSE, B=TRUE  | A XOR B = ",XOR(0,1)," |")
print("A=TRUE, B=FALSE  | A XOR B = ",XOR(1,0)," |")
print("A=TRUE, B=TRUE   | A XOR B = ",XOR(1,1),"|")

print("______________________________________________________")



                        ##...COMBINATIONAL LOGIC GATE...##
def ANDandOR(a,b):
    c=a*b*(a+b)
    if c!=0:
        return 1
    else:
        return 0

print("    ...COMBINATION OF (AND) AND (OR) GATES...")
print("A = 0, B = 0 | A ANDandOR B = ",ANDandOR(0,0),"|")
print("A = 0, B = 1 | A ANDandOR B = ",ANDandOR(0,1),"|")
print("A = 1, B = 1 | A ANDandOR B = ",ANDandOR(1,0),"|")
print("A = 1, B = 1 | A ANDandOR B = ",ANDandOR(1,1),"|")