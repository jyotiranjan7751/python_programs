class A:
    def __init__(self):
        print("From class a")
        
class B(A):
    def __init__(self):
        super().__init__()
        print("From class B")
        
obj=B()
    
