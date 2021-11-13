##...RISHUL GHOSH...##
##...N230...##

import numpy as np

def FuzzUnion(l1,l2):
    union = []
    u1 = max(l1[0],l2[0])
    union.append(u1)
    u2 = max(l1[1],l2[1])
    union.append(u2)
    u3 = max(l1[2],l2[2])
    union.append(u3)
    u4 = max(l1[3],l2[3])
    union.append(u4)
    u5 = max(l1[4],l2[4])
    union.append(u5)
    print("Union Op = ",union)

def FuzzIntersect(l1,l2):
    intersect = []
    i1 = min(l1[0],l2[0])
    intersect.append(i1)
    i2 = min(l1[1],l2[1])
    intersect.append(i2)
    i3 = min(l1[2],l2[2])
    intersect.append(i3)
    i4 = min(l1[3],l2[3])
    intersect.append(i4)
    i5 = min(l1[4],l2[4])
    intersect.append(i5)
    print("Intersection Op = ",intersect)

def FuzzComp(l1,l2):
    complementA = []
    complementB = []
    ca1 = 1-l1[0]
    complementA.append(ca1)
    ca2 = 1-l1[1]
    complementA.append(ca2)
    ca3 = 1-l1[2]
    complementA.append(ca3)
    ca4 = 1-l1[3]
    complementA.append(ca4)
    ca5 = 1-l1[4]
    complementA.append(ca5)
    print("Complement of Fuzzy Set-1 = ",complementA)
    cb1 = 1-l2[0]
    complementB.append(cb1)
    cb2 = 1-l2[1]
    complementB.append(cb2)
    cb3 = 1-l2[2]
    complementB.append(cb3)
    cb4 = 1-l2[3]
    complementB.append(cb4)
    cb5 = 1-l2[4]
    complementB.append(cb5)
    print("Complement of Fuzzy Set-2 = ",complementB)

def AlgSum(l1,l2):
    asum = []
    p1 = (l1+l2)
    p2 = (l1*l2)
    sums = (p1-p2)
    asum.append(sums[0])
    asum.append(sums[1])
    asum.append(sums[2])
    asum.append(sums[3])
    asum.append(sums[4])
    print("Algebraic Sum = ",asum)

def AlgProduct(l1,l2):
    aproduct = []
    prod = (l1*l2)
    aproduct.append(prod[0])
    aproduct.append(prod[1])
    aproduct.append(prod[2])
    aproduct.append(prod[3])
    aproduct.append(prod[4])
    print("Algebraic Product = ",aproduct)
    
##...DRIVER CODE...##
l1 = np.array([1,3,5,7,9])
l2 = np.array([2,4,6,8,10])
print("Fuzzy Set-1 = ",l1)
print("Fuzzy Set-2 = ",l2)
print("_____________________________________________________")
print("_____________________________________________________")
FuzzUnion(l1,l2)
print("_____________________________________________________")
FuzzIntersect(l1,l2)
print("_____________________________________________________")
FuzzComp(l1,l2)
print("_____________________________________________________")
AlgSum(l1,l2)
print("_____________________________________________________")
AlgProduct(l1,l2)
print("_____________________________________________________")
print("_____________________________________________________")

    
