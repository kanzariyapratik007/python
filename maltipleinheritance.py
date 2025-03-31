class pratik:
    back="orecal db"
    def backend(self):
        print ("backend using",self.back)
class satish:
    funt="html css"
    def funtend(self):
        print ("funtend useing",self.funt)
class leader(pratik,satish):
    def fun(self):
        print ("creted website")
t1=leader()
t1.backend()
t1.funtend()
t1.fun()                        