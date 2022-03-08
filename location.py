from trail import Trail


class Location:
    def __init__(self):
        self.location_wandering = {}
    
    def add_wandering(self, wandering, trail):
        self.location_wandering[wandering] = trail

    def move_wandering(self, wandering):
        dx, dy = wandering.walk()
        actualcoord = self.location_wandering[wandering]
        new_location = actualcoord.move(dx, dy)

        self.location_wandering[wandering] = new_location

    def get_location(self, wandering):
        return self.location_wandering[wandering]