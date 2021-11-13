##...Rishul Ghosh...##
##...N230...##


                             ##...GIVEN QUESTION...##

def Hebb(lst):
    w1old=w2old=b1old=0
    l1=[]
    list = lst[0]
    x1=list[0]
    x2=list[1]
    y1=list[3]
    delw1=x1*y1
    delw2=x2*y1
    delb1=y1
    w1new=w1old + delw1
    w2new=w2old + delw2
    b1new=b1old + delb1
    l1.append(w1new)
    l1.append(w2new)
    l1.append(b1new)
    print("FOR INPUT X1, HEBB NET GENERATED = [w1, w2, b] = ",l1)
    
    w3old=w1new
    w4old=w2new
    b2old=b1new
    l2=[]
    list = lst[1]
    x3=list[0]
    x4=list[1]
    y2=list[3]
    delw3=x3*y2
    delw4=x4*y2
    delb2=y2
    w3new=w3old + delw3
    w4new=w4old + delw4
    b2new=b2old + delb2
    l2.append(w3new)
    l2.append(w4new)
    l2.append(b2new)
    print("FOR INPUT X2, HEBB NET GENERATED = [w1, w2, b] = ",l2)
    
    w5old=w3new
    w6old=w4new
    b3old=b2new
    l3=[]
    list = lst[2]
    x5=list[0]
    x6=list[1]
    y3=list[3]
    delw5=x5*y3
    delw6=x6*y3
    delb3=y3
    w5new=w5old + delw5
    w6new=w6old + delw6
    b3new=b3old + delb3
    l3.append(w5new)
    l3.append(w6new)
    l3.append(b3new)
    print("FOR INPUT X3, HEBB NET GENERATED = [w1, w2, b] = ",l3)
    
    w7old=w5new
    w8old=w6new
    b4old=b3new
    l4=[]
    list = lst[3]
    x7=list[0]
    x8=list[1]
    y4=list[3]
    delw7=x7*y4
    delw8=x8*y4
    delb4=y4
    w7new=w7old + delw7
    w8new=w8old + delw8
    b4new=b4old + delb4
    l4.append(w7new)
    l4.append(w8new)
    l4.append(b4new)
    print("FOR INPUT X4, HEBB NET GENERATED = [w1, w2, b] = ",l4)

    
print("...ENTER YOU INPUTS IN BIPOLAR NOTATION...")
n = int(input("Enter the number of inputs: - "))
print("...ENTER THE INPUTS IN THE ORDER: [x1, x2, b, y]...")
lst = [] 
for i in range(0, n): 
    ele = [int(input()), int(input()), int(input()), int(input())] 
    lst.append(ele)

print("...HERE ARE YOUR INPUTS AS GIVEN BELOW...")
print(lst)
print("\n")
Hebb(lst)
