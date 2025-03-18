class Rhombus:
    def __init__(self, side_a: float, angle_a: float):
        self.side_a = side_a
        self.angle_a = angle_a
    
    # Control setting of attributes 
    def __setattr__(self, name, value):
        # Make rules for our attributes
        if name == "side_a":
            if value <= 0:
                raise ValueError("Side must be more than 0.")
        elif name == "angle_a":
            if not (0 < value < 180):
                raise ValueError("Angle must be between 0 and 180")
            object.__setattr__(self, "angle_b", 180 - value)
        
        # Approve and set attributes
        object.__setattr__(self, name, value)
    
    # Dont allow to set angle β only for reading
    @property
    def angle_b(self):
        return self._angle_b

rhombus = Rhombus(4,20)
print("Side a:", rhombus.side_a)
print("Angle α:", rhombus.angle_a)
print("Angle β:", rhombus.angle_b)
    


 