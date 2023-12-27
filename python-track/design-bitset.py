class Bitset:

    def __init__(self, size: int):
        self.bitset_list = [0 for i in range(size)]
        self.size = size
        self.count_one = 0
        self.isNotFliped = True

    '''
    defined custome function to convert 1 -> 0 and 0 -> 1
    to be used alternatively depending on isNotFliped value
    isNotFliped = True -> one is treated as one and
    isNotFliped = Fasle -> one is treated as zero and zeros are considered as one 
    '''
    def convert_one_to_zero(self, idx: int) -> None:
        if self.bitset_list[idx] == 1:
            self.bitset_list[idx] = 0
            self.count_one += -1 if self.isNotFliped else 1
        
    def convert_zero_to_one(self, idx: int) -> None:
        if self.bitset_list[idx] == 0:
            self.bitset_list[idx] = 1
            self.count_one += 1 if self.isNotFliped else -1

    def fix(self, idx: int) -> None:
        # call functions based on the condition
        if self.isNotFliped:
            self.convert_zero_to_one(idx)
        else:
            self.convert_one_to_zero(idx)        

    def unfix(self, idx: int) -> None:
        #call function based of function
        if self.isNotFliped:
            self.convert_one_to_zero(idx)
        else:
            self.convert_zero_to_one(idx)

    def flip(self) -> None:
        self.isNotFliped = not self.isNotFliped

        self.count_one = abs(self.count_one - self.size)

    def all(self) -> bool:
        return self.size == self.count_one

    def one(self) -> bool:
        return self.count_one > 0

    def count(self) -> int:
        return self.count_one

    def toString(self) -> str:
        if self.isNotFliped:
            return ''.join([str(i) for i in self.bitset_list])
        else:
            return ''.join([ '0' if i == 1 else '1' for i in self.bitset_list])



# Your Bitset object will be instantiated and called as such:
# obj = Bitset(size)
# obj.fix(idx)
# obj.unfix(idx)
# obj.flip()
# param_4 = obj.all()
# param_5 = obj.one()
# param_6 = obj.count()
# param_7 = obj.toString()