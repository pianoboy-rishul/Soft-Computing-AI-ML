##...Rishul Ghosh...##
##...N230...##

                          ##...PERCEPTRON RULE...##
print("________________________________________________________________________")
I = []  
print("                   CASE-1 : For Pattern I :-")
n = int(input("Enter the number of inputs :- "))
b = int(input("Enter the bias value :- "))
t = int(input("Enter the target value :- "))
al = int(input("Enter the alpha value :- "))
the = int(input("Enter the theta value :- "))
print("Enter inputs (Xi) in order :-")
for i in range(0,n):
    ele=int(input())
    I.append(ele)
w1=w2=w3=w4=w5=w6=w7=w8=w9=b=0
print("CALCULATION FOR PATTERN I:")
Yin = b+(I[0]*w1)+(I[1]*w2)+(I[2]*w3)+(I[3]*w4)+(I[4]*w5)+(I[5]*w6)+(I[6]*w7)+(I[7]*w8)+(I[8]*w9)
print("Yin = ",Yin)
if(Yin>0):
    F = 1
    print("F(Yin) = ",F)
elif(Yin==0):
    F = 0
    print("F(Yin) = ",F)
elif(Yin<0):
    F = -1
    print("F(Yin) = ",F)
if(t==F):
    print("...Initialised weights are correct...")
else:
    print("...Initialised weights are not correct...")
    print("CALCULATING NEW WEIGHTS:-")
    WI = []
    w1new = w1+(al*t*I[0])
    w2new = w2+(al*t*I[1])
    w3new = w3+(al*t*I[2])
    w4new = w4+(al*t*I[3])
    w5new = w5+(al*t*I[4])
    w6new = w6+(al*t*I[5])
    w7new = w7+(al*t*I[6])
    w8new = w8+(al*t*I[7])
    w9new = w9+(al*t*I[8])
    bnew = b+(al*t)
    WI.append(w1new)
    WI.append(w2new)
    WI.append(w3new)
    WI.append(w4new)
    WI.append(w5new)
    WI.append(w6new)
    WI.append(w7new)
    WI.append(w8new)
    WI.append(w9new)
    print("New Weights = ",WI)
    print("New Bias = ",bnew)
print("________________________________________________________________________")
F = []
print("                   CASE-2 : For Pattern F :-")
n = int(input("Enter the number of inputs :- "))
bias = int(input("Enter the bias value :- "))
T = int(input("Enter the target value :- "))
al = int(input("Enter the alpha value :- "))
the = int(input("Enter the theta value :- "))
print("Enter inputs (Xi) in order :-")
for i in range(0,n):
    ELE=int(input())
    F.append(ELE)
W1=w1new
W2=w2new
W3=w3new
W4=w4new
W5=w5new
W6=w6new
W7=w7new
W8=w8new
W9=w9new
B=bnew
print("CALCULATION FOR PATTERN I:")
Yinnew = B+(F[0]*W1)+(F[1]*W2)+(F[2]*W3)+(F[3]*W4)+(F[4]*W5)+(F[5]*W6)+(F[6]*W7)+(F[7]*W8)+(F[8]*W9)
print("Yin = ",Yinnew)
if(Yinnew>0):
    Fnew = 1
    print("F(Yin) = ",Fnew)
elif(Yinnew==0):
    Fnew = 0
    print("F(Yin) = ",Fnew)
elif(Yinnew<0):
    F = -1
    print("F(Yin) = ",Fnew)
if(T==Fnew):
    print("...Initialised weights are correct...")
else:
    print("...Initialised weights are not correct...")
    print("CALCULATING NEW WEIGHTS:-")
    WF = []
    W1new = W1+(al*T*F[0])
    W2new = W2+(al*T*F[1])
    W3new = W3+(al*T*F[2])
    W4new = W4+(al*T*F[3])
    W5new = W5+(al*T*F[4])
    W6new = W6+(al*T*F[5])
    W7new = W7+(al*T*F[6])
    W8new = W8+(al*T*F[7])
    W9new = W9+(al*T*F[8])
    Bnew = B+(al*T)
    WF.append(W1new)
    WF.append(W2new)
    WF.append(W3new)
    WF.append(W4new)
    WF.append(W5new)
    WF.append(W6new)
    WF.append(W7new)
    WF.append(W8new)
    WF.append(W9new)
    print("New Weights = ",WF)
    print("New Bias = ",Bnew)
print("________________________________________________________________________")