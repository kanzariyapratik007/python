#single inheritance

class a:
    vlue1=int(input("enter a fast vlue "))
    vlue2=int(input("enter a secand vlue "))
    def add(self):
        print("add", self.vlue1 + self.vlue2)
    def sub(self):
        print("sub",self.vlue1-self.vlue2)
class b(a):
    def mul(self):
        print("mul",self.vlue1*self.vlue2)
    def div(self):
        print("div",self.vlue1/self.vlue2)
    def rem(self):
        print("rem",self.vlue1%self.vlue2)
o1=b()
o1.add()
o1.sub()
o1.mul()
o1.div()
o1.rem()
                   
        
    
