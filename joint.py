import coordinate
class Joint:
    def _init_(self,id:int,coordinate:coordinate.Coordinate):
        self.id = id
        self.coordinate = coordinate
    def get_joint_location(self):
        return self.coordinate