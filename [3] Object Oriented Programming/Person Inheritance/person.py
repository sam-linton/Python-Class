class Person:
    def __init__(self, first, last):
        self._first = first
        self._last = last
        
    def full_name(self):
        return self._first + ' ' + self._last
    
    
# Test program
if __name__ == '__main__':
    person = Person('Frodo', 'Beanberg')
    print(person.full_name())
