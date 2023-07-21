
class myClass:
    def __init__(self):
        self._myAttribute = "spam, spam and more spam"
    
    def myMethod (self):
        return self._myAttribute
    
    def __str__(self):
        return f'{type(self._myAttribute)} {self._myAttribute}'