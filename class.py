class sample:
    x=2                 # class variable
    def get(self,y):
        self.y=y        #instance variable
s1=sample()
s1.get(3)
print(s1.x,s1.y)
s2=sample()
s2.y=4
print(s2.x,s2.y)
