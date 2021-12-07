from member import Member
from joint import Joint
from coordinate import Coordinate
class Truss:
    def __init__(self,filename="Default",joint_list = [],member_list = []):
        self.filename = filename
        self.joint_list = joint_list
        self.member_list = member_list
    def add_member(self,member:Member):
        self.member_list.append(member)
    def add_joint(self,joint:Joint):
        self.joint_list.append(joint)
    def delete_member(self,id:int):
        # Removes member with given id, which will be at
        # the id-1 index in the list 
        self.member_list.pop(id-1)
        # needed to preserve ID integrity 
        self.reassign_member_ids()
    def delete_joint(self,id:int):
        # same logic as with delete_member
        self.joint_list.pop(id-1)
        # needed to preserve ID integrity
        self.reassign_joint_ids()
    def get_number_members(self):
        return len(self.member_list)
    def get_number_joints(self):
        return len(self.joint_list)
    def is_valid(self):
        valid = True
        for member in self.member_list:
            end1_supported = False
            end2_supported = False
            end1,end2 = member.get_member_location()
            for joint in self.joint_list:
                if (end1.get_coordinate() == joint.get_joint_location().get_coordinate()):
                    end1_supported = True
                if (end2.get_coordinate() == joint.get_joint_location().get_coordinate()):
                    end2_supported = True
            if not end1_supported and not end2_supported:
                valid = False
                break
        return valid
    def reassign_joint_ids(self):
        for count,joint in enumerate(self.joint_list):
            joint.id = count
    def reassign_member_ids(self):
        for count,member in enumerate(self.member_list):
            member.id = count
