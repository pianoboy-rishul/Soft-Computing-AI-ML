##...RISHUL GHOSH...##
##...N230...##

import numpy as np
def activation(yin,threshold):
    l=[]
    u=[]
    for i in range(len(yin)):
        l=yin[i]
    for i in l:
        if (i>threshold):
            u.append(1)
        else:
            u.append(-1)
    print(u)
        
S1 = np.array([[1],[1],[1],[-1]])
St = np.transpose(S1)
print("For input: ",St)
threshold = int(input("Enter threshold value: "))
w = np.dot(S1,St)
print(w)
yin=np.dot(St,w)
print(yin)
print(activation(yin,threshold))

print("For error in 0th index:")
S2 = np.array([[0],[1],[1],[-1]])
St2 =np.transpose(S2)
yin2=np.dot(St2,w)
activation(yin2,threshold)


print("For error in 1st index:")
S3 = np.array([[1],[0],[1],[-1]])
St3 =np.transpose(S3)
yin3=np.dot(St3,w)
activation(yin3,threshold)


print("For error in 2nd index:")
S4 = np.array([[1],[1],[0],[-1]])
St4 =np.transpose(S4)
yin4=np.dot(St4,w)
activation(yin4,threshold)


print("For error in 3rd index:")
S5 = np.array([[1],[1],[1],[0]])
St5 =np.transpose(S5)
yin5=np.dot(St5,w)
activation(yin5,threshold)



