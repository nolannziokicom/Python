class Myclass:
    __privatevar=21
    
    def __privMeth(self):
        print("I am inside my class")

    def hello(self):
        print("Private variable value", Myclass.__privatevar)

foo=Myclass()
foo.hello()
foo.__privMeth()