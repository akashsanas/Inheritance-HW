# HW

# Parent Class

class A :
    def show_A(self):
        print("This is class A",("Parent"))
    
# Hierarchical Inheritance

class B(A):
    def show_B(self):
        print("This is class B",("Child of A"))

class C(A):
    def show_C(self):
        print("This is class C",("Child of A"))

#Multilevel Inheritance

class E(B):
    def show_E(self):
        print("This is class E",("Child of B"))

class G(E):
    def show_G(self):
        print("This is class G",("Child of E"))

# Multiple Inheritance

class F(C,G):
    def show_F(self):
        print("This is class F",("Child of C,G"))

# Child(Viru)

class Viru(F):
    def show_Viru(self):
        print("Final child Viru")

v = Viru()

#Calling Method
v.show_A()
v.show_B()
v.show_C()
v.show_E()
v.show_F()
v.show_G()
v.show_Viru()

#MRO
print(type(Viru))
print(A.__mro__)
print(B.__mro__)
print(C.__mro__)
print(E.__mro__)
print(F.__mro__)
print(G.__mro__)