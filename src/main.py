import matplotlib.pyplot as plt
import scipy.io as sio
import numpy as np
import math
from coordinate import Coordinate, get_distance
from member import Member
from truss import Truss 
from joint import Joint
from truss_analysis_program import run

#displays 
def display(truss:Truss):
    jx=np.array([])
    jy=np.array([])
   

    ##plots joint
    for i in truss.joint_list:
        jx=np.append(jx,float(i.coordinate.x_coord))
        jy=np.append(jy,float(i.coordinate.y_coord))
    plt.scatter(jx,jy,color="blue")

    #plot loads
    l=np.array([])
    angle=np.array([])
    #calculates angle and magntude of loads
    for i in truss.joint_list:
        l=np.append(l,float(math.sqrt(math.pow(float(i.x_load),2)+math.pow(float(i.y_load),2)))) #magnitude
        if(int(i.x_load)==0):
            angle=np.append(angle,math.pi/2)
        else:
            angle=np.append(angle,math.atan(float(i.y_load)/float(i.x_load))) #angle
        #scales load
        if(np.amax(l)!=0):
            l=l/np.amax(l)
#actually plots loads
    for i in range(len(l)):
        if(float(l[i])!=0):
            print("\n****\n")
            plt.plot([float(truss.joint_list[i].coordinate.x_coord),float(truss.joint_list[i].coordinate.x_coord)+float(l[i])*math.cos(angle[i])],[float(truss.joint_list[i].coordinate.y_coord),float(truss.joint_list[i].coordinate.y_coord)+float(l[i])*math.sin(angle[i])],color="gray")
    
    #plots members

    for i in truss.member_list:
       plt.plot([float(i.coordinate1.x_coord), float(i.coordinate2.x_coord)],[float(i.coordinate1.y_coord), float(i.coordinate2.y_coord)] , 'g')
    plt.show()

##NOTe WELL!! Id is index+1 for joint list and memberlist

def main():
    ##Program header
    print("\nT R U S S   A N A L Y S I S\nQuentin Clark, Sebastian Gangemi, Dixon Rand, Robert D'Antonio\nEC327 Fall 2021\n\n")


    ##first we input the jpints
    hasjointamount=False
    jointlist=[]
##finds out joint amount with error checking
    while(hasjointamount==False):
        num=input("Enter number of joints: ")
        if(num.isnumeric()==False):
              print("You must enter an integer!\n")
        else:
            hasjointamount=True  

##gets cordinate for each joint with error checking
    for i in range(int(num)):
        print("\nJOINT ",i+1)

        hasx=False
        while(hasx==False):
            x=input("Enter x coordinate: ")
            hasx=True
            try:
                float(x)
            except ValueError:
                hasx=False
                print("Thats not a number!\nTry again\n")

        hasy=False
        while(hasy==False):
            y=input("Enter y coordinate: ")
            hasy=True
            try:
                float(y)
            except ValueError:
                hasy=False
                print("Thats not a number!\nTry again\n")

        ##Checks what support type the joint is
        knowssupport=False
        while (knowssupport==False) :
            s=input("If joint Has no support, enter '0', if joint has pin support, enter '1', and if joint has roller support, enter '2': ")
            is_int=True
            try:
                int(s)
            except ValueError:
                is_int=False
            if(is_int==False):
                print("You can only input 0, 1, or 2!\n")
            elif(int(s)==0 or int(s)==1 or int(s)==2):
                knowssupport=True
            else:
                print("You can only input 0, 1, or 2!!\n")
        s = int(s)
        #Xload
        knowxload=False
        while(knowxload==False):
            xload=input("Enter horizontal load on this joint (Note that a negative input indicates a rightward force): ")
            knowxload=True
            try:
                float(xload)
            except ValueError:
                print("Load must be a number!")
                knowxload=False

        #Yload
        knowyload=False
        while(knowyload==False):
            yload=input("Enter vertical load on this joint (Note that a negative input indicates an upward force): ")
            knowyload=True
            try:
                float(yload)
            except ValueError:
                print("Load must be a number!")
                knowyload=False


        ##adds joint to joint list
        jointlist.append(Joint(id=i+1,coordinate=Coordinate(x,y),support=s,x_load=xload,y_load=yload))
    

    #second we make them input the members
    #error check for member amount input
    hasmemberamount=False
    memberlist=[]
    
    while(hasmemberamount==False):
        mem=input("\nEnter total number of members: ")
        if(mem.isnumeric()==False):
              print("You must enter an integer!\n")
        elif((int(num)==0 or int(num==1)) and int(mem)>0):
            print("Too many members for joints!")
        else:
            hasmemberamount=True


    #adds coordinates of member byjoint ids
    for i in range(int(mem)):
        print("\nMEMBER ",i+1)
        hasfirst=False
        #gets id of first joint with error check that is int and is one of joints
        while(hasfirst==False):
            is_int=True
            jid1=input("What is the ID of the first joint it is connected to? ")
            try:
                int(jid1)
            except ValueError:
                print("Must be an integer!")
                is_int=False
            if(is_int):
                if((int(jid1)>0 and int(jid1)<=int(num))==False):
                    print("ID must be in range of total amount of joints.")
                else:
                     hasfirst=True

        #gets id of second joint with error check that is int and is one of joints that is not first joint
        hassecond=False
        while(hassecond==False):
            is_int=True
            jid2=input("What is the ID of the second joint it is connected to? ")
            try:
                int(jid2)
            except ValueError:
                print("Must be an integer!")
                is_int=False
            if(is_int):
                if((int(jid2)>0 and int(jid2)<=int(num))==False):
                    print("ID must be in range of total amount of joints.")
                elif(jid1==jid2):
                    print("First joint and second joint can't be the same!")
                else:
                    hassecond=True

            #add member list
        memberlist.append(Member(id=i+1,coordinate1=jointlist[int(jid1)-1].get_joint_location(),coordinate2=jointlist[int(jid2)-1].get_joint_location()))


###saves truss
    file=input("\nWhat would you like the truss name to be (may save over if repeated name): ")
    print("Saving truss...")
    thetruss=Truss(filename=file,joint_list=jointlist,member_list=memberlist) 

    #Options menu
    ison=True
    while(ison):
            #list  options
            print("\n\nOPTIONS:\n'D' to display truss (NOTE: truss window will have to be closed before continuing)\n'M' for adding a member\n'N' for deleting a member\n'J' for adding a Joint\n'H' for deleting a joint\n'V' for viewing information on truss\n'Q' to quit program\n")

            #input options
            option=input("Enter input: ")
            option=option.upper()
            
            #execute given option

            #quit
            if(option=="Q"):
                ison=False
            
            elif(option=="D"):
                print("Displaying truss")
                display(thetruss)
                
            elif(option=="V"):
                #totalcost = get_cost(thetruss)
                #print("Cost of Truss: $" + str(totalcost))
                run(thetruss)
                input("Press ENTER to continue")
                
            #add member to truss
            elif(option=="M"):
                print("Member ",len(thetruss.member_list)+1)
                hasfirst=False
                 #gets id of first joint with error check that is int and is one of joints
                while(hasfirst==False):
                     is_int=True
                     jid1=input("What is the ID of the first joint it is connected to? ")
                     try:
                        int(jid1)
                     except ValueError:
                         print("Must be an integer")
                         is_int=False
                     if(is_int):
                             if((int(jid1)>0 and int(jid1)<=len(thetruss.joint_list))==False):
                                print("ID must be in range of total amount of joints")
                             else:
                                 hasfirst=True

                #gets id of second joint with error check that is int and is one of joints that is not first joint
                hassecond=False
                while(hassecond==False):
                    is_int=True
                    jid2=input("What is the ID of the second joint it is connected to?")
                    try:
                          int(jid2)
                    except ValueError:
                         print("Must be an integer")
                         is_int=False
                    if(is_int):
                         if((int(jid2)>0 and int(jid2)<=len(thetruss.joint_list))==False):
                              print("ID must be in range of total amount of joints")
                         elif(jid1==jid2):
                             print("First joint and second joint can't be the same!")
                         else:
                            hassecond=True

                #adds member to jointlist of truss
                thetruss.add_member(Member(id=len(thetruss.member_list)+1,coordinate1=thetruss.joint_list[int(jid1)-1].coordinate,coordinate2=thetruss.joint_list[int(jid2)-1].coordinate))
                input("New member successfully added. Press ENTER to continue")

            #adds joints
            elif(option=='J'):
                print("Joint ",len(thetruss.joint_list)+1)
                #user inputs xcoord
                hasx=False
                while(hasx==False):
                    xin=input("Enter x coordinate: ")
                    hasx=True
                    try:
                        float(xin)
                    except ValueError:
                        hasx=False
                        print("Must be a number!")
                #user inputs y coord
                hasy=False
                while(hasy==False):
                    yin=input("Enter y coordinate: ")
                    hasy=True
                    try:
                        float(yin)
                    except ValueError:
                        hasy=False
                        print("Must be a number!")

                #user inputs support type
                hassupport=False
                while(hassupport==False):
                    sup=input("If joint Has no support, enter '0', if joint has pin support, enter '1', and if joint has roller support, enter '2': ") 
                    isint=True
                    try:
                        int(sup) 
                    except ValueError:
                        isint=False 
                    if(isint):
                        if(int(sup)==0 or int(sup)==1 or int(sup)==2):
                            hassupport=True
                        else:
                            print("Must be 0, 1, or 2!!")       
                 #Xload
                knowxload=False
                while(knowxload==False):
                    xload=input("Enter horizontal load on this joint (Note that a negative input indicates a rightward force): ")
                    knowxload=True
                    try:
                        float(xload)
                    except ValueError:
                        print("Load must be a number!")
                        knowxload=False

                 #Yload
                knowyload=False
                while(knowyload==False):
                    yload=input("Enter vertical load on this joint (Note that a negative input indicates an upward force): ")
                    knowyload=True
                    try:
                        float(yload)
                    except ValueError:
                        print("Load must be a number!")
                        knowyload=False
                thetruss.add_joint(Joint(id=len(thetruss.joint_list)+1,coordinate=Coordinate(x_coord=float(xin),y_coord=yin),support=sup,x_load=xload,y_load=yload))
                input("New joint successfully added. Press ENTER to continue")
                #deletes Member with error checking
            elif(option=="N"):
                hasid=False
                isint=False
                while(hasid==False):
                    id=input("What is the ID of the member which would would like to delete? ")
                    isint=True
                    try:
                        int(id)
                    except ValueError:
                        print("Must be an integer.")
                        isint=False
                    if(isint):
                        if((int(id)>0 and int(id)<=len(thetruss.member_list))==False):
                            print("Must be in range of members")
                        else:
                            hasid=True
                thetruss.delete_member(int(id))
                input("Member successfully deleted. Press ENTER to continue.")
            #deletes joint with error checking
            elif(option=="H"):
                hasid=False
                isint=False
                while(hasid==False):
                    id=input("What is the ID of the joint which would would like to delete? ")
                    isint=True
                    try:
                        int(id)
                    except ValueError:
                        print("Must be an integer")
                        isint=False
                    if(isint):
                        if((int(id)>0 and int(id)<=len(thetruss.joint_list))==False):
                            print("Must be in range of joints")
                        else:
                            hasid=True
                thetruss.delete_joint(int(id))
                input("Joint successfully deleted. Press ENTER to continue.")


main()
 
   






        
