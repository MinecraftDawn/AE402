class Human:
    def __init__(self, name):
        self.name = name
        
    def showName():
        print(self.name)
        
class Man(Human):
    def __init__(self, name, height):
        super().__init__(name)
        self.height = height
		

print(Man("Eric", 180).showName())