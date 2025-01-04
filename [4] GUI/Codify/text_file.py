
class TextFile:
    def __init__(self):
        self._text = ''
        
    @property
    def text(self):
        return self._text
    
    @text.setter
    def text(self, value):
        self._text = value
        
    def read_from(self, filepath):
        print(filepath)
        with open(filepath, 'r') as f:
            self._text = f.read()
            print('Read \n' + self._text)
    
    def save_to(self, filepath):
        print(filepath)
        with open(filepath, 'w') as f:
            f.write(self._text)
    
# Test App
if __name__ == '__main__':
    filename = 'test.txt'
    text_file = TextFile()
    text_file.text = 'Hello, world!'
    print(text_file.text)
    text_file.save_to(filename)
    text_file.read_from(filename)
    print(text_file.text)