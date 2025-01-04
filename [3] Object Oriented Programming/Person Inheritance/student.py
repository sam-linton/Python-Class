from person import Person

class Student(Person):
    def __init__(self, first, last, grad_date):
        super().__init__(first, last)
        self._grad_date = grad_date
        
    def email(self):
        return self._grad_date[-2:] + \
               self._first + self._last[0] + \
               '@students.harker.org'


s = Student('Blinky', 'Beanburg', '2042')
print(s.full_name())
print(s.email())