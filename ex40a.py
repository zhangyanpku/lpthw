class MyStuff(object):
    
    def __init__(self):  #initialize your empty object
        self.tangerine = "And now a thousand years between"
    
    def apple(self):
        print("I AM CLASS APPLES")
thing = MyStuff() #The instantiate opeartion, craft an empty object with all the functions specified in the class using def
thing.apple()
print(thing.tangerine)