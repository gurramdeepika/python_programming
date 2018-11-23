
class access:
    def __init__(self,name):
        if __name__ == '__main__':
           self.name = name
        else:
            self.name = ''
            print('fields in this class cannot be editable')


a = access('deepika')

#dir(__builtins__) -- to get the namespaces









