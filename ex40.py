#define the class
class Song(object):
    
    def __init__(self,lyrics): # self is needed to make it clear that self.lyrics is the instance attribute of the class instead of local variables
        self.lyrics = lyrics
        
    def sing_me_a_song(self):
        for line in self.lyrics:
            print(line)

happy_bday = Song(["Happy birthday to you","I don't want to get sued","So I'll stop right there"])
bulls_on_parade = Song(["They rally around the family", "With pocket full of shells"])

happy_bday.sing_me_a_song()

bulls_on_parade.sing_me_a_song()

