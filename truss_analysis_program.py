import matplotlib.pyplot as plt
import scipy.io as sio
import numpy as np
import math
from coordinate import get_distance
from truss import Truss 

EPSILON = 1.0E-7
TRUSS_COST_P_IN = 1
JOINT_COST = 10
def generate_validation_data():

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
def convert_truss_to_matrix(truss:Truss):
    if not truss.is_valid():
        print('Truss is not valid!')
        return 0
    # Generates C matrix 
    Cm = np.zeros((truss.get_number_joints(),truss.get_number_members()))
    for i,member in enumerate(truss.member_list):
        for j,joint in enumerate(truss.joint_list):
            if (get_distance(member.coordinate1,joint.coordinate)==0) or (get_distance(member.coordinate2,joint.coordinate)==0):
                Cm[j][i] = 1
    # Generates Sx and Sy matrices
    Sx = np.zeroes((truss.get_number_joints(),3))
    Sy = np.zeroes((truss.get_number_joints(),3))
    for i, joint in enumerate(truss.joint_list):
        if(joint.support==1):
            Sx[i][0] = 1
            Sy[i][1] = 1
        if(joint.support==2):
            Sy[i][2] = 1
    # Generates Xm and Ym lists
    Xm = np.zeroes(truss.get_number_joints())
    Ym = np.zeroes(truss.get_number_joints())
    for index, joint in enumerate(truss.joint_list):
        Xm[index] = joint.coordinate.x_coord
        Ym[index] = joint.coordinate.y_coord
    # Generates load list
    Lxm = np.zeroes(truss.get_number_joints())
    Lym = np.zeroes(truss.get_number_joints())
    for index, joint in enumerate(truss.joint_list):
        Xm[index] = joint.x_load
        Ym[index] = joint.y_load
    # I know I could do those two loops in one go but 
    # this makes the code more readable and it's all 
    # happening in user real time anyone (hopefully)
    Lm = np.append(Lxm,Lym)
    data_dict = {"C": Cm,
                "Sx": Sx,
                "Sy": Sy,
                "X": Xm,
                "Y": Ym,
                "L": Lm}
    return data_dict
def read_data(dict_name):

    # Data file will have C,Sx,Sy,X,Y,L
    tempmat = dict_name
    C = tempmat["C"]
    Sx = tempmat["Sx"]
    Sy = tempmat["Sy"]
    X = tempmat["X"]
    Y = tempmat["Y"]
    L = tempmat["L"]
    return C,Sx,Sy,X,Y,L
def analyze_system(truss:Truss):
    C,Sx,Sy,X,Y,L = read_data(convert_truss_to_matrix(truss))
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
def get_cost(truss:Truss):
    cost = 0
    cost += truss.joint_list.size*JOINT_COST
    for member in truss.member_list:
        cost+=member.get_length()*TRUSS_COST_P_IN
    return cost
def run(truss:Truss):
    # Prints the load uWu
    #C,Sx,Sy,X,Y,L = read_data(file_name)
    total_load = 0
    for joint in truss.joint_list:
        total_load+=(joint.x_load + joint.y_load)
    #total_load = int(0)
    #for element in L[0]:
    #    total_load+=int(element)
    print("EK327 Bodyguard Team Project")
    print("Load: " + str(total_load) + " oz")
    # Prints the members and stuff
    T = analyze_system(truss)
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

    total_cost = get_cost(truss)
    
    print("Cost of truss: $" + str(total_cost))
    print("Theoretical max load/cost ratio in oz/$: " + str(total_load/total_cost))

