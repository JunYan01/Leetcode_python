478Generate Random Point in a Circle

class Solution:

    def __init__(self, radius: float, x_center: float, y_center: float):
        self.radius = radius
        self.x_center, self.y_center = x_center, y_center

    def randPoint(self) -> List[float]:
        theta = math.pi * 2* random.random() 
        r = self.radius * math.sqrt(random.random())
        return self.x_center + r*math.cos(theta) , self.y_center + r*math.sin(theta)
        


# Your Solution object will be instantiated and called as such:
# obj = Solution(radius, x_center, y_center)
# param_1 = obj.randPoint()