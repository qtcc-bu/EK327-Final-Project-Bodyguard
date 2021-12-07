import matplotlib.pyplot as plt
import scipy.io as sio
import numpy as np
import math
from coordinate import Coordinate, get_distance
from member import Member
from truss import Truss 
from joint import Joint


##NOTe WELL!! Id is index+1 for joint list and memberlist

def main():
    ##first we input the jpints
    hasjointamount=False
    jointlist=[]
##finds out joint amount with error checking
    while(hasjointamount==False):
        num=input("How many Joints are there?  :")
        if(num.isnumeric()==False):
              print("You must enter an integer!\n")
        else:
            hasjointamount=True  

##gets cordinate for each joint with error checking
    for i in range(int(num)):
        print("Joint ",i+1)

        hasx=False
        while(hasx==False):
            x=input("What is x cord?  :")
            hasx=True
            try:
                float(x)
            except ValueError:
                hasx=False
                print("Thats not a number!\nTry again\n")

        hasy=False
        while(hasy==False):
            y=input("What is y cord?  :")
            hasy=True
            try:
                float(y)
            except ValueError:
                hasy=False
                print("Thats not a number!\nTry again\n")

        ##Checks what support type the joint is
        knowssupport=False
        while (knowssupport==False) :
            s=input("If joint Has no support, type '0', if joint has pin support, type '1', and if joint has roller support, type '2' ")
            if(int(s)==0 or int(s)==1 or int(s)==2):
                knowssupport=True
            else:
                print("You can only input 0 1 or 2!!\n")

        ##adds joint to joint list
        jointlist.append(Joint(id=i+1,coordinate=Coordinate(x,y),support=s))
    

    #second we make them input the members
    #error check for member amount input
    hasmemberamount=False
    memberlist=[]
    while(hasmemberamount==False):
        mem=input("How many members are there?  :")
        if(mem.isnumeric()==False):
              print("You must enter an integer!\n")
        else:
            hasmemberamount=True


    #adds coordinates of member byjoint ids
    for i in range(int(mem)):
        print("Member ",i+1)
        hasfirst=False
        #gets id of first joint with error check that is int and is one of joints
        while(hasfirst==False):
            is_int=True
            jid1=input("What is the id of the first joint it is connected to?")
            try:
                int(jid1)
            except ValueError:
                print("Must be int!")
                is_int=False
            if(is_int):
                if((int(jid1)>0 and int(jid1)<=int(num))==False):
                    print("Id must be in range of total amount of joints")
                else:
                     hasfirst=True

        #gets id of second joint with error check that is int and is one of joints that is not first joint
        hassecond=False
        #gets id of first joint with error check that is int and is one of joints
        while(hassecond==False):
            is_int=True
            jid2=input("What is the id of the second joint it is connected to?")
            try:
                int(jid2)
            except ValueError:
                print("Must be int!")
                is_int=False
            if(is_int):
                if((int(jid2)>0 and int(jid2)<=int(num))==False):
                    print("Id must be in range of total amount of joints")
                elif(jid1==jid2):
                    print("First joint and second joint can't be the same!")
                else:
                     hassecond=True


        



main()
