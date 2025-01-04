from person import Person

class Teacher(Person):
    def __init__(self, first, last):
        super().__init__(first, last)
        
    def email(self):
        return self._first + '.' + self._last + '@harker.og'
        
        
t = Teacher('Nikolai', 'Tesla')
print(t.full_name())
print(t.email())