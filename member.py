from coordinate import get_distance
import coordinate
class Member:
    def __init__(self,id:int,coordinate1:coordinate.Coordinate,coordinate2:coordinate.Coordinate):
        self.coordinate1 = coordinate1
        self.coordinate2 = coordinate2
        self.id = id
    def get_length(self):
        return get_distance(self.coordinate1,self.coordinate2)
    def get_member_location(self):
        return self.coordinate1,self.coordinate1
