
class Curve:
    def __init__(self, color='white'):
        self.points = list()
        self.color = color
        self.currentx = None
        self.currenty = None
        
    def set_x(self, x):
        self.currentx = x
        
    def set_y(self, y):
        self.currenty = y
    
    def add_current_point(self):
        if not self.currentx or not self.currenty:
            return
        
        new_point = (self.currentx, self.currenty)
        if new_point not in self.points:
            self.points.append((self.currentx, self.currenty))
            
        # self.currentx = None
        # self.currenty = None
    
    def clear(self):
        self.points.clear()
        
    def draw(self, line, dot):
        for i in range(1, len(self.points)):
            line(self.points[i - 1], self.points[i], self.color)    
            dot((self.currentx, self.currenty), self.color)
            
                    