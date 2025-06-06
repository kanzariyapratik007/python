def dec(fun):
    def frist(**w):
        print("This is frist")
        num=w+r
        print(num)
        fun()
        def second(a,b):
            c=a+b
            print("add",c)
            def third(x,y):
                z=x-y
                print("sub",z)
            third(5,3)
        second(5,3)
    frist(3)
@dec
def fri():
    print("This is fri")
    def sec(p,q):
        r=p*q
        print("mul",r)
        def thi(e,f):
            d=e/f
            print("div",d)
        thi(10,5)
    sec(2,3)
fri()





