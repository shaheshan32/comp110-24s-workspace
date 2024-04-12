"""Practice writing a class."""

#Definition
class Profile: 

    username: str
    private: bool

    def __init__(self, username_input: str) -> None:
        """Create a new profile object."""
        self.username = username_input
        self.private = True

    def tweet(self, msg: str) -> None: 
        """If profile is public, print msg."""
        if self.private is False: # or u can just write if not self.private, print(msg)
            print(msg)

#Instantiation
user1: Profile = Profile("110_rulez") #this calls __init__()
user1.private = False
# if function call tweet(user1, "oop is cool!")
#if method this below is the syntax
user1.tweet("OOP is cool!")