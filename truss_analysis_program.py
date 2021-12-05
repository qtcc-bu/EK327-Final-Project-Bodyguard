import matplotlib.pyplot as plt
import scipy.io as sio
import numpy as np
import math
EPSILON = 1.0E-7
TRUSS_COST_P_IN = 1
JOINT_COST = 10
def generate_validation_data():
    # Data file will have C,Sx,Sy,X,Y,L
    Cm = np.array([
        #1,2,3,4,5,6,7,8,9,A,B,C,D truss/joint 
        [1,1,0,0,0,0,0,0,0,0,0,0,0], # A
        [1,0,1,1,0,0,0,0,0,0,0,0,0], # B
        [0,0,0,1,1,1,0,0,0,0,0,0,0], # C
        [0,1,1,0,1,0,1,1,0,0,0,0,0], # D
        [0,0,0,0,0,1,1,0,1,1,0,0,0], # E
        [0,0,0,0,0,0,0,1,1,0,1,1,0], # F
        [0,0,0,0,0,0,0,0,0,1,1,0,1], # G
        [0,0,0,0,0,0,0,0,0,0,0,1,1]  # H
    ])
    Sx = np.array([
        #Ax,Ay,Hy
        [1,0,0],
        [0,0,0],
        [0,0,0],
        [0,0,0],
        [0,0,0],
        [0,0,0],
        [0,0,0],
        [0,0,0],
    ])
    Sy = np.array([
        #Ax,Ay,Hy
        [0,1,0],
        [0,0,0],
        [0,0,0],
        [0,0,0],
        [0,0,0],
        [0,0,0],
        [0,0,0],
        [0,0,1],
    ])
    # assuming origin at point A 
    #    A,B,C,D,E,F,G,H
    Xm = [0,0,4,4,8,8,12,12]
    Ym = [0,4,8,4,8,4,4,0]
    #    A,B,C,D,E,F,G,H
    Lm = [0,0,0,0,0,0,0,0, #horizontal load
         0,0,0,25,0,0,0,0] #vertical load 
         # yes the 25 is supposed to be positive
    data_dict = {"C": Cm,
                "Sx": Sx,
                "Sy": Sy,
                "X": Xm,
                "Y": Ym,
                "L": Lm}
    sio.savemat("validationproblem.mat",data_dict)
def generate_design_one():
    # Data file will have C,Sx,Sy,X,Y,L
    Cm = np.array([
        #1,2,3,4,5,6,7,8,9,A,B,C,D,E,F,G,H truss/joint 
        [1,0,0,0,0,1,0,0,0,0,0,0,0,0,0,0,0], # A
        [1,1,0,0,0,0,1,1,0,0,0,0,0,0,0,0,0], # B
        [0,1,1,0,0,0,0,0,1,0,0,0,0,0,0,0,0], # C
        [0,0,1,1,0,0,0,0,0,1,1,1,0,0,0,0,0], # D
        [0,0,0,1,1,0,0,0,0,0,0,0,1,0,0,0,0], # E
        [0,0,0,0,1,0,0,0,0,0,0,0,0,1,0,0,0], # F
        [0,0,0,0,0,1,1,0,0,0,0,0,0,0,1,0,0], # G
        [0,0,0,0,0,0,0,1,1,1,0,0,0,0,1,1,0], # H
        [0,0,0,0,0,0,0,0,0,0,1,0,0,0,0,1,1], # I
        [0,0,0,0,0,0,0,0,0,0,0,1,1,1,0,0,1]  # J
    ])
    Sx = np.array([
        #Ax,Ay,Hy
        [1,0,0], # A
        [0,0,0], # B
        [0,0,0], # C
        [0,0,0], # D
        [0,0,0], # E
        [0,0,0], # F
        [0,0,0], # G
        [0,0,0], # H
        [0,0,0], # I
        [0,0,0] # J
    ])
    Sy = np.array([
        #Ax,Ay,Hy
        [0,1,0], # A
        [0,0,0], # B
        [0,0,0], # C
        [0,0,0], # D
        [0,0,0], # E
        [0,0,0], # F
        [0,0,0], # G
        [0,0,0], # H
        [0,0,0], # I
        [0,0,1] # J
    ])
    # assuming origin at point A 
    #     A, B, C, D, E, F, G, H, I, J
    Xm = [00,10,20,30,40,50,10,20,30,40]
    Ym = [00,00,00,00,00,00, 8, 8, 8, 8]
    #     A,B,C,D,E,F,G,H,I,J
    Lm = [0,0,0,0,0,0,0,0,0,0, #horizontal load
         0,0,0,18,0,0,0,0,0,0] #vertical load 
         # yes the 25 is supposed to be positive
    data_dict = {"C": Cm,
                "Sx": Sx,
                "Sy": Sy,
                "X": Xm,
                "Y": Ym,
                "L": Lm}
    sio.savemat("design1.mat",data_dict)
def generate_design_two():
    # Data file will have C,Sx,Sy,X,Y,L
    Cm = np.array([
        #1,2,3,4,5,6,7,8,9,A,B,C,D,E,F truss/joint 
        [1,0,0,0,0,1,0,0,0,0,0,0,0,0,0], # A
        [1,1,0,0,0,0,1,0,0,0,0,0,0,0,0], # B
        [0,1,1,0,0,0,0,1,1,0,0,0,0,0,0], # C
        [0,0,1,1,0,0,0,0,0,1,1,0,0,0,0], # D
        [0,0,0,1,1,0,0,0,0,0,0,1,0,0,0], # E
        [0,0,0,0,1,0,0,0,0,0,0,0,1,0,0], # F
        [0,0,0,0,0,0,0,0,0,0,1,1,1,0,1], # G
        [0,0,0,0,0,0,0,0,1,1,0,0,0,1,1], # H
        [0,0,0,0,0,1,1,1,0,0,0,0,0,1,0] # I
    ])
    Sx = np.array([
        #Ax,Ay,Hy
        [1,0,0], # A
        [0,0,0], # B
        [0,0,0], # C
        [0,0,0], # D
        [0,0,0], # E
        [0,0,0], # F
        [0,0,0], # G
        [0,0,0], # H
        [0,0,0] # I

    ])
    Sy = np.array([
        #Ax,Ay,Hy
        [0,1,0], # A
        [0,0,0], # B
        [0,0,0], # C
        [0,0,0], # D
        [0,0,0], # E
        [0,0,1], # F
        [0,0,0], # G
        [0,0,0], # H
        [0,0,0] # I

    ])
    # assuming origin at point A 
    #     A, B, C, D, E, F, G, H, I,
    Xm = [ 0, 6,12,30,36,42,33,21, 9]
    Ym = [00,00,00,00,00,00, 5.196, 15.589, 5.196]
    #     A,B,C,D,E,F,G,H,I
    Lm = [0,0,0,0,0,0,0,0,0, #horizontal load
         0,0,0,2,0,0,0,0,0] #vertical load 
         # yes the 25 is supposed to be positive
    data_dict = {"C": Cm,
                "Sx": Sx,
                "Sy": Sy,
                "X": Xm,
                "Y": Ym,
                "L": Lm}
    sio.savemat("design2.mat",data_dict)
def generate_final_design():
    # Data file will have C,Sx,Sy,X,Y,L
    Cm = np.array([
        #1,2,3,4,5,6,7,8,9,A,B,C,D,E,F,G,H truss/joint 
        [1,0,0,0,1,0,0,0,0,0,0,0,0,0,0,0,0], # A
        [1,1,0,0,0,1,1,0,0,0,0,0,0,0,0,0,0], # B
        [0,1,1,0,0,0,0,1,1,1,0,0,0,0,0,0,0], # C
        [0,0,1,1,0,0,0,0,0,0,1,1,0,0,0,0,0], # D
        [0,0,0,1,0,0,0,0,0,0,0,0,1,0,0,0,0], # E
        [0,0,0,0,1,1,0,0,0,0,0,0,0,1,0,0,0], # F
        [0,0,0,0,0,0,0,0,0,0,0,1,1,0,0,0,1], # G
        [0,0,0,0,0,0,1,1,0,0,0,0,0,1,1,0,0], # H
        [0,0,0,0,0,0,0,0,1,0,0,0,0,0,1,1,0], # I
        [0,0,0,0,0,0,0,0,0,1,1,0,0,0,0,1,1], # J
        
    ])
    Sx = np.array([
        #Ax,Ay,Hy
        [1,0,0], # A
        [0,0,0], # B
        [0,0,0], # C
        [0,0,0], # D
        [0,0,0], # E
        [0,0,0], # F
        [0,0,0], # G
        [0,0,0], # H,
        [0,0,0], # I,
        [0,0,0] # J,


    ])
    Sy = np.array([
        #Ax,Ay,Hy
        [0,1,0], # A
        [0,0,0], # B
        [0,0,0], # C
        [0,0,0], # D
        [0,0,1], # E
        [0,0,0], # F
        [0,0,0], # G
        [0,0,0], # H
        [0,0,0], # I,
        [0,0,0] # J,


    ])
    # assuming origin at point A 
    #     A, B, C, D, E, F, G, H, I, J
    Xm = [0,7.5,15,22.5,30,3.75,26.25,7.5,15,22.5]
    Ym = [0,0,0,0,0,3.75,3.75,7.5,7.5,7.5]
    #     A,B,C,D,E,F,G,H,I,J
    Lm = [0,0,0,0,0,0,0,0,0,0, #horizontal load
          0,0,54.6,0,0,0,0,0,0,0] #vertical load 
         # yes the 25 is supposed to be positive
    data_dict = {"C": Cm,
                "Sx": Sx,
                "Sy": Sy,
                "X": Xm,
                "Y": Ym,
                "L": Lm}
    sio.savemat("final.mat",data_dict)
def read_data(file_name):
    # Data file will have C,Sx,Sy,X,Y,L
    tempmat = sio.loadmat(file_name)
    C = tempmat["C"]
    Sx = tempmat["Sx"]
    Sy = tempmat["Sy"]
    X = tempmat["X"]
    Y = tempmat["Y"]
    L = tempmat["L"]
    return C,Sx,Sy,X,Y,L
def analyze_system(file_name):
    C,Sx,Sy,X,Y,L = read_data(file_name)
    X = X[0]
    Y = Y[0]
    A_x_half = C.astype(float)
    A_y_half = C.astype(float)
    #print(C)
    colindex = 0
    for column in C.T:
        index = 0
        pos1 = 0
        pos2 = 0
        # grabs coordinate index of the column
        while(index<len(column)):
            if (column[index]==1 and pos1==0):
                pos1 = index
            elif (column[index]==1):
                pos2 = index
            index=index+1
        # reuses pos1 and pos2 for exact coordinates
        x1 = X[pos1]
        y1 = Y[pos1]
        x2 = X[pos2]
        y2 = Y[pos2]
        distance = (math.sqrt(((x2-x1)**2)+((y2-y1)**2)))
        newx1 = float(x2-x1)/distance
        newx2 = float(x1-x2)/distance
        newy1 = float(y2-y1)/distance
        newy2 = float(y1-y2)/distance
        A_x_half[pos1][colindex] = newx1
        A_x_half[pos2][colindex] = newx2
        A_y_half[pos1][colindex] = newy1
        A_y_half[pos2][colindex] = newy2
        colindex=colindex+1
    #print(A_x_half)
    #print(A_y_half)
    #print(A_x_half[0][0])
    A_x = np.append(A_x_half,Sx,axis=1)
    A_y = np.append(A_y_half,Sy,axis=1)
    A = np.append(A_x,A_y,axis=0)
    A_inv = np.linalg.inv(A)
    #print(A_inv.shape)
    T = np.matmul(A_inv,L.T)
    i = 0
    while(i<abs(len(T))):
        if abs(T[i])<EPSILON:
            T[i]=0
        i=i+1
    return T
def get_cost(file_name):
    C,Sx,Sy,X,Y,L = read_data(file_name)
    X = X[0]
    Y = Y[0]
    # Calculates the cost from trusses
    trusses_cost = int(0)
    for column in C.T:
        index = 0
        pos1 = 0
        pos2 = 0
        # grabs coordinate index of the column
        while(index<len(column)):
            if (column[index]==1 and pos1==0):
                pos1 = index
            elif (column[index]==1):
                pos2 = index
            index=index+1
        # reuses pos1 and pos2 for exact coordinates
        x1 = X[pos1]
        y1 = Y[pos1]
        x2 = X[pos2]
        y2 = Y[pos2]
        distance = (math.sqrt(((x2-x1)**2)+((y2-y1)**2)))
        trusses_cost+=distance*TRUSS_COST_P_IN
    
    # Calculates Joint Cost 
    joint_number = len(C.T[0])
    joint_cost = joint_number*JOINT_COST

    #returns total cost
    return joint_cost+trusses_cost
def run(file_name):
    # Prints the load uWu
    C,Sx,Sy,X,Y,L = read_data(file_name)
    total_load = int(0)
    for element in L[0]:
        total_load+=int(element)
    print("EK301, A4, Group?: Quentin C, Alejandro R, Dongwoo K")
    print("Load: " + str(total_load) + " oz")
    # Prints the members and stuff
    T = analyze_system(file_name)
    print("Member forces in oz:")
    i = 0
    while(i<len(T)-3):
        comptomp = ""
        if (T[i]<0):
            comptomp = "C"
        else:
            comptomp = "T"
        print("m"+str(i+1)+": "+str(abs(T[i]))+" "+comptomp)
        i=i+1
    #i=i+1
    print("Reaction forces in oz:")
    print("Sx1: " + str(T[i]))
    i=i+1
    print("Sy1: " + str(T[i]))
    i=i+1
    print("Sy2: " + str(T[i]))

    total_cost = get_cost(file_name)
    
    print("Cost of truss: $" + str(total_cost))
    print("Theoretical max load/cost ratio in oz/$: " + str(total_load/total_cost))
    
#generate_validation_data()
#generate_validation_data()
generate_final_design()
#generate_design_two()
run("final.mat")
#run("design2.mat")
#run("validationproblem.mat")