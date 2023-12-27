class sumja:
    def __init__(self,numbers,target):
        self.numbers =numbers
        self.target =target

    def find_theSum(self):
        for i in range(len(self.numbers)):
            for j in range(len(self.numbers)):
                if j >0:
                    if self.numbers[i]+self.numbers[j] ==self.target:
                        print('-----------')
                        return i,j
            

s1 =sumja([2,7,11,15],9)
print(s1.find_theSum())

s2=sumja([3,2,4],6)
print(s2.find_theSum())

s3=sumja([3,3],6)
print(s3.find_theSum())

