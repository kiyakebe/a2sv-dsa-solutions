class Robot:

    def __init__(self, width: int, height: int):
        self.dir = "East"
        self.pos = [0, 0]
        self.width = width-1
        self.height = height-1
        self.linear_pos = 0
        self.perimeter = self.height*2 + self.width*2
        # print()
        
    def step(self, num: int) -> None:
        # lets consider the path a linear path of lenght perimeter
        self.linear_pos = (self.linear_pos+num) % self.perimeter

        if 0 < self.linear_pos <= self.width:
            self.pos = [self.linear_pos, 0]
            self.dir = "East"
        elif self.width < self.linear_pos <= self.height + self.width:
            self.pos = [self.width, self.linear_pos-self.width]
            self.dir = "North"
        elif self.height + self.width < self.linear_pos <= self.height + self.width*2:
            self.pos = [(self.height + self.width*2) - self.linear_pos, self.height]
            self.dir = "West"
        else:
            if self.linear_pos == 0:
                self.pos = [0,0]
            else:
                self.pos = [0, self.perimeter-self.linear_pos]
                
            print(self.perimeter, self.linear_pos)
            self.dir = "South"

    def getPos(self) -> List[int]:
        return self.pos

    def getDir(self) -> str:
        return self.dir
        


# Your Robot object will be instantiated and called as such:
# obj = Robot(width, height)
# obj.step(num)
# param_2 = obj.getPos()
# param_3 = obj.getDir()