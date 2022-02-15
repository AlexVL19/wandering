class trail:
    def __init__(self, x, y):
        self.x = x
        self.y = y
    
    def move(self, dx, dy):
        return trail(self.x + dx, self.y + dy)

    def distance (self, other_trail):
        dx = self.x - other_trail.x
        dy = self.y - other_trail.y

        return (dx**2 + dy**2)**0.5