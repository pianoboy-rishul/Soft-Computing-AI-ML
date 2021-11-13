##...RISHUL GHOSH...##
##...N230...##

def EuclidDistanceV1(C1, C2, V1):
    D11 = pow((C1[0]-V1[0][0]),2) + pow((C1[1]-V1[0][1]),2) + pow((C1[2]-V1[0][2]),2) + pow((C1[3]-V1[0][3]),2)
    D12 = pow((C2[0]-V1[0][0]),2) + pow((C2[1]-V1[0][1]),2) + pow((C2[2]-V1[0][2]),2) + pow((C2[3]-V1[0][3]),2)
    print("______________________________________")
    print("### Vector-1 =",V1[0],"###")
    print("D1 = ",D11)
    print("D2 = ",D12)
    if(D11<D12):
        print("Winning Cluster = ",D11,". Hence initialising J = 1...")
        C1[0] = C1[0] + a*(V1[0][0]-C1[0])
        C1[1] = C1[1] + a*(V1[0][1]-C1[1])
        C1[2] = C1[2] + a*(V1[0][2]-C1[2])
        C1[3] = C1[3] + a*(V1[0][3]-C1[3])
        print("...New Weights...")
        print("W1 = ",C1[0])
        print("W2 = ",C1[1])
        print("W3 = ",C1[2])
        print("W4 = ",C1[3])
        print("______________________________________")
    else:
        print("Winning Cluster = ",D12,". Hence initialising J = 2...")
        C2[0] = C2[0] + a*(V1[0][0]-C2[0])
        C2[1] = C2[1] + a*(V1[0][1]-C2[1])
        C2[2] = C2[2] + a*(V1[0][2]-C2[2])
        C2[3] = C2[3] + a*(V1[0][3]-C2[3])
        print("...New Weights...")
        print("W1 = ",C2[0])
        print("W2 = ",C2[1])
        print("W3 = ",C2[2])
        print("W4 = ",C2[3])
        print("______________________________________")
        
def EuclidDistanceV2(C1, C2, V2):
    D21 = pow((C1[0]-V2[0][0]),2) + pow((C1[1]-V2[0][1]),2) + pow((C1[2]-V2[0][2]),2) + pow((C1[3]-V2[0][3]),2)
    D22 = pow((C2[0]-V2[0][0]),2) + pow((C2[1]-V2[0][1]),2) + pow((C2[2]-V2[0][2]),2) + pow((C2[3]-V2[0][3]),2)
    print("### Vector-2 =",V2[0],"###")
    print("D1 = ",D21)
    print("D2 = ",D22)
    if(D21<D22):
        print("Winning Cluster = ",D21,". Hence initialising J = 1...")
        C1[0] = C1[0] + a*(V2[0][0]-C1[0])
        C1[1] = C1[1] + a*(V2[0][1]-C1[1])
        C1[2] = C1[2] + a*(V2[0][2]-C1[2])
        C1[3] = C1[3] + a*(V2[0][3]-C1[3])
        print("...New Weights...")
        print("W1 = ",C1[0])
        print("W2 = ",C1[1])
        print("W3 = ",C1[2])
        print("W4 = ",C1[3])
        print("______________________________________")
    else:
        print("Winning Cluster = ",D22,". Hence initialising J = 2...")
        C2[0] = C2[0] + a*(V2[0][0]-C2[0])
        C2[1] = C2[1] + a*(V2[0][1]-C2[1])
        C2[2] = C2[2] + a*(V2[0][2]-C2[2])
        C2[3] = C2[3] + a*(V2[0][3]-C2[3])
        print("...New Weights...")
        print("W1 = ",C2[0])
        print("W2 = ",C2[1])
        print("W3 = ",C2[2])
        print("W4 = ",C2[3])
        print("______________________________________")
        
def EuclidDistanceV3(C1, C2, V3):
    D31 = pow((C1[0]-V3[0][0]),2) + pow((C1[1]-V3[0][1]),2) + pow((C1[2]-V3[0][2]),2) + pow((C1[3]-V3[0][3]),2)
    D32 = pow((C2[0]-V3[0][0]),2) + pow((C2[1]-V3[0][1]),2) + pow((C2[2]-V3[0][2]),2) + pow((C2[3]-V3[0][3]),2)
    print("### Vector-3 =",V3[0],"###")
    print("D1 = ",D31)
    print("D2 = ",D32)
    if(D31<D32):
        print("Winning Cluster = ",D31,". Hence initialising J = 1...")
        C1[0] = C1[0] + a*(V3[0][0]-C1[0])
        C1[1] = C1[1] + a*(V3[0][1]-C1[1])
        C1[2] = C1[2] + a*(V3[0][2]-C1[2])
        C1[3] = C1[3] + a*(V3[0][3]-C1[3])
        print("...New Weights...")
        print("W1 = ",C1[0])
        print("W2 = ",C1[1])
        print("W3 = ",C1[2])
        print("W4 = ",C1[3])
        print("______________________________________")
    else:
        print("Winning Cluster = ",D32,". Hence initialising J = 2...")
        C2[0] = C2[0] + a*(V3[0][0]-C2[0])
        C2[1] = C2[1] + a*(V3[0][1]-C2[1])
        C2[2] = C2[2] + a*(V3[0][2]-C2[2])
        C2[3] = C2[3] + a*(V3[0][3]-C2[3])
        print("...New Weights...")
        print("W1 = ",C2[0])
        print("W2 = ",C2[1])
        print("W3 = ",C2[2])
        print("W4 = ",C2[3])
        print("______________________________________")
        
def EuclidDistanceV4(C1, C2, V4):
    D41 = pow((C1[0]-V4[0][0]),2) + pow((C1[1]-V4[0][1]),2) + pow((C1[2]-V4[0][2]),2) + pow((C1[3]-V4[0][3]),2)
    D42 = pow((C2[0]-V4[0][0]),2) + pow((C2[1]-V4[0][1]),2) + pow((C2[2]-V4[0][2]),2) + pow((C2[3]-V4[0][3]),2)
    print("### Vector-4 =",V4[0],"###")
    print("D1 = ",D41)
    print("D2 = ",D42)
    if(D41<D42):
        print("Winning Cluster = ",D41,". Hence initialising J = 1...")
        C1[0] = C1[0] + a*(V4[0][0]-C1[0])
        C1[1] = C1[1] + a*(V4[0][1]-C1[1])
        C1[2] = C1[2] + a*(V4[0][2]-C1[2])
        C1[3] = C1[3] + a*(V4[0][3]-C1[3])
        print("...New Weights...")
        print("W1 = ",C1[0])
        print("W2 = ",C1[1])
        print("W3 = ",C1[2])
        print("W4 = ",C1[3])
        print("______________________________________")
    else:
        print("Winning Cluster = ",D42,". Hence initialising J = 2...")
        C2[0] = C2[0] + a*(V4[0][0]-C2[0])
        C2[1] = C2[1] + a*(V4[0][1]-C2[1])
        C2[2] = C2[2] + a*(V4[0][2]-C2[2])
        C2[3] = C2[3] + a*(V4[0][3]-C2[3])
        print("...New Weights...")
        print("W1 = ",C2[0])
        print("W2 = ",C2[1])
        print("W3 = ",C2[2])
        print("W4 = ",C2[3])
        print("______________________________________")

import numpy as np

V1 = np.array([[0, 0, 1, 1]])
V2 = np.array([[1, 0, 0, 0]])
V3 = np.array([[0, 1, 1, 0]])
V4 = np.array([[0, 0, 0, 1]])
print("Input Vector-1 : ", V1)
print("Input Vector-2 : ", V2)
print("Input Vector-3 : ", V3)
print("Input Vector-4 : ", V4)
print("______________________________________")
a = float(input("Enter the learning rate: "))
print("______________________________________")

WM = np.array([[0.2, 0.4, 0.6, 0.8],
               [0.9, 0.7, 0.5, 0.3]])
print("INITIALISING WEIGHT MATRIX BETWEEN 0-1:")
print("WM =")
print(np.transpose(WM))

C1 = WM[0]
C2 = WM[1]
print("_________________________________________________________________________________________")
print("CALCULATING EUCLIDIAN DISTANCES FOR EVERY INPUT VECTORS AND UPDATING THE CLUSTER WEIGHTS:")
EuclidDistanceV1(C1, C2, V1)
EuclidDistanceV2(C1, C2, V2)
EuclidDistanceV3(C1, C2, V3)
EuclidDistanceV4(C1, C2, V4)
