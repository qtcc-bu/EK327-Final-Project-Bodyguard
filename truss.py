from member import Member
from joint import Joint
from coordinate import Coordinate
class Truss:
    def __init__(self,filename="Default",joint_list = [],member_list = []):
        self.filename = filename
        self.joint_list = joint_list
        self.member_list = member_list
    def add_member(self,id:int,coordinate1:Coordinate,coordinate2:Coordinate):
        self.member_list.append(Member(id,coordinate1,coordinate2))
    def add_joint(self,id:int,coordinate:Coordinate):
        self.joint_list.append(Joint(id,coordinate))
    def get_number_members(self):
        return self.member_list.size
    def get_number_joints(self):
        return self.joint_list.size
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