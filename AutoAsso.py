##...RISHUL GHOSH...##
##...N230...##


def ActFunc(Yin):
    F = []
    print("Elements of the (Yin) matrix are: ")
    for i in range(len(Yin)):
        list=(Yin[i])
    for j in list:
        print(j)
    theta = int(input("Enter the threshold value: "))
    for k in list:
        if(k>theta):
            F.append(1)
        elif(k<theta):
            F.append(-1)
    print("Y = F(Yin) = ",F)
    
print("...AUTO-ASSOCIATIVE NETWORK...")
print("___________________________________________")
import numpy as np
InputMatrix1 = np.array([[-1],[-1],[-1],[-1]])
InputMatrix2 = np.array([[-1],[-1],[1],[1]])
TestingMatrix = np.array([[1],[1],[1],[1]])
Transpose1 = np.transpose(InputMatrix1)
Transpose2 = np.transpose(InputMatrix2)
TestingTranspose = np.transpose(TestingMatrix)

#Input-1#
print("GIVEN INPUT MATRIX: (Xi) - ",Transpose1)
print("TRANSPOSED INPUT MATRIX: (XiT) - ")
print(InputMatrix1)
print("___________________________________________")
print("CALCULATING Wij: (Wij = XiT * Xi)")
Wij1 = np.dot(InputMatrix1,Transpose1)
print(Wij1)
print("___________________________________________")
print("CALCULATING Yin: (Yin = Xi * Wij)")
Yin1 = np.dot(Transpose1,Wij1)
print(Yin1)
print("___________________________________________")
print("CALCULATING Y: (Y = F(Yin))")
ActFunc(Yin1)
print("___________________________________________")
print("___________________________________________")

#Input-2#
print("GIVEN INPUT MATRIX: (Xi) - ",Transpose2)
print("TRANSPOSED INPUT MATRIX: (XiT) - ")
print(InputMatrix2)
print("___________________________________________")
print("CALCULATING Wij: (Wij = XiT * Xi)")
Wij2 = np.dot(InputMatrix2,Transpose2)
print(Wij2)
print("___________________________________________")
print("CALCULATING Yin: (Yin = Xi * Wij)")
Yin2 = np.dot(Transpose2,Wij2)
print(Yin2)
print("___________________________________________")
print("CALCULATING Y: (Y = F(Yin))")
ActFunc(Yin2)
print("___________________________________________")
print("___________________________________________")

#Testing Section#
print("GIVEN TESTING MATRIX: (Xi) - ",TestingTranspose)
print("TRANSPOSED TESTING MATRIX: (XiT) - ")
print(TestingMatrix)
print("___________________________________________")
print("CALCULATING Wij: (Wij = XiT * Xi)")
WijT = np.dot(TestingMatrix,TestingTranspose)
print(WijT)
print("___________________________________________")
print("CALCULATING Yin: (Yin = Xi * Wij)")
YinT = np.dot(TestingTranspose,WijT)
print(YinT)
print("___________________________________________")
print("CALCULATING Y: (Y = F(Yin))")
ActFunc(YinT)
print("___________________________________________")
print("___________________________________________")





