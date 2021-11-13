##...RISHUL GHOSH...##
##...N230...##


def ActFunc(Yin):
    F = []
    for i in range(len(Yin)):
        list=(Yin[i])
    theta = int(input("Enter the threshold value: "))
    for k in list:
        if(k>theta):
            F.append(1)
        elif(k<=theta):
            F.append(-1)
    print("Y = F(Yin) = ",F)

def DiagZero(W):
    W[0][0]=0
    W[1][1]=0
    W[2][2]=0
    W[3][3]=0    
    
print("...AUTO-ASSOCIATIVE NETWORK...")
print("___________________________________________")
import numpy as np
InputMatrix1 = np.array([[1],[1],[1],[1]])
InputMatrix2 = np.array([[-1],[1],[1],[-1]])
TestingMatrix1 = np.array([[1],[1],[1],[1]])
TestingMatrix2 = np.array([[-1],[1],[1],[-1]])
TestingMatrix3 = np.array([[1],[1],[1],[0]])
Transpose1 = np.transpose(InputMatrix1)
Transpose2 = np.transpose(InputMatrix2)
TestingTranspose1 = np.transpose(TestingMatrix1)
TestingTranspose2 = np.transpose(TestingMatrix2)
TestingTranspose3 = np.transpose(TestingMatrix3)

#Input-1
print("GIVEN INPUT MATRIX-1: (Xi) - ",Transpose1)
print("TRANSPOSED INPUT MATRIX-1: (XiT) - ")
print(InputMatrix1)
print("___________________________________________")
print("CALCULATING Wij: (Wij = XiT * Xi)")
Wij1 = np.dot(InputMatrix1,Transpose1)
print(Wij1)
print("___________________________________________")
print("CALCULATING Yin: (Yin = Xi * Wij)")

#Input-2
print("___________________________________________")
print("___________________________________________")
print("GIVEN INPUT MATRIX-2: (Xi) - ",Transpose2)
print("TRANSPOSED INPUT MATRIX-2: (XiT) - ")
print(InputMatrix2)
print("___________________________________________")
print("CALCULATING Wij: (Wij = XiT * Xi)")
Wij2 = np.dot(InputMatrix2,Transpose2)
print(Wij2)
print("___________________________________________")
print("CALCULATING Yin: (Yin = Xi * Wij)")

#Final Weight Matrix
print("___________________________________________")
print("___________________________________________")
W=Wij1 + Wij2
print("WEIGHT MATRIX GENERATED AFTER STORAGE (W): ")
print(W)


#Testing Matrix: [1 1 1 1]
print("___________________________________________")
print("___________________________________________")
print("TESTING MATRIX: [1 1 1 1]")
Yin1 = np.dot(TestingTranspose1,W)
print("Yin = ",Yin1)
print("APPLYING ACTIVATION FUNCTION, WE GET: ")
ActFunc(Yin1)

#Testing Matrix: [-1 1 1 -1]
print("___________________________________________")
print("___________________________________________")
print("TESTING MATRIX: [-1 1 1 -1]")
Yin2 = np.dot(TestingTranspose2,W)
print("Yin = ",Yin2)
print("APPLYING ACTIVATION FUNCTION, WE GET: ")
ActFunc(Yin2)

#Testing Matrix: [1 1 1 0]
print("___________________________________________")
print("___________________________________________")
print("TESTING MATRIX: [1 1 1 0]")
Yin3 = np.dot(TestingTranspose3,W)
print("Yin = ",Yin3)
print("APPLYING ACTIVATION FUNCTION, WE GET: ")
ActFunc(Yin3)

#Repeating with Diagonal Elements of Weight Matrix as Zero
DiagZero(W)
print("___________________________________________")
print("___________________________________________")
print("___________________________________________")
print("NEW WEIGHT MATRIX AFTER DIAGONAL ELEMENTS GET ZERO")
print(W)
#Testing Matrix: [1 1 1 1]
print("___________________________________________")
print("...REPEATING TESTING WITH NEW WEIGHT MATRIX...")
print("___________________________________________")
print("TESTING MATRIX: [1 1 1 1]")
Yin4 = np.dot(TestingTranspose1,W)
print("Yin = ",Yin4)
print("APPLYING ACTIVATION FUNCTION, WE GET: ")
ActFunc(Yin4)

#Testing Matrix: [-1 1 1 -1]
print("___________________________________________")
print("___________________________________________")
print("TESTING MATRIX: [-1 1 1 -1]")
Yin5 = np.dot(TestingTranspose2,W)
print("Yin = ",Yin5)
print("APPLYING ACTIVATION FUNCTION, WE GET: ")
ActFunc(Yin5)

#Testing Matrix: [1 1 1 0]
print("___________________________________________")
print("___________________________________________")
print("TESTING MATRIX: [1 1 1 0]")
Yin6 = np.dot(TestingTranspose3,W)
print("Yin = ",Yin6)
print("APPLYING ACTIVATION FUNCTION, WE GET: ")
ActFunc(Yin6)





