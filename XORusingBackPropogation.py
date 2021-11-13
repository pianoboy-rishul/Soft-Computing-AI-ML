import numpy as np
wij = np.random.rand(2,2) # input to hidden layer weights
wjk = np.random.rand(2,1) # hidden layer to output weights
bij = np.random.rand(1,2)
bjk = np.random.rand(1,1)
alpha = 0.5
def sigmoid(x, w, b):
    z = np.dot(x, w) + b
    return 1/(1 + np.exp(-z))
def gradient_descent(x, y):
    global wij, wjk, bij, bjk
    for i in range(10000):
        Xi = np.array(x)
        Xj = sigmoid(Xi, wij, bij)
        yhat = sigmoid(Xj, wjk, bjk)
        dk = (y - yhat) * yhat * (1 - yhat)
        dj = np.dot(dk, wjk.T) * Xj * (1 - Xj)
        g_wjk = np.dot(Xj.T, dk) * alpha
        g_wij = np.dot(Xi.T, dj) * alpha
        wjk += g_wjk
        wij += g_wij
        bjk += np.sum(dk) * alpha
        bij += np.sum(dj) * alpha
    print('\nFinal predictions: ')
    for i in range(4):
        print(x[i],":", yhat[i])
    print("\nFinal Errors:")
    for i in range(4):
        print(x[i],":",*(abs(y-yhat)[i]*100),"%")
    print("\nFinal Weights: (Input to Hidden)")
    print(wij)
    print(bij)
    print("\nFinal Weights: (Hidden to Output)")
    print(wjk)
    print(bjk)
print("2 Neurons in Input Layer. 2 in Hidden and 1 in Output Layer.")
print('\nStarting Input to Hidden weights: ')
print(wij)
print(bij)
print('\nStarting Hidden to Output weights: ')
print(wjk)
print(bjk)
inputs = np.array([[0,0],[0,1],[1,0],[1,1]])
outputs = np.array([[0],[1],[1],[0]])
gradient_descent(inputs, outputs)
