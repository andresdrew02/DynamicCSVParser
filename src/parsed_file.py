class ParsedFile:
    def __init__(self, headers, data):
        if type(headers).__name__ not in ('list', 'tuple'):
            raise TypeError('headers must be a list or tuple')
        if type(data).__name__ not in ('list', 'tuple'):
            raise TypeError('data must be a list or tuple')
        
        self.headers = headers
        self.data = data
    
    def __init__(self):
        self.headers = []
        self.data = []
    
    def check_empty(self):
        if self.headers == [] or self.data == []:
            return True
        else:
            return False