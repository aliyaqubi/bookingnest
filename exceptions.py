class StoryException(Exception):
    def __init__(self, name: str):
        self.name = name


#> Share by Jurgen
#class MyException(Exception):
#    passraise MyException("My hovercraft is full of eels")
    