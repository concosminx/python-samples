class MyError(TypeError):
    #pass
    """
    Exception raised for specific code!
    """
    def __init__(self, msg, code):
        super().__init__(f'Error code {code}: {msg}')
        self.code = code


#raise MyError('Oops! ... something bad happened', 500)

err = MyError('Oops! ... something bad happened', 500)
print(err.__doc__)