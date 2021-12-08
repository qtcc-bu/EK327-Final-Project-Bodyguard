import math
class Coordinate:
    def __init__(self,x_coord,y_coord):
        self.x_coord = x_coord
        self.y_coord = y_coord
    def get_coordinate(self):
        return self.x_coord,self.y_coord
    
def get_distance(coord1:Coordinate,coord2:Coordinate):
    x1,y1 = coord1.get_coordinate()
    x2,y2 = coord2.get_coordinate()
    return math.sqrt(math.pow((float(x2)-float(x1)),2)+math.pow((float(y2)-float(y1)),2))
