class Other(object):
    def override(self):
        print("OTHER override()")
    def implicit(self):
        print("OTHER implicit()")
    def altered(self):
        print("OTHER altered()")

class Child(object):
    def __init__(self):
        self.other = Other() #composition
    def override(self):
        print("CHILD override()")
    def implicit(self):
        self.other.implicit()
    def altered(self):
        print("CHILD, BEFORE OTHER altered()")
        self.other.altered()
        print("CHILD, AFTER OTHER altered()")
        
son = Child()
son.implicit() #OTHER implicit()
son.override() # CHILD override()
son.altered() # CHILD, BEFORE OTHER altered(); OTHER altered(); CHILD, AFTER OTHER altered()
    