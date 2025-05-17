class A:
    def show(self):
        print("Class A has been created!")
        
class B(A):
    def show(self):
        print("Class B has been created that inherits class A!")
        
class C(A):
    def show(self):
        print("Class C has been created that inherits class A!")
        
class D(B, C):
    pass

d1 = D()
print(d1.show())