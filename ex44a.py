#implicit inheritance
class Parent(object):
    def implicit(self):
        print("PARENT implicit()")

class Child(Parent):
    pass #The use of pass to tell python that you want an empty block, nothing new to define.

dad = Parent()
son = Child()
dad.implicit()
son.implicit()