import coordinate
class Joint:
    def __init__(self,id:int,coordinate:coordinate.Coordinate,x_load:float=0,y_load:float=0,support:int=0):
        self.id = id
        self.coordinate = coordinate
        self.x_load = x_load
        self.y_load = y_load
        self.support = support
        # The support integer tells you if it's the roller or pin joint that the truss
        # is held up by - and it uses the following key... 
        # 0 = regular joint
        # 1 = pin support
        # 2 = roller support 
    def get_joint_location(self):
        return self.coordinate